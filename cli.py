"""cli.py - command line interface for SousChef"""

import os

commands = {'-s --show': 'Show my loaded recipes', '-a --add': 'Add a new recipe from a URL', '-e --exit': 'Exit the application'}

cli_rows=20

def clear():
    # print('clear\n\n\n')
    os.system('cls')

def prt_header():
    print("""SousChef - Recipes, Nutrition, and Shopping in one Place!\n\n""")

def prt_space(content_rows = 0):
    print('\n'*(20-content_rows))

def prt_cmd(cmds):
    print(f"Available commands:")
    for k,v in cmds.items():
        print(f"{k:12s}  {v}")
    print('\n')

def draw(**kwargs):
    clear()
    prt_header()
    content_rows = 0

    if 'display_data' in kwargs.keys():
        if kwargs['display_data'] != None:
            for data in kwargs['display_data']:
                print(data)
            content_rows = len(kwargs['display_data'])
    
    if 'show_cmds'in kwargs.keys():
        content_rows += len(kwargs['show_cmds'].keys()) + 2
    
        prt_space(content_rows)
        prt_cmd(kwargs['show_cmds'])

        if 'bad_cmd' in kwargs.keys():
            if kwargs['bad_cmd']:
                print('Unrecognized Command.\n')

    user_input = input('Command: ').lower()

    content_rows = 0
    return user_input

def get_url():
    clear()
    prt_header()
    content_rows = 3

    url = input('\n\nAdd a recipe from web.\n(-c or --cancel to cancel)')

    return url
