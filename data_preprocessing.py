import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(filename='scraping.log', level=logging.INFO)

# Function to scrape property data with error handling
def scrape_property_data(address):
    try:
        search_url = f"https://www.realestate.com.au/rent/in-{address.replace(' ', '+').replace(',', '%2C').lower()}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('span', {'class': 'property-price'}).text.strip()
        bedrooms = soup.find('span', {'class': 'general-features__beds'}).text.strip()
        bathrooms = soup.find('span', {'class': 'general-features__baths'}).text.strip()
        inspection_times = [time.text.strip() for time in soup.find_all('span', {'class': 'inspection-time'})]
        return {'address': address, 'price': price, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'inspection_times': inspection_times}
    except Exception as e:
        logging.error(f"Error scraping {address}: {e}")
        return None

# Data collection loop
addresses = [
    "1/1701 Centre Road, Oakleigh South",
    "8 Hewitts Road, Carnegie",
    "5 Fairview Road, Mount Waverley",
    "1634 Dandenong Road, Huntingdale",
    "89 Power Avenue, Chadstone",
    "9 Roy St, Oakleigh East",
    "2/8 Mimosa Avenue, Oakleigh South",
    "27 Palm Beach Crescent, Mount Waverley"
]

property_data = [scrape_property_data(address) for address in addresses if scrape_property_data(address) is not None]
property_df = pd.DataFrame(property_data)
property_df.to_csv('property_data.csv', index=False)
