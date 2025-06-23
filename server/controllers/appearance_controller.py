from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.appearance import Appearance
from ..models.guest import Guest
from ..models.episode import Episode
from ..app import db

appearance_bp = Blueprint("appearance", __name__, url_prefix="/appearances")

@appearance_bp.route("", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")

    if not all([rating, guest_id, episode_id]):
        return jsonify({"error": "All fields are required"}), 400

    if not Appearance.validate_rating(rating):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return jsonify({"error": "Guest or Episode not found"}), 404

    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )

    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        "id": appearance.id,
        "rating": appearance.rating,
        "guest": {"id": guest.id, "name": guest.name},
        "episode": {"id": episode.id, "number": episode.number}
    }), 201
