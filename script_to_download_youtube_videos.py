# For refrence https://github.com/hastagAB/Awesome-Python-Scripts/blob/master/Youtube_Video_Downloader/download_video.py

# Requirements
# pytube

from pytube import YouTube
link = input('https://youtu.be/6M1rP2r672o')
yt = Youtube(link)
yt.streams.first().download()
print('downloaded', link)
