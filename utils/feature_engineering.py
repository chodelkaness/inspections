import pandas as pd

def create_features(data):
    data['price_per_bedroom'] = data['price'] / data['bedrooms']
    data['price_per_bathroom'] = data['price'] / data['bathrooms']
    data['bed_bath_ratio'] = data['bedrooms'] / data['bathrooms']
    return data

if __name__ == "__main__":
    data = pd.read_csv('data/property_data.csv')
    data = create_features(data)
    print(data.head())
