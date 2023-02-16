import tkinter as tk

gui = tk.Tk()
gui.title('Sous Chef')
gui.geometry("1024x760")

frame = tk.Frame(gui)
bottom_frame = tk.Frame(gui).pack(side='bottom')

label_title = tk.Label(frame, text="Sous Chef - Recipes, Nutrition, and Pricing all in one place.")
label_title.grid(row=0)

tk.Label(frame, text='User zip code').grid(row=1)
user_zip = tk.Entry(frame)
user_zip.grid(row=1, column=1)

frame.pack(side='top', anchor='nw')

button_exit = tk.Button(bottom_frame, text='Exit', bg='grey', fg='black',  command=gui.destroy)
# button_exit.pack()
button_exit.place(relx=.9, rely=.9, anchor='ne')

gui.mainloop()