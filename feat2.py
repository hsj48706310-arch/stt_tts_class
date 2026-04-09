import streamlit as st
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from gtts import gTTS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize TTS engine
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("말씀하세요...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            return text
        except sr.UnknownValueError:
            return "음성을 인식하지 못했습니다."
        except sr.RequestError:
            return "음성 인식 서비스에 문제가 있습니다."

# Function to refine text with LLM
def refine_text(input_text, style):
    if style == "감성 가득한 시인 버전":
        prompt = f"다음 고백을 감성적이고 시적인 언어로 다듬어주세요: {input_text}"
    elif style == "박력있는 사투리 버전":
        prompt = f"다음 고백을 박력있는 사투리로 다듬어주세요: {input_text}"
    elif style == "깔끔한 직장인 버전":
        prompt = f"다음 고백을 깔끔하고 직장인다운 언어로 다듬어주세요: {input_text}"
    else:
        prompt = f"다음 고백을 다듬어주세요: {input_text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

# Function to speak text with TTS
def speak_text(text, voice_id=None):
    if voice_id is not None:
        # Use pyttsx3 for local voices
        voices = engine.getProperty('voices')
        if voice_id < len(voices):
            engine.setProperty('voice', voices[voice_id].id)
        engine.say(text)
        engine.runAndWait()
    else:
        # Use gTTS for default
        tts = gTTS(text=text, lang='ko')
        tts.save("temp_audio.mp3")
        os.system("start temp_audio.mp3")  # Windows에서 기본 플레이어로 재생

# Streamlit app
st.title("💗오글거리는 고백 교정기💌💕")

# Input method
input_method = st.radio("입력 방법 선택", ("텍스트", "음성"))

input_text = ""
if input_method == "텍스트":
    input_text = st.text_input("고백을 입력하세요:")
elif input_method == "음성":
    if st.button("음성 입력 시작"):
        input_text = recognize_speech()
        st.write(f"인식된 텍스트: {input_text}")

if input_text:
    # Style selection
    style = st.selectbox("스타일 선택", ["감성 가득한 시인 버전", "박력있는 사투리 버전", "깔끔한 직장인 버전"])

    if st.button("교정하기"):
        refined_text = refine_text(input_text, style)
        st.session_state['refined_text'] = refined_text
        st.session_state['style'] = style

    # Display refined text if available
    if 'refined_text' in st.session_state:
        st.write(f"교정된 텍스트: {st.session_state['refined_text']}")

        # TTS options
        voices = engine.getProperty('voices')
        voice_options = [f"Voice {i}: {voice.name}" for i, voice in enumerate(voices)]
        selected_voice = st.selectbox("목소리 선택", voice_options)

        if st.button("듣기"):
            voice_id = voice_options.index(selected_voice)
            speak_text(st.session_state['refined_text'], voice_id)