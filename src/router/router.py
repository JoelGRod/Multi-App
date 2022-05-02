from sound_analyzer.main.app.pages.analyzer_page import SoundAnalyzerHome
from yt_downloader.main.app.pages.yt_downloader_page import YoutubeDownloaderHome

page_frames = {
    # "Home": StartPage,
    "Sound Analyzer": SoundAnalyzerHome,
    "YouTube Downloader": YoutubeDownloaderHome
}

page_names = ['Options'] + list(page_frames.keys())

page_values = tuple(page_frames.values())

def create_frames(container, controller):
    frames = {}
    for F in page_values:
        frame = F(container, controller)
        frames[F] = frame
        frame.grid(row = 0, column = 0, sticky="nesw")
    return frames
