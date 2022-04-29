# Main view here
import tkinter as tk
from tkinter import ttk

import router.routes as routes
from config.styles import Styles

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        Styles(self)
        self.frames = self.create_frames(
            self.create_container(), 
            routes.page_values
        )
        self.create_navbar(
            routes.page_names, 
            routes.page_frames
        )
        self.show_frame(
            "Sound Analyzer", 
            routes.page_frames
        )
    
    def create_navbar(self, page_names, page_frames):
        navbar_frame = ttk.Frame(self, padding = ("10", "10"))
        navbar_frame.grid(row = 0, column = 0, sticky = "nsew")
        # navbar_frame.grid(row = 0, column = 0, sticky = "e")
        value = tk.StringVar()
        value.set(page_names[0])
        app_title_label = ttk.Label(navbar_frame, text = "Multi App", style = "title.TLabel")
        app_title_label.grid(row = 0, column = 0, sticky = "nesw")
        drop = ttk.OptionMenu(
            navbar_frame, 
            value, 
            *page_names,
            direction = "flush",
            command=lambda _: self.show_frame(value.get(), page_frames))
        drop.grid(row = 0, column = 1, sticky = "nesw")
        exit_button = ttk.Button(
            navbar_frame, 
            text = "Exit", 
            command = self.quit)
        exit_button.grid(row = 0, column = 2, sticky = "nesw")
        navbar_frame.columnconfigure(0, weight = 9)
        navbar_frame.columnconfigure(1, weight = 2)
        navbar_frame.columnconfigure(2, weight = 1)
    
    def create_container(self):
        container = ttk.Frame(self, padding = ("10", "10")) 
        # container.pack(side = "bottom", fill = "both", expand = True)
        container.grid(row = 1, column = 0)
        container.grid_rowconfigure(0, weight = 1)
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