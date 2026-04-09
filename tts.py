import asyncio
import edge_tts
import pygame
import io

async def _generate_audio(text, voice, rate=0, pitch=0, volume=1.0):
    communicate = edge_tts.Communicate(text, voice, rate=f"{rate:+d}%", pitch=f"{pitch:+d}Hz", volume=f"{int(volume * 100):+d}%")
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

def text_to_speech(text, voice_type="sweet", rate=0, pitch=0, volume=1.0):
    if voice_type == "sweet":
        voice = "ko-KR-SunHiNeural"  # 감미로운 여성 목소리
    elif voice_type == "character":
        voice = "ko-KR-InJoonNeural"  # 도라에몽 스타일 남성 목소리 (낮은 톤)
    else:
        voice = "ko-KR-SunHiNeural"

    # 비동기 함수 실행
    audio_data = asyncio.run(_generate_audio(text, voice, rate, pitch, volume))

    # pygame으로 재생
    pygame.mixer.init()
    pygame.mixer.music.load(io.BytesIO(audio_data))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)