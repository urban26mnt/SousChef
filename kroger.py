"""Kroger.py - API to get product and location data from Kroger Corp."""

# Imports
import requests
import json
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

headers = {'Accept': 'application/json', 'scope': SCOPE}

# Functions
def get_token():
    """Open connection to Kroger API, remains active for 30 mins."""
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=URL_TOKEN, auth=auth, scope=SCOPE)
    
    # Update header dict for next request and return token
    headers['Authorization'] = 'Bearer ' + token['access_token']

    return token

def get_locations(zip,filter_limit=3):
    """Get nearest Kroger Corp Locations"""   
    url_loc_search =  f"{URL_BASE}locations?filter.zipCode.near={zip}&filter.limit={str(filter_limit)}"

    resp = requests.get(url_loc_search, headers=headers)

    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        print(f"request failed. message: \n\n" + resp.text)

def get_products(location_id, prod_search_term, filter_limit=10):
    """Get top 10 products matching the search term from location"""
    url_prod_search =  f"{URL_BASE}products?filter.locationId={location_id}&filter.term={prod_search_term}&filter.limit={filter_limit}"

    resp = requests.get(url_prod_search, headers=headers)

    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        print(f"request failed. message: \n\n" + resp.text)

# Begin section for automatic tests
if __name__ == "__main__":
    """Tests"""
    # Open Connection
    token = get_token()

    print(headers)

    # Test location search & return
    user_zip = '48009'

    locations = get_locations(user_zip, '3')

    with open('kroger_api_tests_location', mode='wt', encoding='utf-8') as f:
        f.writelines(f"User zip input: {user_zip}\n\n")
        for location in locations['data']:
            f.writelines(f"locationId: {location['locationId']}, chain: {location['chain']}, address: {location['address']}\n\n")

    # Test product search & return
    search_prod = 'milk'
    products = get_products('01800685', search_prod)

    with open('kroger_api_tests_products.txt', mode='wt', encoding='utf-8') as f:
        f.writelines(f"User input search term: {search_prod}\n\n")
        for product in products['data']:
            f.writelines(f"product: {product}\n\n")