"""
오디오 진단 스크립트
음성 입력/출력 문제를 진단하기 위한 도구
"""

import sys
import speech_recognition as sr
import pygame
import asyncio
import edge_tts
import io

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def check_microphone():
    """마이크 상태 확인"""
    print_section("마이크 진단")
    
    try:
        # 사용 가능한 마이크 확인
        print("사용 가능한 마이크:")
        mic_list = sr.Microphone.list_microphone_indexes()
        if not mic_list:
            print("  ❌ 감지된 마이크가 없습니다.")
            return False
        
        for index in mic_list:
            print(f"  ✓ 마이크 #{index}")
        
        # 기본 마이크 테스트
        print("\n기본 마이크 테스트 중...")
        with sr.Microphone() as source:
            print("  ✓ 마이크 연결됨")
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("  ✓ 주변음 조정 완료")
        
        return True
    except Exception as e:
        print(f"  ❌ 마이크 오류: {e}")
        return False

def check_speaker():
    """스피커/오디오 출력 확인"""
    print_section("스피커 진단")
    
    try:
        # pygame 초기화
        print("pygame 초기화 중...")
        pygame.mixer.init()
        print("  ✓ pygame mixer 정상")
        
        # 더미 오디오로 테스트
        print("스피커 테스트 신호 재생 중...")
        sample_rate = 22050
        duration = 1  # 1초
        frequency = 440  # A4 음
        
        import numpy as np
        frames = int(duration * sample_rate)
        arr = np.sin(2.0 * np.pi * frequency * np.linspace(0, duration, frames)).astype(np.float32)
        
        sound = pygame.sndarray.make_sound((arr * 32767).astype(np.int16))
        sound.play()
        pygame.time.wait(int(duration * 1000))
        print("  ✓ 스피커 테스트 완료")
        
        pygame.mixer.quit()
        return True
    except ImportError:
        print("  ⚠️  numpy 미설치 - 간단한 테스트만 진행")
        try:
            pygame.mixer.init()
            print("  ✓ pygame mixer 정상")
            pygame.mixer.quit()
            return True
        except Exception as e:
            print(f"  ❌ 오디오 출력 오류: {e}")
            return False
    except Exception as e:
        print(f"  ❌ 스피커 오류: {e}")
        return False

def check_google_api():
    """Google Speech Recognition API 확인"""
    print_section("Google API 연결 확인")
    
    try:
        print("인터넷 연결 테스트 중...")
        recognizer = sr.Recognizer()
        
        # 더미 오디오로 API 접근 테스트
        with sr.Microphone() as source:
            print("  짧은 음성 녹음 중... (3초)")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
        
        print("  Google API 요청 중...")
        try:
            text = recognizer.recognize_google(audio, language="ko-KR")
            print(f"  ✓ API 정상: '{text}'")
            return True
        except sr.UnknownValueError:
            print("  ✓ API 정상 (음성 인식 실패 - 정상 범위)")
            return True
        except sr.RequestError as e:
            print(f"  ❌ API 오류: {e}")
            print("     - 인터넷 연결 확인")
            print("     - 방화벽/프록시 설정 확인")
            return False
    except Exception as e:
        print(f"  ❌ 오류: {e}")
        return False

async def check_edge_tts():
    """Edge TTS 서비스 확인"""
    print_section("Edge TTS 진단")
    
    try:
        test_text = "안녕하세요"
        print(f"테스트 텍스트 합성 중: '{test_text}'")
        
        communicate = edge_tts.Communicate(
            test_text, 
            "ko-KR-SunHiNeural"
        )
        
        audio_data = b""
        chunk_count = 0
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
                chunk_count += 1
        
        if audio_data:
            print(f"  ✓ Edge TTS 정상 ({len(audio_data)} bytes, {chunk_count} chunks)")
            return True
        else:
            print("  ❌ 오디오 데이터 생성 실패")
            return False
            
    except Exception as e:
        print(f"  ❌ Edge TTS 오류: {e}")
        return False

def main():
    """진단 실행"""
    print("\n" + "="*60)
    print("   🔊 음성 입출력 시스템 진단 도구")
    print("="*60)
    
    results = {
        "마이크": check_microphone(),
        "스피커": check_speaker(),
        "Google API": check_google_api(),
        "Edge TTS": asyncio.run(check_edge_tts())
    }
    
    print_section("진단 결과 요약")
    
    all_ok = True
    for component, status in results.items():
        icon = "✓" if status else "❌"
        print(f"{icon} {component}: {'정상' if status else '문제 발생'}")
        if not status:
            all_ok = False
    
    print()
    if all_ok:
        print("🎉 모든 시스템이 정상입니다!")
    else:
        print("⚠️  문제가 있는 항목을 확인하세요.")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
