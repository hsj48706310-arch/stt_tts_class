"""
빠른 스피커 테스트 스크립트
"""

import asyncio
import edge_tts
import pygame
import io

async def test_speaker():
    print("\n=== 스피커 간단 테스트 ===\n")
    
    try:
        # Edge TTS로 음성 생성
        print("음성 합성 중...")
        test_text = "안녕하세요. 스피커 테스트입니다."
        
        communicate = edge_tts.Communicate(test_text, "ko-KR-SunHiNeural")
        audio_data = b""
        
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        
        if not audio_data:
            print("✗ 음성 합성 실패")
            return
        
        print(f"✓ 음성 합성 완료 ({len(audio_data)} bytes)")
        
        # 재생
        print("\n스피커로 재생 중... (1초)")
        pygame.mixer.init()
        pygame.mixer.music.load(io.BytesIO(audio_data))
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
        
        pygame.mixer.quit()
        print("✓ 재생 완료")
        
    except Exception as e:
        print(f"✗ 오류: {e}")
        print("\n스피커가 연결되어 있는지 확인하세요.")

if __name__ == "__main__":
    asyncio.run(test_speaker())
