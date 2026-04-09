@echo off
REM 음성 입출력 시스템 설치 스크립트 (Windows)
REM 권장: 관리자 권한으로 실행

echo.
echo ==========================================
echo   음성 입출력 프로젝트 설치 도우미
echo ==========================================
echo.

REM Python 버전 확인
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python이 설치되지 않았습니다.
    echo         https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/5] Python 버전 확인 중...
python --version
echo.

echo [2/5] pip 업그레이드 중...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo [WARNING] pip 업그레이드 실패
)
echo.

echo [3/5] 필수 패키지 설치 중...
echo        (이 과정은 5-10분 소요될 수 있습니다)
echo.
python -m pip install ^
    streamlit>=1.56.0 ^
    openai>=2.30.0 ^
    speechrecognition>=3.10.0 ^
    edge-tts>=7.2.0 ^
    pygame>=2.6.0 ^
    pyaudio>=0.2.14 ^
    python-dotenv>=0.9.9

if errorlevel 1 (
    echo.
    echo [WARNING] 일부 패키지 설치 실패
    echo           PyAudio 설치 실패 시 아래 명령 시도:
    echo           pipwin install pyaudio
)
echo.

echo [4/5] 설치된 패키지 확인 중...
python -c "import streamlit; import speech_recognition; import edge_tts; import pygame; print('[OK] 모든 패키지 확인됨')" 2>nul
if errorlevel 1 (
    echo [WARNING] 패키지 확인 실패 - 수동 설치가 필요할 수 있습니다
)
echo.

echo [5/5] 진단 도구 실행 (선택사항)
echo.
set /p RUN_DIAG="진단 도구를 지금 실행하시겠습니까? (y/n): "
if /i "%RUN_DIAG%"=="y" (
    python audio_diagnostic.py
)

echo.
echo ==========================================
echo ✓ 설치 완료!
echo ==========================================
echo.
echo 다음 명령으로 앱을 실행하세요:
echo   streamlit run main_improved.py
echo.
echo 문제가 있으면 다음을 참고하세요:
echo   - AUDIO_TROUBLESHOOTING.md
echo   - python audio_diagnostic.py (진단 도구)
echo.
pause
