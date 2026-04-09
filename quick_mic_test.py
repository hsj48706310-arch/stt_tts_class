"""
빠른 마이크 테스트 스크립트
"""

import speech_recognition as sr

print("\n=== 마이크 간단 테스트 ===\n")

try:
    # 마이크 목록
    print("사용 가능한 마이크:")
    for i, mic_name in enumerate(sr.Microphone.list_microphone_indexes()):
        print(f"  {i}: 마이크 #{i}")
    
    print("\n기본 마이크로 5초간 녹음 중...")
    print("(말을 해주세요)")
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    
    print("\n Google API로 인식 중...")
    
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        print(f"\n✓ 인식 성공: '{text}'")
    except sr.UnknownValueError:
        print("\n⚠️  음성을 인식할 수 없습니다.")
        print("    더 큰 목소리로 다시 시도하세요.")
    except sr.RequestError as e:
        print(f"\n✗ Google API 오류: {e}")
        print("   인터넷 연결 또는 API 접근성을 확인하세요.")

except Exception as e:
    print(f"\n✗ 오류: {e}")
    print("\n마이크가 연결되어 있는지 확인하세요.")
