import tkinter as tk
from tkinter import ttk


class Results(ttk.Frame):
    def __init__(self, parent, results):
        ttk.Frame.__init__(self, parent)
        self.results = results
        self.show_results()
    
    def show_results(self):
        table = ttk.Treeview(self)
        # Columns
        table['columns'] = ('song_name', 'is_fake', 'supposed_bitrate', 'real_bitrate', 'path')
        # Indexes
        table.column('#0', width = 0, stretch=tk.NO)
        table.column('song_name', stretch=tk.NO)
        table.column('is_fake', width = 70, anchor = "c", stretch=tk.NO)
        table.column('supposed_bitrate', width = 70, anchor = "c", stretch=tk.NO)
        table.column('real_bitrate', width = 90, anchor = "c", stretch=tk.NO)
        table.column('path', width = 350, anchor = "c", stretch=tk.NO)
        # Columns Headings
        table.heading('#0', text='Id')
        table.heading('song_name', text='Song Name')
        table.heading('is_fake', text='Is Fake?')
        table.heading('supposed_bitrate', text='Bitrate')
        table.heading('real_bitrate', text='Real Bitrate')
        table.heading('path', text='Path')
        # Add To View
        table.grid(row = 0, column = 0)
        # Add results
        for idx, result in enumerate(self.results):
            table.insert(
                '', tk.END, idx, 
                values=(
                    result.name, 
                    not result.is_valid, 
                    result.bitrate, 
                    result.real_bitrate, 
                    result.path), 
                text=str(idx))