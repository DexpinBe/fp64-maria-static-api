
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class User:
    def __init__(self, id, username, email, age, password):
        self.id = id
        self.username = username
        self.email = email
        self.age = age
        self._password = password 

    def check_password(self, password):
        return self._password == password

class UserManagement:
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)
    
    def delete_user(self, user_id):
        for user in self._users:
            if user.id == user_id:
                self._users.remove(user)
                return True
        return False
    
    def get_user(self, user_id):
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def update_user(self, user_id, new_data):
        for user in self._users:
            if user.id == user_id:
                user.username = new_data.get("username", user.username)
                user.email = new_data.get("email", user.email)
                user.password = new_data.get("password", user.password)
                user.age = new_data.get("age", user.age)
                return True
        return False
    
    def get_all_users(self):
        return self._users

