import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)
    data['bedrooms'] = data['bedrooms'].astype(int)
    data['bathrooms'] = data['bathrooms'].astype(int)
    data['price_per_bedroom'] = data['price'] / data['bedrooms']
    data['price_per_bathroom'] = data['price'] / data['bathrooms']
    data['bed_bath_ratio'] = data['bedrooms'] / data['bathrooms']
    return data

if __name__ == "__main__":
    data = preprocess_data('data/property_data.csv')
    print(data.head())
