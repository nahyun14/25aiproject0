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
    "INFJ": [
        {"title": "Her", "summary": "AI와의 사랑 속에서 자아를 찾는 남자의 이야기 💌"},
        {"title": "The Green Mile", "summary": "기적과 감동이 있는 감방 안의 특별한 이야기 ✨"},
        {"title": "Life of Pi", "summary": "믿음과 희망이 담긴 동화 같은 여정 🐅"}
    ],
    "INTP": [
        {"title": "The Imitation Game", "summary": "암호를 풀고 전쟁을 바꾼 천재의 이야기 🧠"},
        {"title": "A Beautiful Mind", "summary": "수학적 천재의 삶과 내면의 싸움 📐"},
        {"title": "The Social Network", "summary": "페이스북의 시작, 천재들의 충돌 ⚡"}
    ],
    "INTJ": [
        {"title": "Inception", "summary": "꿈을 조작하는 스릴 넘치는 작전 🌀"},
        {"title": "Interstellar", "summary": "시간과 우주의 경계를 넘는 여정 🚀"},
        {"title": "The Matrix", "summary": "가상 현실과 진짜 세계의 경계 🤖"}
    ],
    "ENFP": [
        {"title": "The Truman Show", "summary": "쇼 속에 살던 남자의 자각과 탈출 이야기 🎭"},
        {"title": "Good Will Hunting", "summary": "천재의 마음을 여는 따뜻한 우정 💞"},
        {"title": "The Secret Life of Walter Mitty", "summary": "상상에서 현실로, 모험을 떠나는 이야기 🌄"}
    ],
    "ENFJ": [
        {"title": "The Pursuit of Happyness", "summary": "고난을 이겨내는 아빠와 아들의 눈물 나는 여정 👨‍👦"},
        {"title": "The Blind Side", "summary": "사랑과 관심으로 변화된 청년의 이야기 🏈"},
        {"title": "Freedom Writers", "summary": "학생들의 삶을 바꾼 선생님의 감동 실화 ✏️"}
    ],
    "ENTP": [
        {"title": "The Big Short", "summary": "금융 위기를 예측한 괴짜들의 반란 💸"},
        {"title": "Catch Me If You Can", "summary": "사기꾼과 FBI의 두뇌 싸움 ✈️"},
        {"title": "Iron Man", "summary": "천재 발명가의 슈퍼히어로 탄생기 ⚙️"}
    ],
    "ENTJ": [
        {"title": "The Wolf of Wall Street", "summary": "끝없는 야망과 성공을 향한 질주 💼"},
        {"title": "Gladiator", "summary": "복수를 위한 로마 검투사의 전설 🗡️"},
        {"title": "The Godfather", "summary": "가문의 명예를 지키는 권력의 이야기 👑"}
    ],
    "ISFP": [
        {"title": "Amélie", "summary": "작지만 따뜻한 기적을 일으키는 소녀의 이야기 🌸"},
        {"title": "La La Land", "summary": "꿈과 사랑 사이에서 선택하는 예술가들 🎹"},
        {"title": "Call Me by Your Name", "summary": "한여름의 낭만적인 첫사랑 🌞"}
    ],
    "ISFJ": [
        {"title": "The Help", "summary": "용기 있게 목소리를 낸 여성들의 이야기 👒"},
        {"title": "Little Women", "summary": "자매들의 꿈과 사랑이 담긴 고전적 이야기 📝"},
        {"title": "Wonder", "summary": "다름을 존중하는 아름다운 이야기 🌟"}
    ],
    "ISTP": [
        {"title": "Mad Max: Fury Road", "summary": "광기와 액션이 넘치는 황무지 탈출 🚗"},
        {"title": "The Dark Knight", "summary": "혼돈 속에서 정의를 외치는 배트맨 🦇"},
        {"title": "Tenet", "summary": "시간을 거꾸로 가는 두뇌 폭발 액션 ⏳"}
    ],
    "ISTJ": [
        {"title": "12 Angry Men", "summary": "한 사람의 신념이 판결을 바꾸는 이야기 ⚖️"},
        {"title": "Bridge of Spies", "summary": "냉전 시대, 정보전의 숨겨진 이야기 🕵️‍♂️"},
        {"title": "The King's Speech", "summary": "말더듬이를 극복한 왕의 성장 🗣️"}
    ],
    "ESFP": [
        {"title": "The Greatest Showman", "summary": "화려한 쇼맨십과 음악의 세계 🎤"},
        {"title": "Pitch Perfect", "summary": "아카펠라 여신들의 대결 🎶"},
        {"title": "Legally Blonde", "summary": "핑크와 열정으로 세상을 바꾼 그녀 💅"}
    ],
    "ESFJ": [
        {"title": "The Blind Side", "summary": "따뜻한 가족애와 성공 이야기 🏈"},
        {"title": "Julie & Julia", "summary": "요리로 이어지는 두 여성의 열정 🍳"},
        {"title": "Mamma Mia!", "summary": "음악과 사랑이 가득한 그리스 여행 🎶"}
    ],
    "ESTP": [
        {"title": "Fast & Furious", "summary": "스피드와 가족애가 넘치는 액션 레이싱 🚘"},
        {"title": "Now You See Me", "summary": "마법 같은 도둑들의 쇼 🎩"},
        {"title": "Mission: Impossible", "summary": "불가능은 없다! 💥"}
    ],
    "ESTJ": [
        {"title": "The Post", "summary": "정의로운 언론의 힘을 보여주는 실화 📰"},
        {"title": "Moneyball", "summary": "데이터로 야구의 판을 바꾸다 ⚾"},
        {"title": "Erin Brockovich", "summary": "진실을 파헤친 평범한 여성의 용기 ⚖️"}
    ]
}

    # 나머지 MBTI들도 필요하시면 추가해 드릴게요!


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
