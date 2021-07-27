import tkinter as tk
from entry import entry
from entry import take
def button ():
	b = tk.Button(text="Add Task!",bg="red",fg="white",command=take())
	b.pack()