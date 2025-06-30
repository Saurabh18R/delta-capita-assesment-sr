from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client.get_database("clientsdb")

@app.route("/")
def index():
    return jsonify({"message": "Clients API is running"})

@app.route("/clients")
def get_clients():
    clients = list(db.clients.find({}, {"_id": 0}))
    return jsonify(clients)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
