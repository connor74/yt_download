
from __future__ import unicode_literals
import yt_dlp as youtube_dl

path = "C:/Users/KurzanovAV/Documents/youtube/"

def run(url, path):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=url,
        download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f"{path}{filename}",
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

links = []

if __name__=='__main__':
    for i in links:
        run(i, path)
