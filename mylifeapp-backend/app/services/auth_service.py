from app.repositories.auth_repositorie import create_user, get_user_by_username, get_user_by_email
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, set_access_cookies

def register_user(data):
    if not data.get('username') or not data.get('password') or not data.get('email'):
        return {'error': 'Missing username, email, or password'}, 400

    if get_user_by_username(data['username']) or get_user_by_email(data['email']):
        return {'error': 'User or email already exists'}, 409

    create_user(data['username'], data['email'], data['password'])
    return {'message': 'User created successfully'}, 201

def login_user(data):
    if not data.get('email') or not data.get('password'):
        return {'error': 'Missing email or password'}, 400

    user = get_user_by_email(data['email'])

    if user and user.check_password(data['password']):
        return {'message': 'Login successful', 'user_id': user.id}, 200  
    else:
        return {'error': 'Invalid credentials'}, 401



def logout_user():
    # Si usas JWT, puedes "revocar" el token o simplemente esperar que caduque.
    # No es necesario hacer nada explícitamente si el token tiene una caducidad predefinida.
    return {'message': 'Logout successful'}, 200
