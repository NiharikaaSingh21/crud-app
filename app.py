from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
USERS_FILE = "users.json"

# Helper functions
def load_users():
    """Load users from JSON file."""
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    """Save users to JSON file."""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# GET: Fetch all users
@app.route("/users", methods=["GET"])
def get_users():
    users = load_users()
    return jsonify(users), 200


# GET: Fetch single user by ID
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    users = load_users()
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

# POST: Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    users = load_users()
    data = request.get_json()
    
    if not data or "id" not in data:
        return jsonify({"error": "User ID required"}), 400
    
    user_id = str(data["id"])
    
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {
        "name": data.get("name", ""),
        "email": data.get("email", "")
    }

    save_users(users)
    return jsonify({"message": "User created"}), 201

# PUT: Update user information

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    users = load_users()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "email": data.get("email", users[user_id]["email"])
    })

    save_users(users)
    return jsonify({"message": "User updated"}), 200

# Delete user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = load_users()
    if user_id in users:
        del users[user_id]
        save_users(users)
        return jsonify({"message": "User deleted"}), 200
    
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
