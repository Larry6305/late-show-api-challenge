from flask import Blueprint, jsonify
from ..models.episode import Episode
from ..app import db

episode_bp = Blueprint("episode", __name__, url_prefix="/episodes")

@episode_bp.route("", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {
            "id": e.id,
            "date": e.date.isoformat(),
            "number": e.number
        } for e in episodes
    ])

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "guest": {
                    "id": a.guest.id,
                    "name": a.guest.name
                }
            } for a in episode.appearances
        ]
    })
