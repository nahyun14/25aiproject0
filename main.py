import streamlit as st
import requests

# TMDB API 키 설정
TMDB_API_KEY = 'YOUR_TMDB_API_KEY'  # TMDB API 키를 입력하세요

# MBTI별 추천 영화 목록
mbti_movies = {
    "INTJ": ["Inception", "Interstellar", "The Matrix"],
    "INTP": ["The Imitation Game", "A Beautiful Mind", "The Prestige"],
    "ENTJ": ["The Wolf of Wall Street", "Gladiator", "The Godfather"],
    "ENTP": ["The Social Network", "The Big Short", "The Pursuit of Happyness"],
    "INFJ": ["The Shawshank Redemption", "Forrest Gump", "The Green Mile"],
    "INFP": ["Dead Poets Society", "Into the Wild", "The Secret Life of Walter Mitty"],
    "ENFJ": ["The Pursuit of Happyness", "The Blind Side", "A Beautiful Mind"],
    "ENFP": ["The Secret Life of Walter Mitty", "Good Will Hunting", "The Truman Show"],
    "ISTJ": ["The Godfather", "12 Angry Men", "The Shawshank Redemption"],
    "ISFJ": ["The Sound of Music", "The Blind Side", "The Pursuit of Happyness"],
    "ESTJ": ["Gladiator", "The Godfather", "The Dark Knight"],
    "ESFJ": ["The Blind Side", "The Pursuit of Happyness", "The Help"],
    "ISTP": ["Mad Max: Fury Road", "Die Hard", "The Dark Knight"],
    "ISFP": ["Into the Wild", "The Secret Life of Walter Mitty", "Dead Poets Society"],
    "ESTP": ["The Dark Knight", "Mad Max: Fury Road", "Die Hard"],
    "ESFP": ["The Pursuit of Happyness", "The Blind Side", "The Help"]
}

# 영화 포스터 URL 가져오기
def get_movie_poster(movie_name):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}'
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    else:
        return None

# Streamlit 앱 구성
st.title("🎬 MBTI별 영화 추천")
st.write("당신의 MBTI 유형을 입력하면 어울리는 영화를 추천해드려요!")

mbti_input = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)").upper()

if mbti_input in mbti_movies:
    st.subheader(f"추천 영화 ({mbti_input}):")
    for movie in mbti_movies[mbti_input]:
        st.write(f"- {movie}")
        poster_url = get_movie_poster(movie)
        if poster_url:
            st.image(poster_url, width=200)
else:
    st.error("유효한 MBTI 유형을 입력해주세요 (예: INFP, ENTJ 등)")
