import pandas as pd 
import numpy as np 

def recommender_system(song_name, df, similarity_matrix, artist_name=None, n_recommendations=10):
    if song_name in df['track_name'].values:
        song_idx = df[df['track_name'] == song_name].index[0]
        sim_scores = similarity_matrix[song_idx]
        sorted_indices = sim_scores.argsort()[::-1]
        recommended_songs = sorted_indices[1:n_recommendations+1]
        song_names = df.iloc[recommended_songs][['track_name', 'artist_name']]
        return song_names
    else:
        return None