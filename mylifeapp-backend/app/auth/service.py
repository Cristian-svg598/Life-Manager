from .repositories import create_user, get_user_by_username, get_user_by_email

def register_user(data):
    if not data.get('username') or not data.get('password') or not data.get('email'):
        return {'error': 'Missing username, email, or password'}, 400

    if get_user_by_username(data['username']) or get_user_by_email(data['email']):
        return {'error': 'User or email already exists'}, 409

    create_user(data['username'], data['email'], data['password'])
    return {'message': 'User created successfully'}, 201

def login_user(data):
    if not data.get('username') or not data.get('password'):
        return {'error': 'Missing username or password'}, 400

    user = get_user_by_username(data['username'])

    if user and user.check_password(data['password']):
        return {'message': 'Login successful'}, 200
    else:
        return {'error': 'Invalid credentials'}, 401
