import pandas as pd
import spotipy as sp
from sklearn.metrics.pairwise import euclidean_distances
from spotipy.oauth2 import SpotifyClientCredentials
cid = "eb018f76e1bb427caf2857fccc6cc719"
secret = "74dc7173c9e34e03aab2b6dad04f2aa8"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = sp.Spotify(client_credentials_manager=client_credentials_manager)
def model_1(df,song_1):
    df['sim'] = euclidean_distances(df.drop(['id', 'id_artists'], axis=1), song_1.drop(['id', 'id_artists'], axis=1))
    df_model = df.sort_values('sim', ascending=True)
    qq = df_model.groupby('id_artists').head(10).id.head(10)  # to limit recmmendation by same artist
    aa = sp.tracks(qq[0:10])

    Fresult_1_preview_url=[]

    for i in range(10):
        Fresult_1_preview_url.append(aa["tracks"][i]["id"])

    df.drop("sim", axis=1, inplace=True)
    return Fresult_1_name, Fresult_1_artistname,Fresult_1_preview_url,Fresult_1_image
