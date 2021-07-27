import tkinter as tk
from entry import entry

name = entry

def command():
	greeting=tk.Label(text=f"Hello {entry}",bg="black")
	greeting.pack()


def button():
	button = tk.Button(bg="red",fg="blue",text="Click me",command=command)
	button.pack()