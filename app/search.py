# app/search.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import or_
from .models import Profile, User

search_bp = Blueprint('search', __name__, url_prefix='/api/search')

@search_bp.route('', methods=['GET'])
@jwt_required()
def search_profiles():
    me = get_jwt_identity()
    q  = Profile.query.filter(Profile.user_id!=me)
    name = request.args.get('name')
    if name:
        q = q.join(User).filter(or_(
            User.name.ilike(f"%{name}%"),
            Profile.description.ilike(f"%{name}%")
        ))
    for param in ('race','sex','parish'):
        v = request.args.get(param)
        if v:
            q = q.filter(getattr(Profile, param).ilike(f"%{v}%"))
    by = request.args.get('birth_year')
    if by and by.isdigit():
        q = q.filter(Profile.birth_year==int(by))
    return jsonify([p.as_dict() for p in q.all()]), 200
