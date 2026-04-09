import asyncio
import edge_tts
from typing import Tuple

async def _generate_audio(text: str, voice: str, rate: int = 0, pitch: int = 0, volume: str = "+0%") -> bytes:
    """
    Edge TTS를 사용하여 음성 합성
    
    Args:
        text: 합성할 텍스트
        voice: 목소리 선택
        rate: 재생 속도 (-100 ~ 100)
        pitch: 음정 (-100 ~ 100)
        volume: 볼륨 (-100% ~ 100%)
    
    Returns:
        생성된 오디오 바이트 데이터
    """
    try:
        communicate = edge_tts.Communicate(
            text, 
            voice, 
            rate=f"{rate:+d}%", 
            pitch=f"{pitch:+d}Hz", 
            volume=volume
        )
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    except Exception as e:
        raise Exception(f"음성 합성 오류: {str(e)}")

def text_to_speech(text: str, voice_type: str = "sweet", rate: int = 0, pitch: int = 0, volume: float = 1.0) -> bytes:
    """
    텍스트를 음성으로 변환하여 오디오 데이터 반환
    
    Args:
        text: 합성할 텍스트
        voice_type: 목소리 타입 ("sweet" 또는 "character")
        rate: 재생 속도
        pitch: 음정
        volume: 볼륨 (0.0 ~ 2.0)
    
    Returns:
        오디오 바이트 데이터
    """
    try:
        # 목소리 선택
        if voice_type == "sweet":
            voice = "ko-KR-SunHiNeural"  # 감미로운 여성 목소리
        elif voice_type == "character":
            voice = "ko-KR-InJoonNeural"  # 캐릭터 남성 목소리
        else:
            voice = "ko-KR-SunHiNeural"
        
        # 볼륨 변환 (1.0 -> "+0%", 0.5 -> "-50%", 1.5 -> "+50%")
        volume_str = f"{int((volume - 1) * 100):+d}%"
        
        # 비동기 음성 생성
        audio_data = asyncio.run(_generate_audio(text, voice, rate, pitch, volume_str))
        
        if not audio_data:
            raise Exception("음성 생성 실패")
        
        return audio_data
        
    except Exception as e:
        raise Exception(f"음성 생성 오류: {str(e)}")
