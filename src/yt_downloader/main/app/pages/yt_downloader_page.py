import tkinter as tk
from tkinter import filedialog

import apafy

LARGEFONT =("Verdana", 35)

class YoutubeDownloaderHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.download_folder = tk.StringVar()
        self.download_folder.set("No Specified")
        self.video_url = tk.StringVar()
        self.video_url.set("No Specified")

        # UI
        title_frame = tk.Frame(self, padx = 10, pady = 10, width=100)
        title_frame.grid(row = 0, column = 0, sticky = "w")
        dl_frame = tk.Frame(self, padx = 10, pady = 10, width=100)
        dl_frame.grid(row = 1, column = 0, sticky = "w")

        # Title frame
        label = tk.Label(title_frame, text ="Youtube Downloader", font = LARGEFONT)
        label.grid(row = 0, column = 0)

        # Download Frame
        url_label = tk.Label(dl_frame, text="Video URL:")
        url_label.grid(row = 0, column = 0, padx = 10, sticky = "w")
        url_entry = tk.Entry(dl_frame, width = 40)
        url_entry.grid(row = 0, column = 1, padx = 10)
        set_video_url_button = tk.Button(
            dl_frame, text="Set Video URL", 
            command = lambda: self.save_video_url(url_entry))
        set_video_url_button.grid(row = 0, column = 2, padx = 10, sticky = "w")

        folder_label = tk.Label(dl_frame, text="Download Folder:")
        download_folder_label = tk.Label(dl_frame, textvariable=self.download_folder)
        folder_label.grid(row = 1, column = 0, padx = 10, sticky = "w")
        download_folder_label.grid(row = 1, column = 1, padx = 10, sticky = "w")
        select_folder_button = tk.Button(
            dl_frame, text="Download Folder", 
            command = self.save_download_folder)
        select_folder_button.grid(row = 1, column = 2, padx = 10, sticky = "w")

        url_video_label = tk.Label(dl_frame, text="Video URL:")
        url_video_confirmed_label = tk.Label(dl_frame, textvariable=self.video_url)
        url_video_label.grid(row = 2, column = 0, padx = 10, sticky = "w")
        url_video_confirmed_label.grid(row = 2, column = 1, padx = 10, sticky = "w")

    
        download_video_button = tk.Button(
            dl_frame, text="Get Video", 
            command = lambda: self.download("video"))
        download_video_button.grid(row = 3, column = 0, padx = 10, sticky = "w")
        download_audio_button = tk.Button(
            dl_frame, text="Get Audio", 
            command = lambda: self.download("audio"))
        download_audio_button.grid(row = 3, column = 1, padx = 10, sticky = "w")

    # Scripts
    def save_download_folder(self) -> None:
        folder = filedialog.askdirectory(title="select songs directory")
        self.download_folder.set(folder)
    
    def save_video_url(self, url: tk.Entry) -> None:
        self.video_url.set(url.get())
        url.delete(0, tk.END)

    def download(self, download_type) -> None:
        video = apafy.new(self.video_url.get())
        stream = None
        if(download_type == "video"):
            stream = video.getbest()
        if(download_type == "audio"):
            stream = video.getbestaudio()
        print("Size is %s" % stream.get_filesize())
        filename = stream.download(self.download_folder.get())  # starts download

    
        






# Video Info
# title = tk.Label(self, text=f"Title: {video.title}")
# title.grid(row = 1, column = 0)
# rating = tk.Label(self, text=f"Rating: {video.rating}")
# rating.grid(row = 1, column = 1)
# author = tk.Label(self, text=f"Author: {video.author}")
# author.grid(row = 1, column = 2)
# viewcount = tk.Label(self, text=f"Views: {video.viewcount}")
# viewcount.grid(row = 2, column = 0)
# duration = tk.Label(self, text=f"Duration: {video.duration}")
# duration.grid(row = 2, column = 1)
# likes = tk.Label(self, text=f"Likes: {video.likes}")
# likes.grid(row = 2, column = 2)
# dislikes = tk.Label(self, text=f"Dislikes: {video.dislikes}")
# dislikes.grid(row = 3, column = 0)
# description = tk.Label(self, text=f"Description: {video.description}")
# description.grid(row = 3, column = 1)
# published = tk.Label(self, text=f"Published: {video.published}")
# published.grid(row = 3, column = 2
# image = tk.Label(self, text=f"Image: {video.bigthumb}")
# image.grid(row = 4, column = 0)