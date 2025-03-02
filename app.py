


import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ea03f76e9ab1ab1efd2c838d7cf6fe69&language=en-US')
    data=response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    
    
    

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #Here we are trying to fetch movie poster based on recommended movie Id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
    

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

#
st.title('Content Based Recommender System by Ashish Verma')

selected_movie_name = st.selectbox('Select a movie you like', movies['title'].values)

if st.button('Show Recommendations'):
    if selected_movie_name:
        name, posters = recommend(selected_movie_name)
        
        num_recommendations = len(name)
        columns = st.columns(num_recommendations)
        
        for i, col in enumerate(columns):
            col.text(name[i])
            col.image(posters[i])
