import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 35)

class ExampleFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button1 = ttk.Button(self, text ="Page 1",
        #                         command = lambda : controller.show_frame(Page1))
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button2 = ttk.Button(self, text ="Page 2",
        #                         command = lambda : controller.show_frame(Page2))
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button1 = ttk.Button(self, text ="StartPage",
        #                         command = lambda : controller.show_frame(StartPage))
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button2 = ttk.Button(self, text ="Page 2",
        #                         command = lambda : controller.show_frame(Page2))
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button1 = ttk.Button(self, text ="Page 1",
        #                         command = lambda : controller.show_frame(Page1))
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button2 = ttk.Button(self, text ="Startpage",
        #                         command = lambda : controller.show_frame(StartPage))
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
# Delete