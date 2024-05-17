import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load and preprocess data
data = pd.read_csv('data/property_data.csv')
data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)
data['bedrooms'] = data['bedrooms'].astype(int)
data['bathrooms'] = data['bathrooms'].astype(int)

# Feature Engineering
data['price_per_bedroom'] = data['price'] / data['bedrooms']
data['price_per_bathroom'] = data['price'] / data['bathrooms']
data['bed_bath_ratio'] = data['bedrooms'] / data['bathrooms']

# Extract features and target
features = data[['price', 'bedrooms', 'bathrooms', 'price_per_bedroom', 'price_per_bathroom', 'bed_bath_ratio']]
target = data['overall_rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Define the model and hyperparameters
model = GradientBoostingRegressor()

param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5]
}

# Use Grid Search for hyperparameter tuning
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_absolute_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Evaluate model
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
print(f"R-squared: {r2}")

# Save the model
joblib.dump(best_model, 'model/property_rating_model.pkl')
