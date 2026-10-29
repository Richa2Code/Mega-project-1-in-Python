from urllib.parse import quote_plus

def _youtube_search(query):
    return "https://www.youtube.com/results?search_query=" + quote_plus(query)

music = {
    "tum hi ho": _youtube_search("Tum Hi Ho Arijit Singh"),
    "kesariya": _youtube_search("Kesariya Brahmastra Arijit Singh"),
    "believer": _youtube_search("Believer Imagine Dragons"),
}

def get_song_link(song_name):
    song_name = song_name.strip().lower()
    if song_name in music:
        return music[song_name]
    return _youtube_search(song_name)