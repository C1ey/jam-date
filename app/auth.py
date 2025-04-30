from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    if not data.get('username') or not data.get('password'):
        return jsonify(msg='Username and password required'), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify(msg='Username already exists'), 409

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(msg='User created'), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.check_password(data.get('password', '')):
        return jsonify(msg='Bad credentials'), 401

    token = create_access_token(identity=str(user.id))
    return jsonify(access_token=token), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify(msg='Logged out'), 200