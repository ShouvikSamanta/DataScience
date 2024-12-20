import pickle

import streamlit as st
import pandas as pd
import requests



similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
#Fetch Poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

#recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movie_posters =[]
    for i in movie_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_movie_posters


st.title('Movie Recommendor System')

Selected_movie_name = st.selectbox('What do you want to watch ?',
movies['title'].values
)


if st.button('Show Recommendation'):
    recommended_movies,recommended_movie_posters = recommend(Selected_movie_name)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movies[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movies[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movies[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movies[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.text(recommended_movies[9])
        st.image(recommended_movie_posters[9])