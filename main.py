import streamlit as st
import time

# 👉 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼", layout="centered")

# 🎨 CSS 스타일링
st.markdown(
    """
    <style>
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #6C63FF;
            text-align: center;
        }
        .job-box {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎉 제목
st.markdown('<div class="title">💼 MBTI 직업 추천기</div>', unsafe_allow_html=True)
st.markdown("### 당신의 성격에 어울리는 직업은? 😎")

# ✅ MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 과학자", "🛠 시스템 설계자"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "📈 기술 분석가"],
    "ENTJ": ["📣 경영 컨설턴트", "📋 기획자", "🏢 기업가"],
    "ENTP": ["📢 마케팅 디렉터", "⚡ 혁신 매니저", "🚀 벤처 창업자"],
    "INFJ": ["🧘 상담사", "✍️ 작가", "🧑‍⚕️ 심리학자"],
    "INFP": ["🎨 예술가", "🖋 카피라이터", "🕊 인권 활동가"],
    "ENFJ": ["👥 HR 매니저", "📚 교육자", "🧑‍🏫 코치"],
    "ENFP": ["🎤 광고기획자", "📱 콘텐츠 크리에이터", "🎙 강연자"],
    "ISTJ": ["🧾 회계사", "⚖️ 법률가", "🏛 공무원"],
    "ISFJ": ["👩‍⚕️ 간호사", "🤝 사회복지사", "👩‍🏫 교사"],
    "ESTJ": ["🧑‍💼 경영 관리자", "📁 프로젝트 매니저", "🪖 군 간부"],
    "ESFJ": ["💁 서비스 매니저", "🎉 이벤트 코디네이터", "📞 고객 상담사"],
    "ISTP": ["🔧 엔지니어", "✈️ 파일럿", "🛠 기술자"],
    "ISFP": ["🎨 디자이너", "🌳 조경사", "📸 사진작가"],
    "ESTP": ["💼 세일즈 매니저", "🏅 스포츠 선수", "🤝 비즈니스 디벨로퍼"],
    "ESFP": ["🎤 MC/사회자", "🎬 연예인", "🌍 여행 가이드"]
}

# 📝 사용자 입력
mbti_input = st.text_input("🔤 당신의 MBTI를 입력하세요 (예: INFP)", max_chars=4).upper()

# 🎯 결과 출력
if mbti_input:
    with st.spinner("🔍 당신에게 어울리는 직업을 찾고 있어요..."):
        time.sleep(1.5)

    if mbti_input in mbti_jobs:
        st.success(f"🎯 {mbti_input} 유형에게 어울리는 직업 추천!")
        st.markdown('<div class="job-box">', unsafe_allow_html=True)
        for job in mbti_jobs[mbti_input]:
            st.markdown(f"✅ {job}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("🚫 올바른 MBTI 유형을 입력해주세요 (예: INFP, ESTJ 등)")
