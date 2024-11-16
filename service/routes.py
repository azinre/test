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
    Product(3, "Product 3", "Category A", True),
    Product(4, "Product 4", "Category C", True),
    Product(5, "Product 5", "Category B", False),
]

# READ function: Get a product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.serialize()), 200

# UPDATE function: Update a product by ID
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

# DELETE function: Delete a product by ID
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    return jsonify({"message": "Product deleted"}), 200

# LIST ALL / LIST BY NAME / LIST BY CATEGORY / LIST BY AVAILABILITY function
@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get('name')
    category = request.args.get('category')
    available = request.args.get('available')

    filtered_products = products

    if name:
        filtered_products = [p for p in filtered_products if name.lower() in p.name.lower()]
    if category:
        filtered_products = [p for p in filtered_products if category.lower() in p.category.lower()]
    if available is not None:
        available = available.lower() == 'true'
        filtered_products = [p for p in filtered_products if p.available == available]

    return jsonify([p.serialize() for p in filtered_products]), 200

if __name__ == "__main__":
    app.run(debug=True)
