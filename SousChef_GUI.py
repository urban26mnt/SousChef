# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:02:13 2023

@author: PZZNVD
"""
from tkinter import *
import tkinter as ttk
import recipes as rec
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()

root = Tk()
#root.geometry("600x600")
root.title("Sous Chef")
#root.state('zoomed')
root.iconbitmap('sous_chef.ico')

root.rowconfigure(0, weight =1)
root.columnconfigure(0, weight =1)


frame3 = ttk.Frame(root)
frame2 = ttk.Frame(root)
frame1 = ttk.Frame(root)

img = Image.open("food.PNG")
resize_img = img.resize((800,200))
conv_img = ImageTk.PhotoImage(resize_img, master=root)

def show1():
    URL_Entered = URLinput.get(1.0, "end-1c")
    url_mesg = rec.add_recipe(URL_Entered)
    url_lbl = ttk.Label(frame1, text = url_mesg, bg='#fffddd',bd = 1, relief = "sunken")
    url_lbl.grid(column=0, row=5, sticky='w')

def show2(recipe):
    label1 = Label( frame2 , text = "   ", bg='#fffddd' )
    label1.config( text = click1.get() )
    recipe1 = click1.get()
    recipe_id = int(recipe1.split(':')[0])

    price1 = rec.recipe_price(recipe_id)
    price_str1 = "Estimated price is " + str(price1)
    l = rec.shopping_list(recipe_id)
    price_lbl1 = Label(frame2, text = price_str1, bg='#fffddd',fg='green', font= 'bold',relief = "sunken")
    price_lbl1.grid(column = 0, row =10, sticky = 'W' )
    text=Text(frame2, width=30, height=15, bg='#fffddd')
    text.grid(column=0, row=11,sticky='W')
#    text.pack()
    for i in l:
        text.insert(END,i + '\n')
    
    
def show3(recipe):
    label2 = Label( frame2 , text = "" )
    label2.config( text = click2.get() )
    recipe2 = click2.get()
    recipe_id = int(recipe2.split(':')[0])

    price2 = rec.recipe_price(recipe_id)
    price_str2 = "Estimated price is " + str(price2)
    price_lbl2 = Label(frame2, text = price_str2, bg='#fffddd',fg='green', font= 'bold', relief = "sunken")
    price_lbl2.grid(column = 1, row =10, sticky = 'W' )
    text=Text(frame2, width=30, height=15, bg='#fffddd')
    l = rec.shopping_list(recipe_id)
    text=Text(frame2, width=30, height=15, bg='#fffddd')
    text.grid(column=1, row=11,sticky='WE')
#    text.pack()
    for i in l:
        text.insert(END, i + '\n')
        
def show_nut1(recipe):
    label3_1 = Label( frame3 , text = "   ", bg='#fffddd' )
    label3_1.config( text = click3_1.get() )
    recipe1 = click3_1.get()
    recipe_id = int(recipe1.split(':')[0])

    l = rec.nutrition_profile(recipe_id)
    text=Text(frame3, width=35, height=15, bg='#fffddd')
    text.grid(column=0, row=10,sticky='W')
#    text.pack()
    for i in l:
        text.insert(END,i + '\n')
    
    
def show_nut2(recipe):
    label3_2 = Label( frame3 , text = "" )
    label3_2.config( text = click3_2.get() )
    recipe2 = click3_2.get()
    recipe_id = int(recipe2.split(':')[0]) 
    
    l = rec.nutrition_profile(recipe_id)
    text=Text(frame3, width=35, height=15, bg='#fffddd')
    text.grid(column=1, row=10,sticky='WE')
#    text.pack()
    for i in l:
        text.insert(END, i + '\n')

def Close():
    root.destroy()

#@##Frame 1
#Image placement for Frame 1
piclbl1 = ttk.Label(frame1, image = conv_img)
piclbl1.grid(column=0, row=0)
frame1.config(bg='#fffddd')
#frame1.resizable(width=True, height=200)

frame1_title = ttk.Label(frame1, text = "Welcome to Sous Chef", font=('calibre',15, 'bold'), bg='#fffddd',bd = 1, relief = "sunken")
frame1_title.grid(column=0, row=1)

enterURLLbl = ttk.Label(frame1, text="Enter a recipe URL to add to saved recipes.", font=('calibre',10, 'bold'), bg='#fffddd')
enterURLLbl.grid(column=0, row=2)

frame1_lbl = ttk.Label(frame1, text = "Search Recipe using URL", bg='#fffddd')
frame1_lbl.grid(column=0, row=3, sticky='w',columnspan= 1)

frame1_btn = Button(frame1,text = "Next", command = lambda: show_frame(frame2))
frame1_btn.grid(column=2, row=0, columnspan=2, sticky='n')


URLinput = ttk.Text(frame1,height = 1, width = 20)
button_url = Button( frame1 , text = "Search" , command = show1 )
URLinput.grid(column=0, row=4, sticky='WE')
button_url.grid(column=1, row=4, sticky='WE')
frame1.columnconfigure(100, weight=2)
#frame1.rowconfigure(1, weight=1)

#@##Frame 2
frame2.config(bg='#fffddd')

frame2_bbtn = Button(frame2,text = "Go back", command = lambda: show_frame(frame1))
frame2_bbtn.grid(column=0, row=0, columnspan=3, sticky='w')
frame2_nbtn = Button(frame2,text = "Next page", command = lambda: show_frame(frame3))
frame2_nbtn.grid(column=10, row=0, columnspan=3)

#Image placement for Frame 2
piclbl2 = ttk.Label(frame2, image = conv_img)
piclbl2.grid(column=0, row=1)

frame2_title1 = ttk.Label(frame2, text = "Compare Recipes - Shopping List and estimated price", font=('calibre',10, 'bold'), bg='#fffddd')
frame2_title1.grid(column=0, row=3)
selectLbl = ttk.Label(frame2, text="Select the two recipes from dropdown to show shopping lists.",fg = 'blue', bg='#fffddd')
selectLbl.grid(column=0, row=4)
infolbl_f2_2 = ttk.Label(frame2, text="Click on \'Next page\' button to compare nutrition between two recipes.\n", bg='#fffddd')
infolbl_f2_2.grid(column=0, row=5)

recipelist = rec.recipe_list()
click1 = StringVar()
click1.set("Pick a recipe")

label11 = Label( frame2 , text = "" )
f2Recipedrop1 = OptionMenu( frame2 , click1 , *recipelist, command = show2)
#f2Recipedrop1 = OptionMenu( frame2 , click1 , *recipelist )
#f2button1 = Button( frame2 , text = "ok" , command = show2 )

click2 = StringVar()
click2.set("Pick a recipe")

f2Recipedrop2 = OptionMenu( frame2 , click2 , *recipelist, command = show3 )
#####Select recipes from dropdown

f2Recipedrop1.grid(column=0, row=8, sticky='W')
#f2button1.grid(column=6, row=8,columnspan= 2, sticky='W')

f2Recipedrop2.grid(column=1, row=8, sticky='W')

##############################################
#@##Frame 3
piclbl3 = ttk.Label(frame3, image = conv_img)
piclbl3.grid(column=0, row=1)

frame3.config(bg='#fffddd')

frame3_bbtn = Button(frame3,text = "Go back", command = lambda: show_frame(frame2))
frame3_bbtn.grid(column=0, row=0, columnspan=3, sticky='w')
frame3_btn = Button(frame3,text = "Next page", command = lambda: show_frame(frame1))
frame3_btn.grid(column=20, row=0, columnspan=3)

frame3_title1 = ttk.Label(frame3, text = "Compare Recipes - Nutrition", font=('calibre',10, 'bold'), bg='#fffddd')
frame3_title1.grid(column=0, row=3)

infolbl_f3_1 = ttk.Label(frame3, text="This page allows you to compare nutrition between two recipes.",fg = 'blue', bg='#fffddd')
infolbl_f3_1.grid(column=0, row=5)
infolbl_f3_2 = ttk.Label(frame3, text="Click on \'Next page\' button to compare prices between two recipes.\n", bg='#fffddd')
infolbl_f3_2.grid(column=0, row=6)

click3_1 = StringVar()
click3_1.set("Pick a recipe")

label3_1 = Label( frame2 , text = "" )
f3Recipedrop1 = OptionMenu( frame3 , click3_1 , *recipelist, command = show_nut1)
#f2Recipedrop1 = OptionMenu( frame2 , click1 , *recipelist )
#f2button1 = Button( frame2 , text = "ok" , command = show2 )

click3_2 = StringVar()
click3_2.set("Pick a recipe")

f3Recipedrop2 = OptionMenu( frame3 , click3_2 , *recipelist, command = show_nut2 )
#####Select recipes from dropdown
f3Recipedrop1.grid(column=0, row=8, sticky='W')
f3Recipedrop2.grid(column=1, row=8, sticky='W')

# Button for closing
exit_button = Button(root, text="Exit", command=Close,bg='#fffddd')
exit_button.grid(column = 0, row =50)

for frame in (frame3, frame2, frame1):
    frame.grid(row = 0, column =0, sticky ='nsew')
      

root.mainloop()