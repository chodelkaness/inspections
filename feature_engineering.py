import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load and preprocess data
data = pd.read_csv('property_data.csv')
data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)
data['bedrooms'] = data['bedrooms'].astype(int)
data['bathrooms'] = data['bathrooms'].astype(int)

# Feature engineering
features = data[['price', 'bedrooms', 'bathrooms']]
target = data['overall_rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Save model
import joblib
joblib.dump(model, 'property_rating_model.pkl')
