# 🌙 Late Show API 🎤

A Flask RESTful API to manage a late-night talk show, with support for user registration/login, guest appearances, and full token-based access control.

---

## ⚙️ Tech Stack

- Python 3
- Flask
- PostgreSQL
- Flask SQLAlchemy
- Flask Migrate
- Flask JWT Extended
- Postman (for testing)
- MVC folder structure

---

## 📁 Project Structure

.
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── init.py
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ └── appearance.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── auth_controller.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ └── appearance_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md

yaml
Copy
Edit

---

## 🚀 Setup Instructions

### ✅ 1. Clone and Install Dependencies

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
pipenv install
pipenv shell
```
✅ 2. PostgreSQL Setup
Create the database and user in psql:
```
sql
Copy
Edit
CREATE USER larry WITH PASSWORD '250515..';
ALTER USER larry WITH SUPERUSER;
CREATE DATABASE late_show_db OWNER larry;
Update your server/config.py:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "postgresql://larry:250515..@localhost:5432/late_show_db"
```
✅ 3. Initialize & Migrate DB
```
bash
Copy
Edit
export FLASK_APP=app_factory.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
✅ 4. Seed the Database
```
bash
Copy
Edit
python server/seed.py
```
✅ 5. Run the Server
```
bash
Copy
Edit
flask run
```
🔐 Authentication Flow
POST /register — Create user

POST /login — Login and receive a JWT token

Protected routes require:

makefile
Copy
Edit
Authorization: Bearer <your_token_here>
🧪 API Routes
Method	Endpoint	Auth	Description
POST	/register	❌	Register a new user
POST	/login	❌	Login and get JWT
GET	/guests	❌	List all guests
GET	/episodes	❌	List all episodes
GET	/episodes/<int:id>	❌	Get episode with guest appearances
DELETE	/episodes/<int:id>	✅	Delete an episode + its appearances
POST	/appearances	✅	Add a guest appearance to episode

📬 Postman Testing
Import: challenge-4-lateshow.postman_collection.json

Register and Login

Copy the JWT token

Set header for protected requests:

makefile
Copy
Edit
Authorization: Bearer <token>
✅ Submission Checklist
 MVC folder structure

 PostgreSQL used

 Models, validation, relationships complete

 JWT authentication implemented

 Protected routes enforced

 Seed data working

 All routes tested via Postman

 Clean, complete README

🔗 GitHub Repo
👉 https://github.com/larry6305/late-show-api-challenge

Built with 💙 by Larry

