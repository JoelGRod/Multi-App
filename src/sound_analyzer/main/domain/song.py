class Song:
    def __init__(self, name, path, is_valid, bitrate, real_bitrate) -> None:
        self.name: str = name
        self.path: str = path
        self.is_valid: bool = is_valid
        self.bitrate: str = bitrate
        self.real_bitrate: str = real_bitrate
