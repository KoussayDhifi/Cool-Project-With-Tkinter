import tkinter as tk
def entry():
	entry1 = tk.Entry(text="Password",bg="white",fg="blue",show="*")
	name = entry1.get()
	entry1.pack()
	return name
