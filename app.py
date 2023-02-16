import pickle
import pandas as pd
import streamlit as st


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = csmx[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommender_movies = []
    for i in movies_list:
        recommender_movies.append(movies.iloc[i[0]].title)
    return recommender_movies

#list of movies
movies_dict = pickle.load(open('model.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

csmx = pickle.load(open('csmx.pkl', 'rb'))

st.title('Movies Recommendation System')

sel_movie = st.selectbox(
    'Enter a Movie Name',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(sel_movie)
    for i in recommendations:
        st.write(i)
