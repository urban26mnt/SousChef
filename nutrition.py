# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:57:36 2023

@author: PZZNVD
"""
import requests
import pandas as pd
import json
import os

ingredientlist = ['sherry vinegar',
'Dijon mustard',
'black pepper',
'olive oil']

ingredientlist1 = ['sherry vinegar',
'Dijon mustard',
'black pepper',
'olive oil',
'precooked lentils',
'Golden Beet',
'baby spinach',
'walnuts',
'Cotija cheese']

ingredientlist2 = ['olive oil',
'onion',
'garlic cloves',
'tomatoes',
'chicken stock',
'dried oregano',
'spaghetti',
'salt',
'spinach',
'Parmesan cheese']

query = 'Parmesan cheese'
# =============================================================================
# https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=TqLg4D5JEEcbnbNHDpjezbaaPZm81eL3Vjtgp5a3
# =============================================================================
# =============================================================================
# api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
# =============================================================================
nutrition_d = {}
for i in ingredientlist2:
    api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query={}'.format(i)
    response = requests.get(api_url, headers={'X-Api-Key': 'TqLg4D5JEEcbnbNHDpjezbaaPZm81eL3Vjtgp5a3'})
    if response.status_code == requests.codes.ok:
        d = json.loads(response.text)
        
        for nut in d['foods'][0]['foodNutrients']:
            if nut['nutrientName'] in nutrition_d:
                nutrition_d[nut['nutrientName']] += nut['value']
            else:
                nutrition_d[nut['nutrientName']] = nut['value']
            
    # =============================================================================
    #     print(nut['nutrientName'].split(',')[0])
    # =============================================================================
        
# =============================================================================
#         for nut in d['foods'][0]['foodNutrients']:
#             keylist = []
#             keylist.append(nut['nutrientName'])
#             valuelist = []
#             valuelist.append(nut['value'])    
# =============================================================================
            
    else:
        print("Error:", response.status_code, response.text)
# =============================================================================
#     nutrition = dict(zip(keylist, valuelist)) 
# =============================================================================
    
#apikey = 'TqLg4D5JEEcbnbNHDpjezbaaPZm81eL3Vjtgp5a3'

# =============================================================================
# print(f'Energy: {response.json().get("Energy")}')
# =============================================================================
# =============================================================================
# cwd = os.getcwd()
# out_file = cwd + "/resp.txt"
# p1 = open(out_file, 'w')  
# p1.write(response.text)
# =============================================================================


# =============================================================================
# d = json.loads(response.text)
# 
# keylist = []
# for nut in d['foods'][0]['foodNutrients']:
#     keylist.append(nut['nutrientName'])
# # =============================================================================
# #     print(nut['nutrientName'].split(',')[0])
# # =============================================================================
# valuelist = []
# for nut in d['foods'][0]['foodNutrients']:
#     valuelist.append(nut['value'])
#     
# nutrition_d = dict(zip(keylist, valuelist)) 
# =============================================================================
print(nutrition_d)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#s = pd.DataFrame([nutrition_d])
NutritionSeries = pd.Series(nutrition_d)
s = pd.DataFrame(pd.Series(nutrition_d)).T 
print(NutritionSeries)
# =============================================================================
# cwd = os.getcwd()
# out_file = cwd + "/nutrition_data.csv"
# p1 = open(out_file, 'w')  
# p1.write(pd.DataFrame.to_csv(s))
# =============================================================================
