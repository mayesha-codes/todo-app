from flask import jsonify, request
from app import app, db
from app.models import User

@app.route("/api/users", methods=["POST"])
def add_users():
    data=request.json
    new_user=User(username=data["username"],email=data["email"],password=data["password"],role=data["role"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"}), 201

