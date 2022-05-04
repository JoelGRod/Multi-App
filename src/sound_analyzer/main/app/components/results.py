import tkinter as tk
from tkinter import ttk
from pathlib import Path


class Results(ttk.Frame):
    def __init__(self, parent, results):
        ttk.Frame.__init__(self, parent, style="blue.TFrame")
        self.results = results
        self.show_results()
    
    def show_results(self):
        table = ttk.Treeview(self)
        # Columns
        table['columns'] = ('song_name', 'is_fake', 'supposed_bitrate', 'real_bitrate', 'path')
        # Indexes
        table.column('#0', width = 0, stretch=tk.NO)
        table.column('song_name', width= 350, stretch=tk.NO)
        table.column('is_fake', width = 70, anchor = "c", stretch=tk.NO)
        table.column('supposed_bitrate', width = 70, anchor = "c", stretch=tk.NO)
        table.column('real_bitrate', width = 90, anchor = "c", stretch=tk.NO)
        table.column('path', width = 195, anchor = "w", stretch=tk.NO)
        # Columns Headings
        table.heading('#0', text='Id')
        table.heading('song_name', text='Song Name')
        table.heading('is_fake', text='Is Fake?')
        table.heading('supposed_bitrate', text='Bitrate')
        table.heading('real_bitrate', text='Real Bitrate')
        table.heading('path', text='Path')
        # Add To View
        table.grid(row = 0, column = 0, sticky="nesw")
        self.grid_columnconfigure(0, weight = 1)
        # Add results
        for idx, result in enumerate(self.results):
            path_parts = Path(result.path).parts
            table.insert(
                '', tk.END, idx, 
                values=(
                    result.name, 
                    not result.is_valid, 
                    result.bitrate, 
                    result.real_bitrate, 
                    '../' + '/'.join(path_parts[-3:-1])), 
                text=str(idx))