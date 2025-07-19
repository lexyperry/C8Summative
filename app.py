from flask import Flask, jsonify, request
from database import get_all_items, get_item_by_id,add_item, update_item, delete_id
import uuid 
from API import fetch_product_details

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def fetch_all():
    return jsonify(get_all_items()), 200

@app.route('/inventory/<id>', methods=['GET'])
def fetch_one(id):
    item = get_item_by_id(id)
    if item: 
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route('/inventory', methods=['POST'])
def create_item():
    data = request.get_json()
    barcode = data["barcode"]
    product_info = {}
    if barcode: 
        product_info = fetch_product_details(barcode) or {}
    
    print(product_info)
    item = {
        "id": str(uuid.uuid4()),
        "name": product_info.get("product_name", data["name"]),
        "brands": product_info.get("brands", ""),
        "ingredients": product_info.get("ingredients", ""),
        "stock": data["stock"],
        "price": data["price"],
        "barcode": barcode

    }
    add_item(item)
    return jsonify(item), 201

@app.route('/inventory/<id>', methods=['PATCH'])
def update(id):
    data = request.get_json()
    updated = update_item(id, data)
    if updated: 
        return jsonify(updated), 200
    return jsonify({"error": "Item not found"}), 404

@app.route('/inventory/<id>', methods=['DELETE'])
def delete(id):
    delete_id(id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)

