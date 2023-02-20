"""SousChef.py - Get Recipes, FDA Nutrition, and Kroger Corp Pricing"""

# Dependencies
import recipes
import kroger
import cli
import tkinter as tk

def show_recipes():
    global state

    display_data = []
    if len(recipes.my_recipes) == 0:
        display_data = ['no recipes saved.']
    for recipe in recipes.my_recipes:
        display_data.append(f"{recipe['id']}: {recipe['name']}")
    
    if state[0] != 'SHOW_RCP':
        state.insert(0, "SHOW_RCP")    

    return display_data

def recipe_detail(rcp_id):
    
    # Check rcp_id in recipes
    rcp_data = recipes.my_recipes[rcp_id]

    display_data = [f"Recipe:  {rcp_data['name']}"]
    display_data.append('\nIngredients:\n')
    # display_data.append(f"{0:8s}{1:8s}{2:40s}")
    display_data.append(f"Qty:     Unit:    Ingredient:")
    # for ingredient in rcp_data['ingredients']:
        # display_data.append(ingredient['qty'])
    for ingredient in rcp_data['ingredients']:
        if ingredient['unit'] is None:
            unit = ""
        else:
            unit = ingredient['unit']
        
        display_data.append(f"{ingredient['qty']:9s}{unit:9s}{ingredient['desc']:40s}")
    
    return display_data
    
def add_recipe():

    user_input = cli.get_url()

    if user_input == '-c' or user_input == '--cancel':
        state[0] = 'MAIN'
        return []
    
    # TODO Error check URL.

    status, html = recipes.fetch_from_url(user_input)

    if status==200:
        recipe = recipes.html_to_recipe(html)
    else:
        print(f'Unable to reach site:\n\n Response{status}\nMessage:  {html}')
    
    recipes.write(recipe)

def back():
    global display_data, prior_display
    state.pop(0)
    display_data = prior_display

# Commands configuration
cmds ={}
cmds['func_call'] = {
    '--add':add_recipe,
    '-a': add_recipe,
    '--show': show_recipes,
    '-s': show_recipes,
    '-b': back,
    '--back': back,
    '-e': exit,
    '--exit': exit}

cmds['disp_main'] = {'-s --show': 'Show my loaded recipes', '-a --add': 'Add a new recipe from a URL', '-e --exit': 'Exit the application'}
cmds['disp_recp'] = {'-b --back': 'Go back', '##': 'Recipe Details'}

# State control variables
display_data = []
prior_display = []
bad_cmd=False
state = ["MAIN"]

# Program Loop
while True:
    if state[0] == "MAIN":
        display_data=[]
        cmd_set = cmds['disp_main']
    elif state[0] == "SHOW_RCP":
        cmd_set = cmds['disp_recp']

    user_input = cli.draw(display_data=display_data, show_cmds=cmd_set, bad_cmd=bad_cmd, state=state)
    bad_cmd = False
    prior_display = display_data

    if user_input in cmds['func_call'].keys():
        if user_input == '--exit' or user_input == '-e':
            cli.clear()
            exit()
        else:
            display_data = cmds['func_call'][user_input]()
            
    elif state[0] == "SHOW_RCP":
        try:
            rcp_id = int(user_input)
        except:
            bad_cmd = True
            break
    
        state.insert(0, "RCP_DETAIL")
        display_data = recipe_detail(rcp_id)
    else: 
        bad_cmd = True
