import tkinter as tk
class Button:
    def __init__(self, name, x, y, function):
        self.button = tk.Button(
                      bg='#5349CD',
                      fg='#FFFFFF',
                      text=name,
                      font=("Helvitica", int(10.0)),
                      borderwidth = 0,
                      command=function,
                      highlightthickness = 0,
                      relief="flat"
                      )
        self.button.place(
             x=x,
             y=y,
             width = 120,
             height = 48
        )