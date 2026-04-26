#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route("/")
def home():
    """Root endpoint with a welcome message."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary via POST request."""
    # Check if request is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Validation: Username required
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Validation: Duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to memory
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
