# Main view here
import tkinter as tk
from tkinter import ttk

from router import router
from config.styles import Styles
from shared.main.components import NavBar

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        self.create_navbar(
            self.create_container(0, 0),
            router.page_names, 
            router.page_frames
        )
        self.frames = router.create_frames(
            self.create_container(1, 0), 
            self
        )
        self.show_frame(
            router.page_names[1], 
            router.page_frames
        )
        Styles(self)
    
    def create_navbar(self, container, page_names, page_frames):
        navbar = NavBar(
            container, 
            self, 
            page_names, 
            page_frames)
        navbar.grid(row = 0, column = 0, sticky="nesw")
    
    def create_container(self, row, col):
        container = ttk.Frame(self, padding = ("10", "10"))
        container.grid(row = row, column = col, sticky="nesw")
        container.grid_rowconfigure(row, weight = 1)
        container.grid_columnconfigure(col, weight = 1)
        return container

    def show_frame(self, page, page_frames):
        frame = self.frames[page_frames[page]]
        frame.tkraise()


app = tkinterApp()
app.mainloop()