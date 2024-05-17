from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from pymilvus import Collection, connections

app = Flask(__name__)

# Load the model
model = joblib.load('model/property_rating_model.pkl')

# Connect to Milvus
connections.connect("default", host="127.0.0.1", port="19530")
collection = Collection("property_embeddings")
collection.load()

# Load sentence transformer
sentence_transformer = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

@app.route('/similar', methods=['POST'])
def find_similar_properties():
    data = request.json
    property_features = data['features']
    query_embedding = sentence_transformer.encode([property_features])
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search(query_embedding, "embedding", search_params, limit=5, output_fields=["property_id"])
    similar_properties = [hit.entity.property_id for hit in results[0]]
    return jsonify({'similar_properties': similar_properties})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
