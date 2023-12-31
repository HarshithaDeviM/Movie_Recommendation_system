import streamlit as st
import pandas as pd
import pickle

def get_similar_movies(movie_name, user_ratings):
    similar_score = item_similarity_df[movie_name] * (user_ratings - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score

# Load the saved model
with open('model.pkl', 'rb') as model_file:
    item_similarity_df = pickle.load(model_file)

movies = pd.read_csv("movies.csv")

# Streamlit UI
st.title("Movie Recommendation App")

# User input for movie preferences
selected_movie = st.selectbox("Select a movie:", movies['title'])
user_rating = st.slider("Rate the movie (1-5):", 1, 5, 3)

# Get similar movies based on user input
similar_movies = get_similar_movies(selected_movie, user_rating)

# Display the top recommended movies with ratings
st.subheader("Top Recommended Movies:")
recommended_movies = similar_movies.head(10).reset_index()
recommended_movies = recommended_movies.rename(columns={selected_movie: 'Ratings'})
recommended_movies = recommended_movies[['title', 'Ratings']]

st.table(recommended_movies)
