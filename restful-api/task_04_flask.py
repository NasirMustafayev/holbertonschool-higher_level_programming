#!/usr/bin/python3
"""Flask API with multiple routes and error handling"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    usernames = []
    for key, user in users.items():
        usernames.append(user["username"])

    return jsonify(usernames)


@app.route("/status")
def get_status():
    return jsonify({"status": "OK"})


@app.route("/users/<username>")
def get_userdata(username):
    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "username is required"}), 400
    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = data
    return jsonify(data), 201


if __name__ == "__main__":
    app.run()
