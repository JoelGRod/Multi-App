import tkinter as tk
from tkinter import ttk


class NavBar(ttk.Frame):
    def __init__(self, parent, controller, page_names, page_frames):
        ttk.Frame.__init__(self, parent)
        value = tk.StringVar()
        value.set(page_names[0])

        app_title_label = ttk.Label(
            self, 
            text = "Multi App", 
            style = "title.TLabel"
        )
        app_title_label.grid(row = 0, column = 0, sticky = "w")

        options_frame = ttk.Frame(self)
        drop = ttk.OptionMenu(
            options_frame, 
            value, 
            *page_names,
            direction = "flush",
            command=lambda _: controller.show_frame(value.get(), page_frames))
        drop.grid(row = 0, column = 0)
        
        exit_button = ttk.Button(
            options_frame, 
            text = "Exit",
            width= "5", 
            command = self.quit)
        exit_button.grid(row = 0, column = 1)
        options_frame.grid(row = 0, column = 1, sticky="e")

        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
  
        