# Main view here
import tkinter as tk
from tkinter import ttk

import router.routes as routes
from config.styles import Styles

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        Styles(self)
        self.frames = self.create_frames(
            self.create_container(), 
            routes.page_values
        )
        self.create_ui(
            routes.page_names, 
            routes.page_frames
        )
        self.show_frame(
            "Sound Analyzer", 
            routes.page_frames
        )
    
    def create_ui(self, page_names, page_frames):
        value = tk.StringVar()
        value.set(page_names[0])
        drop = ttk.OptionMenu(
            self, 
            value, 
            *page_names,
            command=lambda _: self.show_frame(value.get(), page_frames))
        drop.pack()
    
    def create_container(self):
        container = ttk.Frame(self) 
        container.pack(side = "bottom", fill = "both", expand = True)
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