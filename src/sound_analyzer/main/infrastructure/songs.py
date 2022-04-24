import pathlib
from sound_analyzer.main.domain.audio_checker import AudioChecker
from sound_analyzer.main.domain.song import Song

def find_songs(path: str) -> list[str]:
    path = pathlib.Path(path)
    if(path.is_file()): return [path]
    elif(path.is_dir()): return list(filter(
        lambda path: path.suffix in [".mp3", ".wav", ".flac"], 
        path.glob("**/*")
    ))
    return []

def analyze_songs(path: str, **kwargs) -> list[Song]:
    song_paths = find_songs(path)
    audio_checker = AudioChecker()
    return list(
        map(lambda song_path: audio_checker.check_file(song_path, **kwargs),
        song_paths
    ))