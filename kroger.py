"""Kroger.py - API to get product and location data from Kroger Corp."""

# Imports
import requests
import json
import os
from statistics import mean
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

# Constants
CLIENT_ID="cmutestapi-e5afe051aeaf7cd9e472787c6e66fc9b2906097967775590152"
CLIENT_SECRET="sA8Y6DK90_P-Hnsusg4UzkPiuHlF4yzOhmX2V61q"
URL_BASE = "https://api-ce.kroger.com/v1/"
URL_AUTHORIZE = URL_BASE + "connect/oauth2/authorize"
URL_TOKEN = URL_BASE + "connect/oauth2/token"
SCOPE = "product.compact"

KROGER_PATH = 'kroger'
KROGER_SEARCH_FILE = os.path.join(KROGER_PATH,'product_search_results.txt')

def read_search_data():
    if os.path.exists(KROGER_SEARCH_FILE): 
        with open(KROGER_SEARCH_FILE, mode='rt', encoding='utf-8') as f:
            return json.loads(f.read())
    else:
        return {}

def write_search_data():
    with open(KROGER_SEARCH_FILE, mode='wt', encoding='utf-8') as f:
        json.dump(my_searches, f)

def clean_product_data(product):
    if 'images' in product.keys():
        product.pop('images')

    return product

def get_products(location_id, prod_search_term, filter_limit=10):
    """Get top 10 products matching the search term from location"""
    url_prod_search =  f"{URL_BASE}products?filter.locationId={location_id}&filter.term={prod_search_term}&filter.limit={filter_limit}"

    resp = requests.get(url_prod_search, headers=headers)

    if resp.status_code == 200:
        prod_data = json.loads(resp.text)
        products = []
        for product in prod_data['data']:
            cleaned_product = clean_product_data(product)
            products.append(cleaned_product)
        
        return products
    else:
        print(f"request failed. message: \n\n" + resp.text)


def shopping_list_search(shopping_list):
    for item in shopping_list:
        if item not in my_searches:
            products = get_products(location_id=location_id, prod_search_term=item, filter_limit=20)
            my_searches[item] = products

            write_search_data()

def pricing_estimate(search_term):
    if search_term not in my_searches.keys():
        return 'Error: search term not loaded yet.'
    
    results = my_searches[search_term]
    prices = []
    for result in results:
        if 'price' in result['items'][0].keys():
            prices.append(result['items'][0]['price']['regular'])
    
    if len(prices) > 0:
        return mean(prices)
    else:
        return 0
    
def shopping_list_price(shopping_list):
    pricing = []
    for item in shopping_list:
        if item in my_searches.keys():
            pricing.append(pricing_estimate(item))
        else:
            products = get_products(location_id=location_id, prod_search_term=item, filter_limit=20)
            my_searches[item] = products
            write_search_data
            
            pricing.append(pricing_estimate(item))

    return sum(pricing)

def get_locations(zip=48009,filter_limit=3):
    """Get nearest Kroger Corp Locations"""   
    url_loc_search =  f"{URL_BASE}locations?filter.zipCode.near={zip}&filter.limit={str(filter_limit)}"

    resp = requests.get(url_loc_search, headers=headers)

    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        print(f"request failed. message: \n\n" + resp.text)


"""Open connection to Kroger API, remains active for 30 mins."""
auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
client = BackendApplicationClient(client_id=CLIENT_ID)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=URL_TOKEN, auth=auth, scope=SCOPE)

# Update header dict for next request and return token
headers = {'Accept': 'application/json', 'scope': SCOPE}
headers['Authorization'] = 'Bearer ' + token['access_token']

location_id = ''
locations = get_locations()
location_id = locations['data'][0]['locationId']

my_searches = read_search_data()
    

# Begin section for automatic tests
# if __name__ == "__main__":
#     """Tests"""
#     # Open Connection
#     token = get_token()

#     print(headers)

#     # Test location search & return
#     user_zip = '48009'

#     locations = get_locations(user_zip, '3')

#     with open('kroger_api_tests_location', mode='wt', encoding='utf-8') as f:
#         f.writelines(f"User zip input: {user_zip}\n\n")
#         for location in locations['data']:
#             f.writelines(f"locationId: {location['locationId']}, chain: {location['chain']}, address: {location['address']}\n\n")

#     # Test product search & return
#     search_prod = 'milk'
#     products = get_products('01800685', search_prod)

#     with open('kroger_api_tests_products.txt', mode='wt', encoding='utf-8') as f:
#         f.writelines(f"User input search term: {search_prod}\n\n")
#         for product in products['data']:
#             f.writelines(f"product: {product}\n\n")