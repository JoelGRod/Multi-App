import apafy

def downloader():
    video = apafy.new("https://www.youtube.com/watch?v=GAis7CCoFRg&t=313s")
    return video

    # s = v.getbest()

    # s = v.getbestaudio()

    # print("Size is %s" % s.get_filesize())
    # filename = s.download("./downloads/")  # starts download

