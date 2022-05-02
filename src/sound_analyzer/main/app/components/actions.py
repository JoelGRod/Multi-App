from tkinter import ttk
from tkinter import filedialog


class Actions(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        self.show_actions()

    def show_actions(self):
        directory_button = ttk.Button(self, text="Select Songs Directory", command=lambda: self.get_filepath("dir"), )
        file_button = ttk.Button(self, text="Select a Song", command=lambda: self.get_filepath("file"))
        directory_button.grid(row = 0, column = 0)
        file_button.grid(row = 0, column = 1)
    
    def get_filepath(self, selection: str):
        filepath = ""
        if selection == "dir":
            filepath = filedialog.askdirectory(title="select songs directory")
        if selection == "file":
            filepath = filedialog.askopenfilename(
                title="select song", filetypes=(("audio files", "*.mp3 *.wav *.flac"), ("all", "*"))
            )
        if filepath != "": self.parent.get_results(filepath)
