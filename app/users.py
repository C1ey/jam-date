# app/users.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import db
from .models import User, Favourite

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    u = User.query.get_or_404(user_id)
    return jsonify(u.as_dict()), 200

@users_bp.route('/<int:user_id>/favourites', methods=['GET'])
@jwt_required()
def list_my_favourites(user_id):
    # you could also enforce user_id == get_jwt_identity()
    favs = Favourite.query.filter_by(user_id=get_jwt_identity()).all()
    return jsonify([f.as_dict() for f in favs]), 200

# add other user routes (e.g. top-N favourites) similarly…
