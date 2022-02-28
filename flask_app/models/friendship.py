from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models.user import User

class Friendship():
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def friendship_registration(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        return connectToMySQL('friendship_schema').query_db( query, data )

