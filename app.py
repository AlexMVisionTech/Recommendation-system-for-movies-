import streamlit as st
import pandas as pd
import requests
import pickle

# Loading the movie recommendation model
with open('movie_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)
    movies_full_data = model['movies_full_data']
    cosine_sim = model['cosine_sim']

def get_recommendations(title, cosine_sim=cosine_sim):
    """Get movie recommendations based on the title."""
    try:
        idx = movies_full_data[movies_full_data['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  
        movie_indices = [i[0] for i in sim_scores]
        # Including 'movieId' in the returned DataFrame
        return movies_full_data.iloc[movie_indices][['title', 'genres', 'rating', 'movieId']].reset_index(drop=True)
    except Exception as e:
        st.error(f"Error getting recommendations: {str(e)}")
        return pd.DataFrame()  # Returning an empty DataFrame

def fetch_poster(movieId):
    """Fetch movie poster from TMDB API using movie ID."""
    api_key = 'b8799fc8869f0634aff69e08cf9e3417'
    url = f"https://api.themoviedb.org/3/movie/{movieId}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Check if 'poster_path' exists in the response
    if 'poster_path' in data:
        poster_path = data['poster_path']
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}" 
        return full_path
    else:
        return None  # Return None if no poster is found

# Streamlit app layout
st.title("🎬 Movie Recommendation System")

# Input for movie title
title = st.text_input("Enter a movie title:")

if st.button("Get Recommendations"):
    if title:
        recommendations = get_recommendations(title)
        if not recommendations.empty:
            st.write("### Recommendations:")
            for index, row in recommendations.iterrows():
                st.write(f"**{row['title']}**")
                st.write(f"Genres: {row['genres']}")
                st.write(f"Rating: {row['rating']}")
                
                # Fetch and display movie poster using movieId
                poster_url = fetch_poster(row['movieId'])  # Use 'movieId' here
                if poster_url:
                    st.image(poster_url, width=200)
                else:
                    st.warning("Poster not available.")
        else:
            st.warning("No recommendations found. Please try another movie title.")
    else:
        st.warning("Please enter a movie title.")
