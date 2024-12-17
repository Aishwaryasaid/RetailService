from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

products = {
    1: {"name": "Product 1", "price": 100},
    2: {"name": "Product 2", "price": 150}
}

USER_SERVICE_URL = "http://user-service:5001/users"

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route("/products", methods=["POST"])
def create_product():
    product_data = request.get_json()
    product_id = len(products) + 1
    products[product_id] = product_data
    return jsonify({"id": product_id}), 201

@app.route("/products/<int:product_id>/user", methods=["GET"])
def get_product_user(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Get random user data from the User Service
    response = requests.get(f"{USER_SERVICE_URL}/{product_id}")
    if response.status_code == 200:
        user_data = response.json()
        return jsonify({"product": product, "user": user_data})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
