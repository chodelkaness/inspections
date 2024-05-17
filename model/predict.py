import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load('model/property_rating_model.pkl')

def predict(features):
    return model.predict([features])

# Example usage
if __name__ == "__main__":
    # Example feature set
    example_features = [750000, 3, 2, 250000, 375000, 1.5]
    prediction = predict(example_features)
    print(f"Predicted Rating: {prediction[0]}")
