"""SousChef.py - Get Recipes, FDA Nutrition, and Kroger Corp Pricing"""

# Dependencies
import recipes
import kroger
import cli
import tkinter as tk

def show_recipes():
    if len(recipes.my_recipes) == 0:
        print('no recipes saved.')
    for recipe in recipes.my_recipes:
        print(f"{recipe['id']}: {recipe['name']}")

def add_recipe():
    user_input = input('Paste a URL: ')

    status, html = recipes.fetch_from_url(user_input)

    if status==200:
        recipe = recipes.html_to_recipe(html)
    else:
        print(f'Unable to reach site:\n\n Response{status}\nMessage:  {html}')
    
    recipes.write(recipe)

print('Starting SousChef\n')

commands = {'exit': exit, 'show': show_recipes, 'add':add_recipe}

# Get recipes
if len(recipes.my_recipes) == 0:
    print("You have no saved recipes. Command 'A' to add one")

while True:
    cli.draw()
    
    user_input = input('Command: ').lower()
    if user_input in commands.keys():
        commands[user_input]()
    else:
        print(f'"{user_input}" is not a recognized command.')



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
