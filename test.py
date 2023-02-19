import argparse

def show():
    print('show!')

cmd = {'-e':exit,
       '--exit': exit,
       '-s':show,
       '--show':show}

ap = argparse.ArgumentParser(prog="SousChef.py", description="Recipes, Nutrition, .etc")
ap.add_argument('-e', '--exit', metavar='exit', help="Exit the application")
ap.add_argument('-s', '--show', metavar='show', help="Show Recipes")
ap.add_argument('cmd', choices=cmd.keys(), help="Available commmands")

while True:
    user_input = input("Command: ").split()
    if user_input[0] in cmd:
        cmd[user_input[0]]()
    else:
        try:
            args = ap.parse_args(user_input)
            cmd[args.cmd]()
        except:
            print('')
