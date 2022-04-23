import tkinter as tk
from tkinter import filedialog

import sound_analyzer.main.infrastructure.songs as songs

root = tk.Tk()
root.title('Multi App')
root.geometry('500x500')


def open_files(selection: str):
    if selection == "dir":
        root.filename = filedialog.askdirectory(title="select songs directory")
    if selection == "file":
        root.filename = filedialog.askopenfilename(
            title="select song", filetypes=(("mp3 files", "*.mp3"), ("all", "*"))
        )
    songs_paths = songs.check_path(root.filename)
    print(songs.analyze_songs(songs_paths))


directory_button = tk.Button(text="Select Songs Directory", command=lambda: open_files("dir"), )
file_button = tk.Button(text="Select a Song", command=lambda: open_files("file"))
directory_button.pack()
file_button.pack()

root.mainloop()