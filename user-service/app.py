from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "Jane Doe", "email": "jane@example.com"}
}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = user_data
    return jsonify({"id": user_id}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
