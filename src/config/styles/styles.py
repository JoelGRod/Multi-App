from tkinter import ttk

class Styles:
    def __init__(self, root) -> None:
        self.style = ttk.Style(root)
        self.style.theme_use('clam')
        self.main_styles()

    def main_styles(self):
        self.style.configure(
            "TMenubutton", 
            padding = ("10", "10"), 
            foreground="#f3f3f3",
            background="#333333",
            # anchor = "0",
            # compound = "100", 
            # space = "100", 
            # text = "100", 
            font = ("Verdana", 20), 
            # underline = ("100", "100"), 
            width = "10", 
            # justify = "100", 
            # wraplength = "100", 
            embossed = "100", 
            # image = "", 
            # stipple = "50",
            shiftrelief = "10", # Line Down
            # relief = "10"
        )