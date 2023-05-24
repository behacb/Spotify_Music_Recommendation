import spotipy as sp
from sklearn.metrics.pairwise import manhattan_distances
from spotipy.oauth2 import SpotifyClientCredentials
cid = "eb018f76e1bb427caf2857fccc6cc719"
secret = "74dc7173c9e34e03aab2b6dad04f2aa8"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = sp.Spotify(client_credentials_manager=client_credentials_manager)
def model_2(df,song_1):
    df['sim'] = manhattan_distances(df.drop(['id', 'id_artists'], axis=1), song_1.drop(['id', 'id_artists'], axis=1))
    df_model = df.sort_values('sim', ascending=True)
    qq = df_model.groupby('id_artists').head(5).id.head(50)  # to limit recmmendation by same artist
    aa = sp.tracks(qq[0:50])
    Fresult_2=[]
    for i in range(50):
        Fresult_2.append(aa['tracks'][i]['name'])
    df.drop("sim", axis=1, inplace=True)
    return Fresult_2