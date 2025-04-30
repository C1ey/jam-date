# app/profiles.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# grab the db instance directly from the package root
from . import db
# import only the Profile model class
from .models import Profile

profiles_bp = Blueprint('profiles', __name__, url_prefix='/api/profiles')

@profiles_bp.route('', methods=['GET'])
@jwt_required()
def list_profiles():
    current_user_id = get_jwt_identity()
    profiles = Profile.query.filter(Profile.user_id != current_user_id).all()
    return jsonify([p.as_dict() for p in profiles]), 200

@profiles_bp.route('', methods=['POST'])
@jwt_required()
def create_profile():
    data = request.get_json() or {}
    p = Profile(
        user_id            = get_jwt_identity(),
        description        = data['description'],
        parish             = data['parish'],
        biography          = data['biography'],
        sex                = data['sex'],
        race               = data['race'],
        birth_year         = data['birth_year'],
        height             = data['height'],
        fav_cuisine        = data.get('fav_cuisine'),
        fav_colour         = data.get('fav_colour'),
        fav_school_subject = data.get('fav_school_subject'),
        political          = data.get('political', False),
        religious          = data.get('religious', False),
        family_oriented    = data.get('family_oriented', False)
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(p.as_dict()), 201

@profiles_bp.route('/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile(profile_id):
    p = Profile.query.get_or_404(profile_id)
    return jsonify(p.as_dict()), 200
