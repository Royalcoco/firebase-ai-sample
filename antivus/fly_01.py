from flask import Flask, request, jsonify
import hashlib
import time
from pymongo import MongoClient
from flask_pymongo import PyMongo
import pyotp

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/crypto"
mongo = PyMongo(app)
users = mongo.db.users

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(user, password):
    user_data = users.find_one({"username": user})
    return user_data and user_data["password_hash"] == hash_password(password)

def verify_2fa_code(user, code):
    user_data = users.find_one({"username": user})
    totp = pyotp.TOTP(user_data["2fa_secret"])
    return totp.verify(code)

def verify_ping_time(user, ping_time):
    user_data = users.find_one({"username": user})
    return abs(user_data["ping_time"] - ping_time) < 10  # Allow 10ms deviation

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]
    ping_time = data["ping_time"]

    if users.find_one({"username": username}):
        return jsonify({"status": "error", "message": "User already exists"}), 400

    users.insert_one({
        "username": username,
        "password_hash": hash_password(password),
        "2fa_secret": pyotp.random_base32(),
        "ping_time": ping_time
    })
    return jsonify({"status": "success", "message": "User registered"})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    user = data["user"]
    password = data["password"]
    code = data["2fa_code"]
    ping_time = data["ping_time"]

    if verify_password(user, password) and verify_2fa_code(user, code) and verify_ping_time(user, ping_time):
        # Process withdrawal
        return jsonify({"status": "success", "message": "Withdrawal processed"})
    else:
        return jsonify({"status": "error", "message": "Authentication failed"}), 403

if __name__ == '__main__':
    app.run(port=5000)
