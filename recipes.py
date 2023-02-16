"""Recipes.py - Gathers recipes from cooking lite web scrape."""

import requests
import json
import re
import os
import pprint as pp
from bs4 import BeautifulSoup as bs

RECIPE_PATH = 'recipes'
RECIPE_FILE = os.path.join(RECIPE_PATH,'recipes.txt')


def write(recipe):
    my_recipes.append(recipe)
    # Save recipe data to file
    with open(RECIPE_FILE, mode='wt', encoding='utf-8') as f:
        json.dump(my_recipes, f)

    return 'Success'
    
def read():
    # Read recipe data from file if exists
    if os.path.exists(RECIPE_FILE):        
        with open(RECIPE_FILE, mode='rt', encoding='utf-8') as f:
            return json.loads(f.read())
    else:
        return []

def html_to_recipe(html):
    # Initialize recipe
    recipe = {}
    recipe['id'] = len(my_recipes)
    
    # Convert html response to ingredients list
    soup = bs(html, 'html.parser')

    # Save html to backup file for testing / dev
    recipe_name = soup.select(".headline")
    recipe_name = bs.get_text(recipe_name[0])
    recipe_name = re.sub(r'[^\w_. -]', '_', recipe_name)
    with open(f"recipes\{recipe_name}.txt", mode='wt', encoding='utf-8') as f:
        f.write(html)

    recipe['name'] = recipe_name

    # Selection/Cleaning for Cooking Light Domain
    ingredients = soup.select(".ingredients > ul > li")
    ingredients = [bs.get_text(item) for item in ingredients]

    # pattern = re.compile(r"(\d \d/\d|\d/\d|[\d]{1,3}){1}([\S ]*)")
    pattern = re.compile(r"(?P<qty>\d+ \d/\d |\d/\d |\d+ )(?P<unit>\(\d+[-\w\.]*\))?(?P<desc>[\w ]*)")
    
    recipe['ingredients'] = []
    for ingredient in ingredients:
        match = pattern.search(ingredient)
        recipe['ingredients'].append(match.groupdict())
    
    return recipe

def fetch_from_url(url):
    # Fetch recipe from web
    resp = requests.get(url)
    if resp.status_code == 200:
        return (resp.status_code, resp.text)
    else:
        return (resp.status_code, f"Request failed. Status Code: {resp.status_code}. \n\nMessage:\n{resp.text}")

my_recipes = read()
