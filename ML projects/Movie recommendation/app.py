import pickle
import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open('Untitled.jpg')
st.image(image,caption='Darun Movies')


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
         recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies For You')

selected_movie_name = st.selectbox(
"Select you favorite movies",
movies['title'].values)

if st.button('Recommendations'):
    recommendations =recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)






