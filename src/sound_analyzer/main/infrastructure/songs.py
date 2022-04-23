import pathlib
from sound_analyzer.main.domain.audio_checker import AudioChecker
from sound_analyzer.main.domain.song import Song

def check_path(path: str) -> list[str]:
    path = pathlib.Path(path)
    song_paths = []
    if(path.is_file()):
        song_paths.append(str(path))
    if(path.is_dir()):
        for p in path.glob("**/*"):
            if p.suffix in [".mp3", ".wav", ".flac"]:
                song_paths.append(p)
    return song_paths

def analyze_songs(song_paths: list[str], **kwargs) -> list[Song]:
    return list(
        map(lambda song_path: AudioChecker.check_file(song_path, **kwargs),
        song_paths
    ))