import streamlit as st
from llm import refine_and_analyze
from tts_improved import text_to_speech
from stt_improved import speech_to_text

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

# 세션 상태 초기화
if "user_text" not in st.session_state:
    st.session_state.user_text = ""

st.title("💌 고백 교정기")
st.markdown("대충 쓴 진심을 감성적으로 다듬어드려요!")

# 입력 방식 선택
input_method = st.radio("입력 방식 선택", ("텍스트 입력", "음성 입력"))

if input_method == "텍스트 입력":
    st.session_state.user_text = st.text_area(
        "진심을 입력하세요", 
        value=st.session_state.get("user_text", ""), 
        placeholder="예: 나 너 좋아하나는데 사귈래?"
    )
elif input_method == "음성 입력":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("🎤 마이크 입력을 사용하려면 시작 버튼을 누르세요")
    with col2:
        if st.button("🎤 시작"):
            recognized_text = speech_to_text()
            
            if recognized_text and not recognized_text.startswith("❌"):
                st.session_state.user_text = recognized_text
                st.success(f"✅ 인식된 텍스트: {recognized_text}")
            else:
                st.error(recognized_text)
                st.info("""
                **마이크 문제 해결 방법:**
                1. 마이크가 제대로 연결되어 있는지 확인하세요
                2. 윈도우 사운드 설정에서 마이크 활성화 확인
                3. 방화벽/백신이 마이크 접근을 차단하지 않는지 확인
                4. 브라우저 또는 Python 마이크 권한 확인
                
                **진단 방법:**
                터미널에서 `python audio_diagnostic.py` 실행
                """)

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
        st.success("✅ 다듬기 완료!")
    else:
        st.error("❌ 텍스트를 입력하세요.")

if "refined_text" in st.session_state:
    st.subheader("💌 교정된 고백")
    st.write(st.session_state.refined_text)
    
    st.subheader("❤️ AI 성공 확률")
    st.write(st.session_state.probability)
    
    st.subheader("📊 AI 피드백")
    st.write(st.session_state.reason)

    # TTS
    voice_type = st.radio("목소리 선택", ("여성 목소리", "남성 목소리"))
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("음성으로 들어보세요")
    with col2:
        if st.button("🔊 재생"):
            voice_key = "sweet" if voice_type == "여성 목소리" else "character"
            try:
                audio_data = text_to_speech(st.session_state.refined_text, voice_key)
                st.audio(audio_data, format="audio/mp3")
            except Exception as e:
                st.error(f"음성 생성 오류: {str(e)}")

# 하단 정보
with st.expander("🔧 문제 해결 가이드"):
    st.markdown("""
    ### 음성 입력이 안 될 때:
    - **마이크 확인**: 마이크가 정상 작동하는지 확인
    - **인터넷 연결**: Google Speech API 사용으로 인터넷 필수
    - **방화벽**: 방화벽/백신이 마이크 접근 차단 여부 확인
    - **권한**: 브라우저/앱에 마이크 접근 권한 부여 확인
    
    ### 음성 출력이 안 될 때:
    - **스피커 확인**: 스피커/헤드폰 연결 확인
    - **볼륨 확인**: 시스템/앱 볼륨 확인
    - **출력 장치**: 윈도우 사운드 설정에서 기본 재생 장치 확인
    
    ### 진단 실행:
    터미널에서 다음 명령어 실행:
    ```bash
    python audio_diagnostic.py
    ```
    
    시스템의 마이크, 스피커, API 연결 상태를 완전히 진단합니다.
    """)
