from flask import Blueprint, request, jsonify
from .services import register_user, login_user, logout_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        response, status_code = register_user(data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        response, status_code = login_user(data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
