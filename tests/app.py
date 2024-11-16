from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Mock Product model (replace with actual ORM model)
class Product:
    def __init__(self, id, name, category, available):
        self.id = id
        self.name = name
        self.category = category
        self.available = available

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "available": self.available,
        }

# Example in-memory data
products = [
    Product(1, "Product 1", "Category A", True),
    Product(2, "Product 2", "Category B", False),
]

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.json
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.available = data.get("available", product.available)
    return jsonify(product.serialize()), 200

if __name__ == "__main__":
    app.run(debug=True)
