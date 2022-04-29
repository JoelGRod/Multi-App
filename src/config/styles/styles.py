import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Styles:
    def __init__(self, root) -> None:
        self.style = ttk.Style(root)
        self.style.theme_use('clam')
        self.main_styles()

    def main_styles(self):
        # colors
        colors = {
            "black": "#3b4446",
            "white": "#eff2f3",
            "grey_light_one": "#aeb6b8",
            "grey_light_two": "#d7dcdd",
            "grey_dark_one": "#7b868a",
            "grey_dark_two": "#525e61",
            "grey_dark_three": "#7b868a",
            "blue": "#166a8f",
            "green_one": "#2dbe60",
            "green_two": "#2facb2",
        }

        # Fonts (This does not work with ttk)
        # comic_sans = tkFont.Font(
        #     family = "Comic Sans MS", 
        #     size = 16, 
        #     weight = "bold", 
        #     slant = "roman",
        #     underline = "10",
        #     overstrike = "10"
        # )

        # Widgets
        # Frame
        self.style.configure(
            "TFrame",
            background = colors["black"],
            # borderwidth = "",
            # relief = ""
        )
        # Option Menu
        self.style.configure(
            "TMenubutton", 
            # Padding
                padding = ("10", "10"), 
                # relief = "10"
                # shiftrelief = "10", # Line Down
            # Label
                foreground = colors["black"],
                background = colors["white"],
                borderwidth = 0,
                font = (
                    "Comic Sans MS", 
                    16, 
                    "normal", 
                    "roman", 
                    # "underline", 
                    # "overstrike"
                ), 
                anchor = "e",
                width = "18", 
                # compound = tk.LEFT,
                # image = "", 
                # justify = tk.LEFT, 
                # underline = 10, 
                # space = "100", 
                # text = "100", 
                # wraplength = "100", 
                # embossed = "10", 
                # stipple = "50",
        )
        # Button
        self.style.configure(
            "TButton", 
            # Padding
                padding = ("10", "10"), 
                # relief = "10"
                # shiftrelief = "10", # Line Down
            # Label
                foreground = colors["black"],
                background = colors["white"],
                borderwidth = 0,
                font = (
                    "Comic Sans MS", 
                    16, 
                    "normal", 
                    "roman", 
                    # "underline", 
                    # "overstrike"
                ), 
                anchor = "center",
                width = "5", 
                # compound = tk.LEFT,
                # image = "", 
                # justify = tk.LEFT, 
                # underline = 10, 
                # space = "100", 
                # text = "100", 
                # wraplength = "100", 
                # embossed = "10", 
                # stipple = "50",
        )
        # Label
        self.style.configure(
            "TLabel", 
            # Padding
                padding = ("10", "10"), 
                # relief = "10"
                # shiftrelief = "10", # Line Down
            # Label
                foreground = colors["white"],
                background = colors["black"],
                borderwidth = 0,
                font = (
                    "Comic Sans MS", 
                    16, 
                    "normal", 
                    "roman", 
                    # "underline", 
                    # "overstrike"
                ), 
                anchor = "w",
                width = "30", 
                # compound = tk.LEFT,
                # image = "", 
                # justify = tk.LEFT, 
                # underline = 10, 
                # space = "100", 
                # text = "100", 
                # wraplength = "100", 
                # embossed = "10", 
                # stipple = "50",
        )
        

        # Events
        self.style.map(
            'TMenubutton',
            foreground =        [('disabled', colors["black"]),
                                ('pressed', colors["blue"]),
                                ('active', colors["blue"])],
            background =        [('disabled', colors["grey_light_one"]),
                                ('pressed', '!focus', colors["white"]),
                                ('active', colors["white"])],
            highlightcolor =    [('focus', colors["green_one"]),
                                ('!focus', colors["green_one"])],
            relief =            [('pressed', colors["green_one"]),
                                ('!pressed', colors["green_one"])]
        )
        self.style.map(
            'TButton',
            foreground =        [('disabled', colors["black"]),
                                ('pressed', colors["blue"]),
                                ('active', colors["blue"])],
            background =        [('disabled', colors["grey_light_one"]),
                                ('pressed', '!focus', colors["white"]),
                                ('active', colors["white"])],
            highlightcolor =    [('focus', colors["green_one"]),
                                ('!focus', colors["green_one"])],
            relief =            [('pressed', colors["green_one"]),
                                ('!pressed', colors["green_one"])]
        )
