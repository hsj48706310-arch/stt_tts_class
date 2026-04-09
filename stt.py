import speech_recognition as sr
import streamlit as st
from typing import Tuple

def check_microphone_available() -> Tuple[bool, str]:
    """마이크 사용 가능 여부 확인"""
    try:
        with sr.Microphone() as source:
            return True, "마이크가 연결되어 있습니다."
    except Exception as e:
        return False, f"마이크 오류: {str(e)}"

def speech_to_text(language: str = "ko-KR", timeout: int = 10) -> str:
    """
    음성을 텍스트로 변환
    
    Args:
        language: 인식 언어 (기본값: 한국어)
        timeout: 인식 시간 제한 (초)
    
    Returns:
        인식된 텍스트 또는 에러 메시지
    """
    try:
        # 마이크 확인
        mic_available, mic_msg = check_microphone_available()
        if not mic_available:
            return mic_msg
        
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 4000  # 주변음 필터링
        
        with sr.Microphone() as source:
            st.info("🎤 말씀하세요... (최대 10초)")
            
            # 배경음 조정
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # 음성 수집
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=timeout)
        
        st.info("🔄 음성 인식 중...")
        
        # Google API로 인식
        try:
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "❌ 음성을 인식할 수 없습니다. 다시 시도해주세요."
        except sr.RequestError as e:
            return f"❌ Google API 오류: {str(e)}\n인터넷 연결 또는 API 접근성을 확인하세요."
            
    except sr.MicrophoneError as e:
        return f"❌ 마이크 오류: {str(e)}\n마이크가 연결되어 있는지 확인하세요."
    except Exception as e:
        return f"❌ 예상치 못한 오류: {str(e)}"
