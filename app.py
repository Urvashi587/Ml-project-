import streamlit as st
import pickle
import pandas as pd
import requests
def get_poster(mov_id):
    res=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0550740926dfd9476ff1a70b9f597b4a&language=en-US'.format(mov_id))
    data=res.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
similar=pickle.load(open('similar.pkl','rb'))
def recommend(movie):
    ind = mov[mov['title'] == movie].index[0]
    distances = similar[ind]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    posters=[]
    for i in similar_movies:
        recommended_movies.append(mov.iloc[i[0]].title)
        posters.append(get_poster(mov.iloc[i[0]].id))
    return recommended_movies,posters
mov_dict=pickle.load(open('movie.pkl','rb'))
mov=pd.DataFrame(mov_dict)
st.title('Movie Recommender')
movie_selected=st.selectbox('Select a movie',mov['title'].values)
if st.button('Recommend'):
    names,posters=recommend(movie_selected)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
