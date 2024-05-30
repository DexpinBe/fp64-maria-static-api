import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils import APIException
from datastructures import User, UserManagement

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))
CORS(app)

user_management = UserManagement()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_all_users():
    users = user_management.get_all_users()
    nopass_users = [{k: v for k, v in vars(user).items() if k != '_password'} for user in users]
    return jsonify(nopass_users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_management.get_user(user_id)
    if user:
        return jsonify(vars(user))
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if request.form:
            data = request.form
            user = User(data['id'], data['username'], data['email'], data['age'], data['password'])
            user_management.add_user(user)
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "Form data required"}), 400
        
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if request.method == 'PUT':
        data = request.form
        success = user_management.update_user(user_id, data)
        if success:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "User not found"}), 404

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_management.delete_user(user_id):
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
