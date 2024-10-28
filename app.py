import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie posters using TMDb API
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=484a8c33787576d74c1ec32afe152a47&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to recommend movies based on similarity scores
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load movie data and similarity scores
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Page Configuration
st.set_page_config(page_title="Movie Recommender", page_icon="🍿", layout="centered")

# Header with animated gradient
st.markdown("""
    <div style="text-align: center; animation: fadeIn 1.5s;">
        <h1 style="color: #E50914; font-weight: bold; font-size: 2.8rem; margin-bottom: 0; animation: gradientGlow 5s ease-in-out infinite;">
            🍿 Movie Recommendations 🍿
        </h1>
        <p style="color: #e5e5e5; font-size: 1.2rem; font-family: 'Arial', sans-serif;">Discover movies you’ll love, Own Style!</p>
    </div>
""", unsafe_allow_html=True)

# Select movie dropdown
selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values,
    help="Choose a movie to view similar recommendations."
)

# Recommendation Button with Animation
if st.button("🔍 Find Recommendations"):
    with st.spinner("Finding movies..."):
        names, posters = recommend(selected_movie_name)

    # Display recommended movies with hover effect
    st.markdown("<h2 style='text-align: center; color: #E50914;'>Your Movie Recommendations</h2>", unsafe_allow_html=True)
    cols = st.columns(5) if st.expander("For larger screens") else st.columns(1)
    
    # Ensure movies display in columns or a single stack based on screen size
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.markdown(f"""
                <div class="movie-card">
                    <h4>{name}</h4>
                    <img src="{poster}" class="movie-poster"/>
                </div>
            """, unsafe_allow_html=True)

    # Footer with link
    st.markdown("---")
    st.markdown("""
        <div class="footer">
            <p>Powered by <a href="https://www.themoviedb.org/" target="_blank">TMDb</a></p>
        </div>
    """, unsafe_allow_html=True)

# Advanced CSS for styling, animations, and responsiveness
st.markdown("""
    <style>
        /* Background Netflix-style */
        .css-1aumxhk {
            background: #141414;
            color: #e5e5e5;
        }
        
        /* Fade-in and Gradient Animation */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes gradientGlow {
            0%, 100% { color: #E50914; }
            50% { color: #b20710; }
        }
        
        /* Movie Card */
        .movie-card {
            text-align: center;
            background-color: #1f1f1f;
            padding: 15px;
            border-radius: 15px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            width: 100%;
        }
        
        /* Movie Poster Image */
        .movie-poster {
            width: 100%;
            border-radius: 10px;
            transition: transform 0.3s ease;
        }

        /* Movie Card Hover Effect */
        .movie-card:hover {
            transform: scale(1.05);
            box-shadow: 0px 12px 24px rgba(255, 0, 0, 0.5);
        }

        /* Text Styling in Movie Card */
        .movie-card h4 {
            color: #e5e5e5;
            font-weight: bold;
            margin: 10px 0;
            font-size: 1rem;
            transition: color 0.3s ease;
        }
        
        .movie-card:hover h4 {
            color: #ff4b4b;
        }
        
        /* Footer Style */
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #e5e5e5;
            margin-top: 20px;
        }
        
        /* Footer Link Style */
        .footer a {
            color: #E50914;
            text-decoration: none;
            font-weight: bold;
        }

        /* Button Styling */
        .stButton button {
            background-color: #E50914;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 1.1rem;
            font-weight: bold;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .stButton button:hover {
            background-color: #b20710;
            transform: scale(1.05);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .movie-card h4 {
                font-size: 0.9rem;
            }
            .movie-card {
                margin-bottom: 20px;
                padding: 10px;
            }
            .movie-poster {
                width: 80%;
            }
            .stButton button {
                font-size: 0.9rem;
                padding: 8px 16px;
            }
            h1 {
                font-size: 2.2rem;
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 1.8rem;
            }
            .footer {
                font-size: 0.8rem;
            }
        }
    </style>
""", unsafe_allow_html=True)
