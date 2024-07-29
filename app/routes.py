from flask import request, jsonify, abort
from app import app, db
from app.models import Users
import requests
from datetime import datetime

@app.route('/user/fetch', methods=['GET'])
def fetch_users():
    page = request.args.get('page')
    if not page:
        return jsonify({"error": "Missing query parameter 'page'"}), 400

    response = requests.get(f'https://reqres.in/api/users?page={page}')
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), 500

    data = response.json()
    fetched_users = []
    for user_data in data['data']:
        user = Users.query.get(user_data['id'])
        if not user:
            user = Users(
                id=user_data['id'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                avatar=user_data['avatar'],
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.session.add(user)
            fetched_users.append(user_data)
    db.session.commit()

    return jsonify(fetched_users)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = Users.query.filter_by(id=id, deleted_at=None).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "avatar": user.avatar,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
        "deleted_at": user.deleted_at
    })

@app.route('/user', methods=['GET'])
def get_users():
    users = Users.query.filter_by(deleted_at=None).all()
    return jsonify([{
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "avatar": user.avatar,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
        "deleted_at": user.deleted_at
    } for user in users])

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    user = Users(
        id=data['id'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        avatar=data['avatar'],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

@app.route('/user', methods=['PUT'])
def update_user():
    data = request.get_json()
    id = data.get('id')
    user = Users.query.filter_by(id=id, deleted_at=None).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.email = data.get('email', user.email)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.avatar = data.get('avatar', user.avatar)
    user.updated_at = datetime.now()
    db.session.commit()
    return jsonify({"message": "User updated successfully"})

@app.route('/user', methods=['DELETE'])
def delete_user():
    if request.headers.get('Authorization') != '3cdcnTiBsl':
        abort(403)
    data = request.get_json()
    id = data.get('id')
    user = Users.query.filter_by(id=id, deleted_at=None).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.deleted_at = datetime.now()
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

