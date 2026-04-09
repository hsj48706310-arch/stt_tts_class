import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말씀하세요... (10초 녹음)")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="ko-KR")
            return text
        except sr.WaitTimeoutError:
            return "시간 초과: 음성이 감지되지 않았습니다."
        except sr.UnknownValueError:
            return "음성을 인식할 수 없습니다."
        except sr.RequestError:
            return "Google API에 접근할 수 없습니다."