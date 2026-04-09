import streamlit as st
from llm import refine_and_analyze
from tts import text_to_speech
from stt import speech_to_text

# 페이지 설정
st.set_page_config(page_title="고백 교정기", page_icon="💌", layout="centered")

# CSS for pink love theme
st.markdown("""
<style>
    html, body, .main, .block-container, .css-1d391kg, .css-1d391kg .main, .stApp {
        background-color: #ffe4ec !important;
    }
    .css-1y4p8pa.egzxvld3 {
        background-color: #ffe4ec !important;
    }
    .css-18ni7ap.e8zbici2 {
        background-color: transparent !important;
    }
    .stButton>button {
        background-color: #ff7bac;
        color: white;
        border-radius: 10px;
    }
    .stTextInput, .stTextArea {
        background-color: #fff0f6 !important;
    }
    .stRadio > div, .stSelectbox > div, .stMultiSelect > div {
        background-color: #fff0f6 !important;
        padding: 10px;
        border-radius: 10px;
    }
    .css-1q8dd3e.e16nr0p30 {
        background-color: #ffe4ec !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("💌 고백 교정기")
st.markdown("대충 쓴 진심을 감성적으로 다듬어드려요!")

# 입력 방식 선택
input_method = st.radio("입력 방식 선택", ("텍스트 입력", "음성 입력"))

if input_method == "텍스트 입력":
    st.session_state.user_text = st.text_area("진심을 입력하세요", value=st.session_state.get("user_text", ""), placeholder="예: 나 너 좋아하나는데 사귈래?")
elif input_method == "음성 입력":
    if st.button("🎤 음성 입력 시작"):
        with st.spinner("음성 인식 중... (최대 5초)"):
            recognized_text = speech_to_text()
        st.session_state.user_text = recognized_text
        st.write(f"인식된 텍스트: {recognized_text}")

# 스타일 선택
style = st.radio("다듬기 스타일", ("감성 가득한 시인 버전", "깔끔한 직장인 버전"))

# 분위기 선택
mood = st.radio("분위기 선택", ("로맨틱", "코믹", "진지", "귀엽게", "중립"))

if st.button("✨ 다듬기"):
    user_text = st.session_state.get("user_text", "")
    if user_text:
        style_key = "poetic" if style == "감성 가득한 시인 버전" else "professional"
        mood_options = {"로맨틱": "romantic", "코믹": "comic", "진지": "serious", "귀엽게": "cute", "중립": "neutral"}
        mood_key = mood_options[mood]
        result = refine_and_analyze(user_text, style_key, mood_key)
        st.session_state.refined_text = result['message']
        st.session_state.probability = result['probability']
        st.session_state.reason = result['reason']
        st.success("다듬기 완료!")
    else:
        st.error("텍스트를 입력하세요.")

if "refined_text" in st.session_state:
    st.subheader("💌 교정된 고백")
    st.write(st.session_state.refined_text)
    
    st.subheader("❤️ AI 성공 확률")
    st.write(st.session_state.probability)
    
    st.subheader("📊 AI 피드백")
    st.write(st.session_state.reason)

    # TTS
    voice_type = st.radio("목소리 선택", ("여성 목소리", "남성 목소리"))
    if st.button("🔊 듣기"):
        voice_key = "sweet" if voice_type == "여성 목소리" else "character"
        audio_data = text_to_speech(st.session_state.refined_text, voice_key)
        st.audio(audio_data, format="audio/mp3")
