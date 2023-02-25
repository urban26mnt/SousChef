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
    
def read():
    # Read recipe data from file if exists
    if os.path.exists(RECIPE_FILE):        
        with open(RECIPE_FILE, mode='rt', encoding='utf-8') as f:
            return json.loads(f.read())
    else:
        return []

def html_to_recipe(html, source_url):
    # Initialize recipe
    recipe = {}
    recipe['id'] = len(my_recipes)
    
    # Convert html response to ingredients list
    soup = bs(html, 'html.parser')

    # Split code based on domain:
    title = soup.title.string

    # Get recipe name
    if 'Cooking Light' in title:
        recipe_name = soup.select(".headline") 
        recipe['source'] = 'Cooking Light'
    elif 'Food Network' in title:
        recipe_name = soup.select(".o-AssetTitle__a-HeadlineText")
        recipe['source'] = 'Food Network'

    recipe_name = bs.get_text(recipe_name[0])
    recipe_name = re.sub(r'[^\w_. -]', '_', recipe_name)

    recipe['name'] = recipe_name
    recipe['url'] = source_url

    # Selection/Cleaning
    if 'Cooking Light' in title:
        ingredients = soup.select(".ingredients > ul > li")
        ingredients = [bs.get_text(item) for item in ingredients]
    elif 'Food Network' in title:
        ingredients = soup.find_all(class_='o-Ingredients__a-Ingredient')
        ingredients = [bs.get_text(item).strip() for item in ingredients]
        ingredients = ingredients[1:]

    # Clean ingredients
    pattern = re.compile(r"(?P<qty>\d+ \d/\d |\d/\d |\d+ )(?P<unit>\(\d+[-\w\.]*\))?(?P<desc>[\w ]*)")
    unit_words = {'cups':'cup','cup':'cup',
              'tablespoons':'tablespoon', 'tablespoon':'tablespoon',
              'teaspoons':'teaspoon', 'teaspoon':'teaspoon',
              'sprigs':'sprig', 'sprig':'sprig',
              'pounds':'pound', 'pound':'pound',
              'ounces':'ounce', 'ounce':'ounce'}
    
    recipe['ingredients'] = []
    for ingredient in ingredients:
        match = pattern.search(ingredient)
        if match != None:
            item = match.group(0)
            qty = match.group(1)
            unit = match.group(2)
            desc = match.group(3).strip()

            for word in unit_words.keys():
                if word in desc:
                    desc = re.sub(pattern=word, repl="", string=desc).strip()
                    if unit == None:
                        unit = word


            recipe['ingredients'].append({'item':item, 'qty':qty, 'unit':unit, 'desc':desc})
        else:
            recipe['ingredients'].append({'item':ingredient, 'qty':None, 'unit':None, 'desc':ingredient})

    # Save html to backup file for testing / dev
    # with open(f"recipes\{recipe_name}.txt", mode='wt', encoding='utf-8') as f:
    #     f.write(html)

    # write recipe to my_recipes
    write(recipe)
    
    return recipe

def fetch_from_url(url):
    # Fetch recipe from web
    resp = requests.get(url)
    if resp.status_code == 200:
        return (resp.status_code, resp.text)
    else:
        return (resp.status_code, f"Request failed. Status Code: {resp.status_code}. \n\nMessage:\n{resp.text}")

def shopping_list(recipe_id):
    shopping_list = []
    for ingredient in my_recipes[recipe_id]['ingredients']:
        shopping_list.append(ingredient['desc'])
    
    return shopping_list

def recipe_list():
    recipe_list = []
    for recipe in my_recipes:
        recipe_list.append(f"{recipe['id']}: {recipe['name']}")
    
    return recipe_list

def recipe_id_from_url(url):
    recipe_id = None
    for recipe in my_recipes:
        if url == recipe['url']:
            recipe_id = recipe['id']
    
    return recipe_id

def recipe_id_from_name(name):
    recipe_id = None
    for recipe in my_recipes:
        if name == recipe['name']:
            recipe_id = recipe['id']

    return recipe_id

my_recipes = read()
