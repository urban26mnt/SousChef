"""SousChef.py - Get Recipes, FDA Nutrition, and Kroger Corp Pricing"""

# Dependencies
import recipes
import kroger
import cli
import tkinter as tk

def show_recipes():
    global display_data, state

    display_data = []
    if len(recipes.my_recipes) == 0:
        display_data = ['no recipes saved.']
    for recipe in recipes.my_recipes:
        display_data.append(f"{recipe['id']}: {recipe['name']}")
    
    if state[0] != 'SHOW_RCP':
        state.insert(0, "SHOW_RCP")    

    return display_data

def add_recipe():


    user_input = cli.get_url()

    status, html = recipes.fetch_from_url(user_input)

    if status==200:
        recipe = recipes.html_to_recipe(html)
    else:
        print(f'Unable to reach site:\n\n Response{status}\nMessage:  {html}')
    
    recipes.write(recipe)

def back():
    state.pop(0)
    # print(state)
    # d = input()

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
bad_cmd=False
state = ["MAIN"]

# Program Loop
while True:
    if state[0] == "MAIN":
        display_data=[]
        cmd_set = cmds['disp_main']
    elif state[0] == "SHOW_RCP":
        cmd_set = cmds['disp_recp']

    user_input = cli.draw(display_data=display_data, show_cmds=cmd_set, bad_cmd=bad_cmd)
    bad_cmd = False

    if user_input in cmds['func_call'].keys():
        if user_input == '--exit' or user_input == '-e':
            cli.clear()
            exit()
        else:
            display_data = cmds['func_call'][user_input]()
    else:
        bad_cmd = True

# gui = tk.Tk()
# gui.title('Sous Chef')
# gui.geometry("1024x760")

# frame = tk.Frame(gui)
# bottom_frame = tk.Frame(gui).pack(side='bottom')

# label_title = tk.Label(frame, text="Sous Chef - Recipes, Nutrition, and Pricing all in one place.")
# label_title.grid(row=0)

# tk.Label(frame, text='User zip code').grid(row=1)
# user_zip = tk.Entry(frame)
# user_zip.grid(row=1, column=1)

# frame.pack(side='top', anchor='nw')

# button_exit = tk.Button(bottom_frame, text='Exit', bg='grey', fg='black',  command=gui.destroy)
# # button_exit.pack()
# button_exit.place(relx=.9, rely=.9, anchor='ne')

# gui.mainloop()
