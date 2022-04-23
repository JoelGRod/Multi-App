import tkinter as tk
from tkinter import filedialog

import sound_analyzer.main.infrastructure.songs as songs

root = tk.Tk()
root.title('Multi App')
root.geometry('500x500')


def get_filepath(selection: str):
    if selection == "dir":
        root.filename = filedialog.askdirectory(title="select songs directory")
    if selection == "file":
        root.filename = filedialog.askopenfilename(
            title="select song", filetypes=(("audio files", "*.mp3 *.wav *.flac"), ("all", "*"))
        )
    if root.filename != "":
        songs_paths = songs.check_path(root.filename)
        print(songs.analyze_songs(songs_paths))


directory_button = tk.Button(text="Select Songs Directory", command=lambda: get_filepath("dir"), )
file_button = tk.Button(text="Select a Song", command=lambda: get_filepath("file"))
directory_button.pack()
file_button.pack()

root.mainloop()