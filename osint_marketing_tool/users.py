from flask import Blueprint, request, jsonify
from functools import wraps

users_bp = Blueprint('users', __name__)

# Dummy data for users and roles
users = {}
roles = {}

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Implement authentication logic here
        return f(*args, **kwargs)
    return decorated

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    users[username] = {'password': password, 'role': role}
    return jsonify({'message': 'User registered successfully'}), 201

@users_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and user['password'] == password:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@users_bp.route('/roles', methods=['GET'])
@requires_auth
def get_roles():
    return jsonify(roles), 200

@users_bp.route('/roles', methods=['POST'])
@requires_auth
def add_role():
    data = request.json
    role_name = data.get('role_name')

    if role_name in roles:
        return jsonify({'message': 'Role already exists'}), 400

    roles[role_name] = []
    return jsonify({'message': 'Role added successfully'}), 201

@users_bp.route('/assign_role', methods=['POST'])
@requires_auth
def assign_role():
    data = request.json
    username = data.get('username')
    role_name = data.get('role_name')

    if username not in users:
        return jsonify({'message': 'User does not exist'}), 404

    if role_name not in roles:
        return jsonify({'message': 'Role does not exist'}), 404

    roles[role_name].append(username)
    return jsonify({'message': 'Role assigned successfully'}), 200

@users_bp.route('/users', methods=['GET'])
@requires_auth
def list_users():
    return jsonify(users), 200