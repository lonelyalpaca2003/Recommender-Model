import pandas as pd 
import streamlit as st
from data_loader import load_processed_data, load_similarity_matrix
from model import recommender_system

@st.cache_data
def load_data():
   return load_processed_data()

@st.cache_data  
def load_sim_matrix():
   return load_similarity_matrix()

df = load_data()
similarity_matrix = load_sim_matrix()

st.title("Song Recommender")

song_list = df['track_name'].tolist()
selected_song = st.selectbox("Pick a song:", song_list)

if st.button("Get Recommendations"):
   recommendations = recommender_system(selected_song, df, similarity_matrix)
   if recommendations is not None:
       st.write("Similar songs:")
       st.table(recommendations.reset_index(drop=True))
   else:
       st.write("Song not found!")