from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return jsonify(message='This is the beginning of our API'), 200

@main_bp.app_errorhandler(404)
def handle_404(e):
    return jsonify(error='Not found'), 404