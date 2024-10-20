"""
This is your server - Flask goes here
"""
from flask import Flask, jsonify, request
from db_utils import get_all_cards_db, delete_card_by_id, add_new_card_db

app = Flask(__name__)

@app.route("/cards", methods=["GET"])
def get_all_cards():
    return jsonify(get_all_cards_db())

@app.route("/cards/add", methods=["POST"])
def add_new_card():
    new_card_dict = request.get_json()
    return jsonify(add_new_card_db(new_card_dict))

@app.route("/cards/remove/<int:card_id>", methods=["DELETE"])
def del_card_by_id(card_id):
    return jsonify(delete_card_by_id(card_id))

if __name__ == "__main__":
    app.run(debug=True)
