import tkinter as tk
from yt_downloader.main.infrastructure.downloader import downloader

LARGEFONT =("Verdana", 35)

class YoutubeDownloaderHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # UI
        label = tk.Label(self, text ="Youtube Downloader", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        # Scripts
        video = downloader()
        # Video Info
        title = tk.Label(self, text=f"Title: {video.title}")
        title.grid(row = 1, column = 0)
        rating = tk.Label(self, text=f"Rating: {video.rating}")
        rating.grid(row = 1, column = 1)
        author = tk.Label(self, text=f"Author: {video.author}")
        author.grid(row = 1, column = 2)
        viewcount = tk.Label(self, text=f"Views: {video.viewcount}")
        viewcount.grid(row = 2, column = 0)
        duration = tk.Label(self, text=f"Duration: {video.duration}")
        duration.grid(row = 2, column = 1)
        likes = tk.Label(self, text=f"Likes: {video.likes}")
        likes.grid(row = 2, column = 2)
        dislikes = tk.Label(self, text=f"Dislikes: {video.dislikes}")
        dislikes.grid(row = 3, column = 0)
        description = tk.Label(self, text=f"Description: {video.description}")
        description.grid(row = 3, column = 1)
        published = tk.Label(self, text=f"Published: {video.published}")
        published.grid(row = 3, column = 2)

        image = tk.Label(self, text=f"Image: {video.bigthumb}")
        image.grid(row = 4, column = 0)