from tkinter import ttk

# Components
from sound_analyzer.main.app.components import (Actions, Results)
# Infrastructure
import sound_analyzer.main.infrastructure.songs as songs


class SoundAnalyzerHome(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        Actions(self).grid(row = 0, column = 0, pady=10, sticky = "w")

    def get_results(self, filepath: str) -> None:
        song_results = songs.analyze_songs(filepath)
        Results(self, song_results).grid(row = 1, column = 0, sticky = "nesw")

