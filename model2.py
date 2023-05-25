import spotipy as sp
import pandas as pd
from sklearn.metrics.pairwise import manhattan_distances
from spotipy.oauth2 import SpotifyClientCredentials
cid = "eb018f76e1bb427caf2857fccc6cc719"
secret = "74dc7173c9e34e03aab2b6dad04f2aa8"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = sp.Spotify(client_credentials_manager=client_credentials_manager)
def model_2(df,song_1):
    df['sim'] = manhattan_distances(df.drop(['id', 'id_artists'], axis=1), song_1.drop(['id', 'id_artists'], axis=1))
    df_model = df.sort_values('sim', ascending=True)
    qq = df_model.groupby('id_artists').head(10).id.head(10)  # to limit recmmendation by same artist
    aa = sp.tracks(qq[0:10])
    Fresult_2_name = []
    Fresult_2_artistname=[]
    Fresult_2_preview_url=[]
    Fresult_2_image=[]
    for i in range(10):
        Fresult_2_name.append(aa['tracks'][i]['name'])
        Fresult_2_artistname.append(aa["tracks"][i]["album"]["artists"][0]["name"])
        Fresult_2_preview_url.append(aa["tracks"][i]["id"])
        try:
            Fresult_2_image.append(aa["tracks"][i]["album"]["images"][0]["url"])
        except:
            None

    df.drop("sim", axis=1, inplace=True)
    return Fresult_2_name, Fresult_2_artistname, Fresult_2_preview_url, Fresult_2_image
