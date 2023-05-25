import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.metrics.pairwise import euclidean_distances,manhattan_distances
from PIL import Image
from model1 import model_1
from model2 import model_2
from aud_feat import get_song_features
import pandas as pd


def main():

    df_1=pd.read_parquet("final_df_1.parquet")
    df_2=pd.read_parquet("final_df_2.parquet")
    df_3=pd.read_parquet("final_df_3.parquet")
    df_4=pd.read_parquet("final_df_4.parquet")
    df_5=pd.read_parquet("final_df_5.parquet")
    df=pd.concat([df_1,df_2,df_3,df_4,df_5],ignore_index=True)
    df.drop("Unnamed: 0", axis=1, inplace=True)
    st.set_page_config(page_title="Spotiuul", page_icon="musical_note", layout="centered")
    img = Image.open("Image2.jpg")
    st.image(img)

    st.title("Spotiuul")
    with st.expander("Here's how to find any Song URL in Spotify"):
        st.write(""" 
                        1. Search for Song on the Spotify app
                        2. Right Click on the Song you like
                        3. Click "Share"
                        4. Choose "Copy link to Song" """)
    model = st.radio("Select Model", ("Düz Yol Yöntemi", "Merdiven Yöntemi"))
    url = st.text_input(label="URL",placeholder="Enter Spotify Song Url")
    if st.checkbox("Get Recommendations"):
        song = get_song_features(url)
        if model == "Düz Yol Yöntemi":
            last_result_name,last_result_artistname,last_result_preview_url,last_result_image = model_1(df, song)
            for i in range(10):
                st.image(last_result_image[i])
                st.write(f"Song Name: {last_result_name[i]}")
                st.write(f"Artist Name: {last_result_artistname[i]}")
                uri_link = "https://open.spotify.com/embed/track/" + last_result_preview_url[
                    i] + "?utm_source=generator&theme=0"
                components.iframe(uri_link, height=80)
                st.write("\n")
                st.write("\n")

        if model == "Merdiven Yöntemi":
            last_result_name,last_result_artistname,last_result_preview_url,last_result_image = model_2(df, song)
            for i in range(10):
                st.image(last_result_image[i])
                st.write(f"Song Name: {last_result_name[i]}")
                st.write(f"Artist Name: {last_result_artistname[i]}")
                uri_link = "https://open.spotify.com/embed/track/" + last_result_preview_url[
                    i] + "?utm_source=generator&theme=0"
                components.iframe(uri_link, height=80)
                st.write("\n")
                st.write("\n")


if __name__ == '__main__':
    main()
