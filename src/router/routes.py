from sound_analyzer.main.app.pages.analyzer_page import SoundAnalyzerHome
from yt_downloader.main.app.pages.yt_downloader_page import YoutubeDownloaderHome

page_frames = {
    # "Home": StartPage,
    "Sound Analyzer": SoundAnalyzerHome,
    "YouTube Downloader": YoutubeDownloaderHome
}

page_names = list(page_frames.keys())

page_values = tuple(page_frames.values())
