# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:57:36 2023

@author: PZZNVD
"""
import requests
import pandas as pd
import json
import os
import recipes

# =============================================================================
# https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=TqLg4D5JEEcbnbNHDpjezbaaPZm81eL3Vjtgp5a3
# =============================================================================
# =============================================================================
# api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
# =============================================================================

def fetch_nutrition(ingredientlist):
    nutrition_d = {}
    for i in ingredientlist:
        api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query={}'.format(i)
        response = requests.get(api_url, headers={'X-Api-Key': 'TqLg4D5JEEcbnbNHDpjezbaaPZm81eL3Vjtgp5a3'})
        if response.status_code == requests.codes.ok:
            d = json.loads(response.text)
            
            for nut in d['foods'][0]['foodNutrients']:
                if nut['nutrientName'] in nutrition_d:
                    nutrition_d[nut['nutrientName']] += nut['value']
                else:
                    nutrition_d[nut['nutrientName']] = nut['value']

        else:
            print("Error:", response.status_code, response.text)

    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    wanted_keys = ('Protein','Energy','Carbohydrate, by difference','Water', 'Magnesium, Mg','Fiber, total dietary', 'Sugars, total including NLEA', 'Cholesterol','Fatty acids, total saturated', 'Vitamin D (D2 + D3), International Units')
    filtered_nutrition_d = dictfilt(nutrition_d, wanted_keys)

    return filtered_nutrition_d

if __name__ == "__main__":
    # test_name = 'Lentil Salad With Beets and Spinach'
    test_url = 'https://www.cookinglight.com/recipes/lentil-salad-with-beets-and-spinach'

    # recipe_id = recipes.recipe_id_from_name(test_name)
    recipe_id = recipes.recipe_id_from_url(test_url)

    shopping_list = recipes.shopping_list(recipe_id)

    nutrition_result = fetch_nutrition(shopping_list)
    NutritionSeries = round(pd.Series(nutrition_result),2)
    s = pd.DataFrame(pd.Series(nutrition_result)).T 
    print(NutritionSeries)
