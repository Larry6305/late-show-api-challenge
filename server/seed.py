from app import create_app, db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from datetime import date

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear tables
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Users (optional)
    user = User(username="larry")
    user.set_password("250515..")
    db.session.add(user)

    # Guests
    g1 = Guest(name="Zendaya", occupation="Actress")
    g2 = Guest(name="Elon Musk", occupation="Entrepreneur")
    g3 = Guest(name="Rihanna", occupation="Singer")

    db.session.add_all([g1, g2, g3])

    # Episodes
    e1 = Episode(date=date(2025, 6, 1), number=101)
    e2 = Episode(date=date(2025, 6, 2), number=102)

    db.session.add_all([e1, e2])
    db.session.commit()

    # Appearances
    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=4, guest_id=g2.id, episode_id=e1.id)
    a3 = Appearance(rating=5, guest_id=g3.id, episode_id=e2.id)

    db.session.add_all([a1, a2, a3])
    db.session.commit()

    print("✅ Done seeding!")
