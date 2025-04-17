from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user, logout_user
from flask_jwt_extended import create_access_token

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

        if status_code == 200:  
            user_id = response.get('user_id')
            access_token = create_access_token(identity=user_id)  
            return jsonify({
                'message': 'Login successful',
                'access_token': access_token  
            }), 200
        
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    try:
        response, status_code = logout_user()
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
