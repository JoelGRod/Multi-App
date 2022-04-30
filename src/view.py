# Main view here
import tkinter as tk
from tkinter import ttk

import router.routes as routes
from config.styles import Styles
from shared.main.components.navbar import NavBar

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        Styles(self)
        self.frames = self.create_frames(
            self.create_container(1), 
            routes.page_values
        )
        self.create_navbar(
            self.create_container(0),
            routes.page_names, 
            routes.page_frames
        )
        self.show_frame(
            "Sound Analyzer", 
            routes.page_frames
        )
    
    def create_navbar(self,container, page_names, page_frames):
        navbar = NavBar(
            container, 
            self, 
            page_names, 
            page_frames)
        navbar.grid(row = 0, column = 0, sticky = "nesw")
    
    def create_container(self, row):
        container = ttk.Frame(self, padding = ("10", "10"))
        container.grid(row = row, column = 0, sticky="nesw")
        container.grid_rowconfigure(row, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        return container
    
    def create_frames(self, container, page_values):
        frames = {}
        for F in page_values:
            frame = F(container, self)
            frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        return frames

    def show_frame(self, page, page_frames):
        frame = self.frames[page_frames[page]]
        frame.tkraise()


app = tkinterApp()
app.mainloop()