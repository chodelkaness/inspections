import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('property_rating_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
