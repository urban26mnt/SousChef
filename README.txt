Name: SousChef

Description: SousChef is an app that helps users save recipes, get shopping lists, nutrition profile, approximate price estimate to make the recipe. This entire bg='#fffddd' runs on python code. There are two main components - the GUI using Tkinter module and a command line interface.

Authors: Chris Bidlake (cbidlake), Jessica DeRyckere (jderycke), Lata Gadoo (lgadoo), Jayasri Puppala (jpuppala), Robert Salerno (rsalerno)

Installation requirements:

The application should be run from this zip file to ensure dependencies are loaded properly:

Program Folder Structure:
SousChef_GUI.py
SousChef_cli.py
kroger.py
nutrition.py
recipes.py
cli.py
/recipes
   recipes.txt
/Kroger
   product_search_results.txt

- The 'Kroger.py' module and the 'SousChef_cli.py' program require 'requests-oauthlib' to be installed in the anaconda environment.
- The package may be installed from the anaconda navigator, environments, searching for 'requests-oauthlib' and applying to the desired environment.

Demonstration Video Link:  https://youtu.be/GB2m1rHF_is

Usage Guide:

- The SousChef app comes with two installed versions, a command line interface version (SousChef_cli) and a GUI version (SousChef_GUI).

GUI: The first page shown on launch accepts a url from recipe websites such as cookinglight.com, allrecipes.com

If the recipe url input by the user already exists, the user sees the response on screen as "Recipe already saved."
If it is a new recipe, the recipe gets added (provided the response code is 200) and displays the message "Recipe added successfully."
If the fetch was unsuccessful, the message displayed is Recipe fetch failed. Status code: {status} with message: {html}"
There is "Next" button and the top right hand corner to navigate to the next page.

Example of URLs that can be input to both GUI and Command line interface:

   These have been preloaded:
    https://www.cookinglight.com/recipes/lentil-salad-with-beets-and-spinach
    https://www.cookinglight.com/recipes/one-pot-pasta-spinach-tomatoes
    https://www.cookinglight.com/recipes/pot-roast-sliders-with-pepperoncini-cabbage-slaw
    https://www.cookinglight.com/recipes/fluffiest-multigrain-pancakes-almond-butter-drizzle
    https://www.foodnetwork.com/recipes/rachael-ray/balsamic-roast-pork-tenderloins-recipe-1951758
    
    These may be added and have been previously tested
    https://www.cookinglight.com/recipes/shirred-eggs-marinara-feta
    https://www.foodnetwork.com/recipes/ree-drummond/stuffed-bell-peppers-3325315
    https://www.foodnetwork.com/recipes/ree-drummond/tater-tot-breakfast-casserole-4607655


The second page of the GUI app, lets the user pick two recipes from dropdown menus at the same time. This page then displays the corresponding shopping lists under each recipe.

There are back and next page button available on this page to navigate to the previous url input page or to the nutrition compare page.

The final page of the app lets you pick two recipes from dropdown menus and this time displays the corresponding nutrition profile of each recipe.
The next page on the top right corner let's the user navigate to the home page which is the url input page.

A quit button is available on all pages to exit the application.

Module Function Descriptions:

Nutrition:
Imported requests, pandas, json, os and receipes module.

The requests module allows you to send HTTP requests using Python. Json module is used to work with json data. os module helps user in interacting with the native OS Python is currently running on. Recipes module is a module written in this project that provides nutrition file, the details of the shopping list needed for the requested recipe.


A call is made to the shopping_list function of the recipe module and result from that function call is stored in the variable called ingredientlist.

A call is made to https://api.nal.usda.gov/fdc/v1/foods/search?query={} to get the nutrition information for the listed ingredients. Then we filter the response to just have the nutrition information for these – 'Protein','Energy','Carbohydrate, by difference','Water', 'Magnesium, Mg','Fiber, total dietary', 'Sugars, total including NLEA', 'Cholesterol','Fatty acids, total saturated', 'Vitamin D (D2 + D3), International Units'

Values returned are rounded to 2 decimal values.



Roadmap/Future upgrades: Future versions of the app can support users creating accounts. Also, the app can be further developed to include specific store information and product availability. 

Support:  (TODO)
