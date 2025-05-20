import streamlit as st
import requests

# 🐰 TMDB API 키 설정 (https://www.themoviedb.org/에서 발급받으세요)
TMDB_API_KEY = 'YOUR_TMDB_API_KEY'

# 🐣 MBTI별 추천 영화 목록과 간단한 내용 요약
mbti_movies = {
    "INTJ": [
        {"title": "Inception", "summary": "꿈 속의 꿈을 통해 현실을 조작하는 기술자들의 이야기입니다."},
        {"title": "Interstellar", "summary": "인류의 생존을 위해 우주를 여행하는 과학자들의 모험을 그린 작품입니다."},
        {"title": "The Matrix", "summary": "가상 현실과 현실의 경계를 넘나드는 액션 SF 영화입니다."}
    ],
    "INFP": [
        {"title": "Dead Poets Society", "summary": "자유로운 사고와 창의성을 강조하는 교사의 이야기를 담고 있습니다."},
        {"title": "Into the Wild", "summary": "자연 속에서 진정한 자유를 찾으려는 청년의 여정을 그린 작품입니다."},
        {"title": "The Secret Life of Walter Mitty", "summary": "평범한 직장인이 상상 속 모험을 통해 성장하는 이야기를 담고 있습니다."}
    ]
    # 🐾 다른 MBTI 유형에 대한 영화 목록과 요약도 추가해주세요!
}

# 🐇 영화 포스터 URL 가져오기
def get_movie_poster(movie_name):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}'
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    else:
        return None

# 🐣 Streamlit 앱 구성
st.title("🎬 MBTI별 영화 추천기 🐰")
st.write("당신의 MBTI를 입력하면 어울리는 영화를 추천해드려요! 💖")

mbti_input = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)").upper()

if mbti_input in mbti_movies:
    st.subheader(f"추천 영화 ({mbti_input}):")
    for movie in mbti_movies[mbti_input]:
        st.write(f"🎥 **{movie['title']}**")
        st.write(f"📖 요약: {movie['summary']}")
        poster_url = get_movie_poster(movie['title'])
        if poster_url:
            st.image(poster_url, width=200)
else:
    st.error("유효한 MBTI 유형을 입력해주세요 (예: INFP, ENTJ 등) 🐾")
