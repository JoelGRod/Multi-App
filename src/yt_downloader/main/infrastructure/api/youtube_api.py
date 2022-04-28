import apafy

import config.secrets as secrets

class YoutubeApi:
    @classmethod
    def get_youtube_downloader(cls):
        # apafy.set_api_key(secrets.youtube_api_key)
        return apafy