from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..models.episode import Episode
from ..app import db

episode_bp = Blueprint("episode", __name__, url_prefix="/episodes")

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()

    return jsonify({"message": "Episode deleted"}), 200
