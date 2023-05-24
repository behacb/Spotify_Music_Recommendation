import pandas as pd
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials

cid = "eb018f76e1bb427caf2857fccc6cc719"
secret = "74dc7173c9e34e03aab2b6dad04f2aa8"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = sp.Spotify(client_credentials_manager=client_credentials_manager)
def get_song_features(url):

    uri_id = f"{url}".split('/')[-1].split('?')[0]
    uri = "spotify:track:" + uri_id
    a = sp.track(track_id=uri)
    song = sp.search(a["name"], limit=5)
    release_date = song["tracks"]["items"][0]["album"]["release_date"]
    duration_ms = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["duration_ms"]
    danceability = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["danceability"]
    energy = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["energy"]
    key = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["key"]
    loudness = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["loudness"]
    mode = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["mode"]
    speechiness = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["speechiness"]
    acousticness = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["acousticness"]
    instrumentalness = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["instrumentalness"]
    liveness = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["liveness"]
    valence = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["valence"]
    tempo = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["tempo"]
    time_signature = sp.audio_features(song["tracks"]["items"][0]["id"])[0]["time_signature"]
    id_artists = song["tracks"]["items"][0]["album"]["artists"][0]["id"]
    id_artists = [f"['{id_artists}']"]
    id = uri_id

    data = {"id": id, "duration_ms": duration_ms, "id_artists": id_artists,
            "release_date": release_date,
            "danceability": danceability,
            "energy": energy, "key": key, "loudness": loudness, "mode": mode,
            "speechiness": speechiness,
            "acousticness": acousticness, "instrumentalness": instrumentalness,
            "liveness": liveness, "valence": valence, "tempo": tempo, "time_signature": time_signature}
    song_1 = pd.DataFrame(data, index=[0])
    song_1['release_date'] = pd.to_datetime(song_1['release_date'])
    song_1["release_date"] = song_1["release_date"].apply(lambda x: x.strftime("%Y"))

    return song_1