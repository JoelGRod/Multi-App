

class Video:
    def __init__(self, video):
        self.title: str = video.title
        self.rating: float or None = video.rating
        self.author: str = video.author
        self.viewcount: int = video.viewcount
        self.duration: str = video.duration
        self.likes: int = video.likes
        self.dislikes: int = video.dislikes
        self.description: str = video.description
        self.thumb: str = video.thumb
        self.bigthumb: str = video.bigthumb
        self.published: str = video.published