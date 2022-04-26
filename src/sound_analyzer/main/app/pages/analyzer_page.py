import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import sound_analyzer.main.infrastructure.songs as songs

LARGEFONT =("Verdana", 35)

class SoundAnalyzerHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.filepath = ""

        label = tk.Label(self, text ="Sound Analyzer", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        directory_button = tk.Button(self, text="Select Songs Directory", command=lambda: self.get_filepath("dir"), )
        file_button = tk.Button(self, text="Select a Song", command=lambda: self.get_filepath("file"))
        directory_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        file_button.grid(row = 0, column = 2, padx = 10, pady = 10)

    def get_filepath(self, selection: str):
        if selection == "dir":
            self.filepath = filedialog.askdirectory(title="select songs directory")
        if selection == "file":
            self.filepath = filedialog.askopenfilename(
                title="select song", filetypes=(("audio files", "*.mp3 *.wav *.flac"), ("all", "*"))
            )
        if self.filepath != "":
            song_results = songs.analyze_songs(self.filepath)
            self.show_results(song_results)
    
    def show_results(self, results):
        table = ttk.Treeview(self)
        # Columns
        table['columns'] = ('song_name', 'is_fake', 'supposed_bitrate', 'real_bitrate', 'path')
        # Indexes
        table.column('#0', width = 0, stretch=tk.NO)
        table.column('song_name')
        table.column('is_fake')
        table.column('supposed_bitrate')
        table.column('real_bitrate')
        table.column('path')
        # Columns Headings
        table.heading('#0', text='Id')
        table.heading('song_name', text='Song Name')
        table.heading('is_fake', text='Is Fake?')
        table.heading('supposed_bitrate', text='Supposed Bitrate')
        table.heading('real_bitrate', text='Real Bitrate')
        table.heading('path', text='Path')
        # Add To View
        table.grid(row = 1, column = 0)
        # Add results
        for idx, result in enumerate(results):
            table.insert(
                '', tk.END, idx, 
                values=(
                    result.name, 
                    not result.is_valid, 
                    result.bitrate, 
                    result.real_bitrate, 
                    result.path), 
                text=str(idx))

