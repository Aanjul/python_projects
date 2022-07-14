# For refrence https://python.plainenglish.io/13-advanced-python-scripts-for-everyday-programming-1a52acb84101


# pip install lyricsgenius
import lyricsgenius
api_key = "xxxxxxxxxxxxxxxxxxxxx"
genius = lyricsgenius.Genius(api_key)
artist = genius.search_artist("Pop Smoke", max_songs=5,sort="title")
song = artist.song("100k On a Coupe")

print(song.lyrics)
