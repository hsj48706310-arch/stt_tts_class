#!/bin/bash
# 음성 입출력 시스템 설치 스크립트 (macOS/Linux)

echo ""
echo "=========================================="
echo "  음성 입출력 프로젝트 설치 도우미"
echo "=========================================="
echo ""

# Python 버전 확인
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3이 설치되지 않았습니다."
    echo "        https://www.python.org/downloads/"
    exit 1
fi

echo "[1/5] Python 버전 확인 중..."
python3 --version
echo ""

echo "[2/5] pip 업그레이드 중..."
python3 -m pip install --upgrade pip setuptools wheel
echo ""

echo "[3/5] 필수 패키지 설치 중..."
echo "      (이 과정은 5-10분 소요될 수 있습니다)"
echo ""
python3 -m pip install \
    streamlit>=1.56.0 \
    openai>=2.30.0 \
    speechrecognition>=3.10.0 \
    edge-tts>=7.2.0 \
    pygame>=2.6.0 \
    pyaudio>=0.2.14 \
    python-dotenv>=0.9.9

echo ""
echo "[4/5] 설치된 패키지 확인 중..."
python3 -c "import streamlit; import speech_recognition; import edge_tts; import pygame; print('[OK] 모든 패키지 확인됨')" 2>/dev/null || echo "[WARNING] 패키지 확인 실패"
echo ""

echo "[5/5] 진단 도구 실행 (선택사항)"
echo ""
read -p "진단 도구를 지금 실행하시겠습니까? (y/n): " RUN_DIAG
if [[ "$RUN_DIAG" == "y" || "$RUN_DIAG" == "Y" ]]; then
    python3 audio_diagnostic.py
fi

echo ""
echo "=========================================="
echo "✓ 설치 완료!"
echo "=========================================="
echo ""
echo "다음 명령으로 앱을 실행하세요:"
echo "  streamlit run main_improved.py"
echo ""
echo "문제가 있으면 다음을 참고하세요:"
echo "  - AUDIO_TROUBLESHOOTING.md"
echo "  - python3 audio_diagnostic.py (진단 도구)"
echo ""
