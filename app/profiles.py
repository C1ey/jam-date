# app/profiles.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import db
from .models import Profile, Favourite

profiles_bp = Blueprint('profiles', __name__, url_prefix='/api/profiles')

@profiles_bp.route('', methods=['GET'])
@jwt_required()
def list_profiles():
    me = get_jwt_identity()
    profiles = Profile.query.filter(Profile.user_id != me).all()
    return jsonify([p.as_dict() for p in profiles]), 200

@profiles_bp.route('', methods=['POST'])
@jwt_required()
def create_profile():
    data = request.get_json() or {}
    me = get_jwt_identity()
    p = Profile(
        user_id            = me,
        description        = data['description'],
        parish             = data['parish'],
        biography          = data['biography'],
        sex                = data['sex'],
        race               = data['race'],
        birth_year         = data['birth_year'],
        height             = data['height'],
        photo              = data.get('photo'),
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

@profiles_bp.route('/<int:profile_id>/favourite', methods=['POST'])
@jwt_required()
def favourite_profile(profile_id):
    me = get_jwt_identity()
    # ensure profile exists
    Profile.query.get_or_404(profile_id)
    fav = Favourite(user_id=me, fav_profile_id=profile_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.as_dict()), 201

@profiles_bp.route('/matches/<int:profile_id>', methods=['GET'])
@jwt_required()
def match_profiles(profile_id):
    me = get_jwt_identity()
    mine = Profile.query.get_or_404(profile_id)

    candidates = Profile.query.filter(
        Profile.user_id != me,
        Profile.id != profile_id,
        Profile.birth_year.between(mine.birth_year - 5, mine.birth_year + 5),
        Profile.height.between(mine.height - 10, mine.height + 10)
    ).all()

    matches = []
    for c in candidates:
        score = sum([
            c.fav_cuisine        == mine.fav_cuisine,
            c.fav_colour         == mine.fav_colour,
            c.fav_school_subject == mine.fav_school_subject,
            c.political          == mine.political,
            c.religious          == mine.religious,
            c.family_oriented    == mine.family_oriented
        ])
        if score >= 3:
            matches.append(c.as_dict())

    return jsonify(matches), 200
