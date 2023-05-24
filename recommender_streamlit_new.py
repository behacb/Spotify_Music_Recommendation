import streamlit as st
# import streamlit.components.v1 as components
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
    df = pd.read_parquet("final_df.parquet")
    df.drop("Unnamed: 0", axis=1, inplace=True)
    st.set_page_config(page_title="Spotify Recommender", page_icon="musical_note", layout="centered")
    # --SideBar------
    menu_list = ["Home", "Get Recommendations", "About"]
    with st.sidebar:
        option = option_menu("MENU",
                             [menu_list[0], menu_list[1], menu_list[2]],
                             icons=['house', 'kanban', 'book'],
                             menu_icon="app-indicator", default_index=0, styles={
                "container": {"padding": "5!important", "background-color": "#1DB954"},
                "icon": {"color": "white", "font-size": "28px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "white"},
                "nav-link-selected": {"background-color": "black"}, })
    # pages
    if option == menu_list[0]:
        st.title("Spotiuul")
        with st.expander("Here's how to find any Song URL in Spotify"):
            st.write(""" 
                        1. Search for Song on the Spotify app
                        2. Right Click on the Song you like
                        3. Click "Share"
                        4. Choose "Copy link to Song" """)
        model = st.radio("Select Model", ("Model 1", "Model 2"))
        url = st.text_input(label="URL",placeholder="Enter Spotify Song Url")
        if st.checkbox("Get Recommendations"):
            song = get_song_features(url)
            if model == "Model 1":
                last_result = model_1(df, song)
                st.text(last_result)
            if model == "Model 2":
                last_result = model_2(df, song)
                st.text(last_result)






            if option == menu_list[1]:

                st.write(last_result)


if __name__ == '__main__':
    main()
