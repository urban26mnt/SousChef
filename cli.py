"""cli.py - command line interface for SousChef"""

import os

commands = {'show': 'Show my loaded recipes', 'add': 'Add a new recipe from a URL', 'exit': 'Exit the application'}

cli_rows=20
content_rows=0

def clear():
    os.system('cls')

def prt_header():
    print("""SousChef - Recipes, Nutrition, and Shopping in one Place!\n\n""")

def prt_space(content_rows = 0):
    print('\n'*(20-content_rows))

def prt_cmd():
    global content_rows
    print(f"Available commands:")
    for k,v in commands.items():
        print(f"{k:10s}: {v}")
        content_rows += 1

def draw(data=None):
    global content_rows
    clear()
    prt_header()
    if data == None:
        prt_cmd()
        
    prt_space()


    content_rows = 0
