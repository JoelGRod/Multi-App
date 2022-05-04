import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from yt_downloader.main.infrastructure.api.youtube_api import YoutubeApi

LARGEFONT =("Verdana", 35)

class YoutubeDownloaderHome(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.yt_downloader = YoutubeApi.get_youtube_downloader()
        self.download_folder = tk.StringVar(value = "./")
        self.video_url = tk.StringVar()
        self.video = None
        self.progressbar = None
        
        self.create_template()
    
    # Template
    def create_template(self):
        # Download Frame
        # Setting Download Folder
        download_folder_label = ttk.Label(self, textvariable = self.download_folder)
        download_folder_label.grid(row = 0, column = 0, sticky = "w")
        set_download_folder_button = ttk.Button(
            self, text = "Set Download Folder", 
            command = self.save_download_folder)
        set_download_folder_button.grid(row = 0, column = 1, padx = 10, sticky = "w")

        # Setting YouTube Video URL
        video_url_entry = ttk.Entry(self)
        video_url_entry.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nesw")
        set_video_url_button = ttk.Button(
            self, text = "Set Video URL", 
            command = lambda: self.save_video_url(video_url_entry))
        set_video_url_button.grid(row = 1, column = 1, padx = 10, sticky = "w")

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)

    def show_video_info(self):
        author_label = ttk.Label(self, text = f"Author: {self.video.author}")
        author_label.grid(row = 2, column = 0, sticky = "w")

        title_label = ttk.Label(self, text = f"Title: {self.video.title}")
        title_label.grid(row = 3, column = 0, sticky = "w")

        video_url_label = ttk.Label(self, text = f"Url: {self.video_url.get()}")
        video_url_label.grid(row = 4, column = 0, sticky = "w")
    
    def show_download_buttons(self):
        buttons_frame = ttk.Frame(self, padding = ("10", "10"))
        buttons_frame.grid(row = 5, column = 0, sticky = "w")
        # Download Resource
        download_video_button = ttk.Button(
            buttons_frame, text="Get Video", 
            command = lambda: self.download("video"))
        download_video_button.grid(row = 0, column = 0, padx = 10)
        download_audio_button = ttk.Button(
            buttons_frame, text="Get Audio", 
            command = lambda: self.download("audio"))
        download_audio_button.grid(row = 0, column = 1, padx = 10)
        self.progressbar = ttk.Progressbar(
            buttons_frame,
            length = 200, 
            mode = "determinate")
        self.progressbar.grid(row = 0, column = 2, padx = 10)
    

    # Script
    def save_download_folder(self) -> None:
        folder = filedialog.askdirectory(title="Select Download Folder")
        self.download_folder.set(folder)
    
    def save_video_url(self, url: tk.Entry) -> None:
        self.video_url.set(url.get())
        url.delete(0, tk.END)
        self.get_video()

    def get_video(self) -> None:
        try:
            self.video = self.yt_downloader.new(self.video_url.get())
            self.show_video_info()
            self.show_download_buttons()
        except ValueError:
            messagebox.showerror(title = "Error", message = "Invalid URL, Try Again")

    def download(self, download_type) -> None:
        stream = None
        if(download_type == "video"):
            stream = self.video.getbest(
                preftype="mp4", 
                ftypestrict=False
            )
        if(download_type == "audio"):
            stream = self.video.getbestaudio(
                preftype="mp3", 
                ftypestrict=False
            )
        # print("Size is %s" % stream.get_filesize())
        stream.download(
            filepath = self.download_folder.get(), 
            quiet = True,
            callback = self.download_status)  # starts download
    
    def download_status(self, total, recvd, ratio, rate, eta):
        self.progressbar['value'] = int(ratio * 100)
        self.update()
