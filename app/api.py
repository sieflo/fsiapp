from app import app
from app.models import User, Post
from flask import jsonify


@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    data = user.to_dict()
    return jsonify(data)

@app.route('/api/users', methods=['GET'])
def get_users():
    data = User.to_collection()
    return jsonify(data)

@app.route('/api/users/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass

@app.route('/api/users/<int:id>/followed', methods=['GET'])
def get_followed(id):
    pass

@app.route('/api/users/<int:id>/posts', methods=['GET'])
def get_posts(id):
    pass