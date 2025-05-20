import streamlit as st
import requests

# 🔑 TMDB API 키 입력 (본인의 키로 바꿔주세요!)
TMDB_API_KEY = "YOUR_TMDB_API_KEY"

# 🎬 MBTI별 영화 추천 데이터
mbti_movies = {
    "INFP": [
        {"title": "Dead Poets Society", "summary": "자유롭게 생각하고 꿈꾸는 청춘들의 이야기 📚"},
        {"title": "The Secret Life of Walter Mitty", "summary": "상상만 하던 모험을 현실로 바꾸는 이야기 🌍"},
        {"title": "Into the Wild", "summary": "자연에서 자유를 찾는 청년의 감동 실화 🏕️"}
    ],
    "INTJ": [
        {"title": "Inception", "summary": "꿈을 조작하는 스릴 넘치는 작전 🌀"},
        {"title": "Interstellar", "summary": "시간과 우주의 경계를 넘는 여정 🚀"},
        {"title": "The Matrix", "summary": "가상 현실과 진짜 세계의 경계 🤖"}
    ],
    "INFJ": [
        {"title": "Her", "summary": "AI와의 사랑 속에서 자아를 찾는 남자의 이야기 💌"},
        {"title": "The Green Mile", "summary": "기적과 감동이 있는 감방 안의 특별한 이야기 ✨"},
        {"title": "Life of Pi", "summary": "믿음과 희망이 담긴 동화 같은 여정 🐅"}
    ],
    # 나머지 MBTI들도 필요하시면 추가해 드릴게요!
}

# 🔍 영화 정보 검색 함수
def get_movie_data(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": title}
    res = requests.get(url, params=params)
    if res.status_code == 200:
        results = res.json().get("results")
        if results:
            movie = results[0]
            poster = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get("poster_path") else None
            overview = movie.get("overview", "줄거리를 찾을 수 없어요 😥")
            return poster, overview
    return None, "정보를 찾을 수 없어요 😢"

# 🌈 Streamlit 앱 설정
st.set_page_config(page_title="MBTI 영화 추천기", page_icon="🎬")
st.title("🎬 MBTI 유형별 영화 추천기 🐰✨")
st.markdown("MBTI를 입력하면 나랑 어울리는 영화를 귀엽게 추천해줄게요! 💖")

# 💬 사용자 입력 받기
mbti = st.text_input("💌 MBTI를 입력해주세요 (예: INFP)").upper()

# 🎁 결과 출력
if mbti:
    if mbti in mbti_movies:
        st.subheader(f"✨ {mbti} 유형에게 어울리는 영화예요! 🍿")
        for movie in mbti_movies[mbti]:
            st.markdown(f"**🎥 {movie['title']}**")
            st.markdown(f"📝 줄거리 요약: {movie['summary']}")
            poster, overview = get_movie_data(movie['title'])
            if poster:
                st.image(poster, width=300)
            st.markdown(f"📖 TMDB 설명: _{overview}_")
            st.markdown("---")
    else:
        st.error("😥 아직 준비되지 않은 MBTI 유형이에요! INFP, INTJ, INFJ만 현재 사용 가능해요.")
