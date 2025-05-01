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
    me = get_jwt_identity()
    favs = Favourite.query.filter_by(user_id=me).all()
    return jsonify([f.as_dict() for f in favs]), 200

@users_bp.route('/favourites/top/<int:n>', methods=['GET'])
@jwt_required()
def top_favourites(n):
    # count how many times each profile was favourited
    counts = db.session.query(
        Favourite.fav_profile_id,
        db.func.count(Favourite.id).label('count')
    ).group_by(Favourite.fav_profile_id) \
     .order_by(db.desc('count')) \
     .limit(n) \
     .all()

    result = []
    for profile_id, cnt in counts:
        from .models import Profile
        prof = Profile.query.get(profile_id)
        if prof:
            d = prof.as_dict()
            d['favourite_count'] = cnt
            result.append(d)

    return jsonify(result), 200
