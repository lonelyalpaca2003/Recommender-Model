import pandas as pd
import numpy as np

def load_full_data():
    full_df = pd.read_csv('./data/spotify.csv')
    return full_df

def load_processed_data():
    processed_df = pd.read_csv('./data/data_sample.csv')
    return processed_df

def load_similarity_matrix():
   similarity_matrix = np.load('./data/similarity_matrix.npy')
   return similarity_matrix
