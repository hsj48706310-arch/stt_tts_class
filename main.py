import streamlit as st
from llm import refine_text
from tts import text_to_speech
from stt import speech_to_text

# 페이지 설정
st.set_page_config(page_title="고백 교정기", page_icon="💌", layout="centered")

# CSS for beige theme
st.markdown("""
<style>
    .main {
        background-color: #f5f5dc;
    }
    .stButton>button {
        background-color: #d2b48c;
        color: white;
        border-radius: 10px;
    }
    .stTextInput, .stTextArea {
        background-color: #faf0e6;
    }
    .stRadio > div {
        background-color: #faf0e6;
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("💌 고백 교정기")
st.markdown("대충 쓴 진심을 감성적으로 다듬어드려요!")

# 입력 방식 선택
input_method = st.radio("입력 방식 선택", ("텍스트 입력", "음성 입력"))

user_text = ""
if input_method == "텍스트 입력":
    user_text = st.text_area("진심을 입력하세요", placeholder="예: 나 너 좋아하나는데 사귈래?")
elif input_method == "음성 입력":
    if st.button("🎤 음성 입력 시작"):
        user_text = speech_to_text()
        st.write(f"인식된 텍스트: {user_text}")

# 스타일 선택
style = st.radio("다듬기 스타일", ("감성 가득한 시인 버전", "깔끔한 직장인 버전"))

if st.button("✨ 다듬기"):
    if user_text:
        style_key = "poetic" if style == "감성 가득한 시인 버전" else "professional"
        refined = refine_text(user_text, style_key)
        st.session_state.refined_text = refined
        st.success("다듬기 완료!")
        st.text_area("다듬은 편지", value=refined, height=150)
    else:
        st.error("텍스트를 입력하세요.")

# TTS
if "refined_text" in st.session_state:
    voice_type = st.radio("목소리 선택", ("감미로운 목소리", "캐릭터 목소리"))
    # 톤 선택 버튼
    st.markdown("### 톤 선택")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("💕 부드럽게"):
            st.session_state.tone = "soft"
    with col2:
        if st.button("😎 담백하게"):
            st.session_state.tone = "casual"
    with col3:
        if st.button("🔥 직진"):
            st.session_state.tone = "direct"
    with col4:
        if st.button("😢 애절하게"):
            st.session_state.tone = "sad"
    
    # 선택된 톤 표시
    if "tone" in st.session_state:
        st.write(f"선택된 톤: {st.session_state.tone}")
    
    if st.button("🔊 듣기"):
        voice_key = "sweet" if voice_type == "감미로운 목소리" else "character"
        # 톤에 따른 파라미터 설정
        tone_params = {
            "soft": {"rate": -20, "pitch": -10, "volume": 0.8},
            "casual": {"rate": 0, "pitch": 0, "volume": 1.0},
            "direct": {"rate": 20, "pitch": 10, "volume": 1.0},
            "sad": {"rate": -30, "pitch": -20, "volume": 0.7}
        }
        params = tone_params.get(st.session_state.get("tone", "casual"), tone_params["casual"])
        text_to_speech(st.session_state.refined_text, voice_key, **params)
