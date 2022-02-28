from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.friendship import Friendship

class User():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friendship = []

    @classmethod
    def user_registration(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('friendship_schema').query_db( query, data )

    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendship_schema').query_db( query)
        users = []

        for user in results:
            users.append(User(user))
        return users

    @classmethod
    def all_friendships(cls):
        query = "SELECT * FROM users JOIN friendships ON users.id = friendships.user_id JOIN users AS U ON friendships.friend_id = U.id;"
        results = connectToMySQL('friendship_schema').query_db( query)

        friendships = {}
        for result in results:
            mainuser = cls(result)
            data = {
                'id': result['U.id'],
                'first_name': result['U.first_name'],
                'last_name': result['U.last_name'],
                'created_at': result['U.created_at'],
                'updated_at': result['U.updated_at']
                # 'dojo_id': result['dojo_id']
            }
            mainuserfriend = cls(data)
            friendships[mainuser] = mainuserfriend
        return friendships

