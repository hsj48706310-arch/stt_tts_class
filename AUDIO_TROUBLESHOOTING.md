# 음성 입출력 문제 해결 가이드

## 📋 개선사항 요약

### 1. **향상된 에러 처리**
- 모든 오류 메시지가 사용자 친화적으로 변경
- 각 단계별 진행 상황을 사용자에게 표시
- 문제 원인 및 해결 방법 제시

### 2. **새 파일 구조**

```
📁 stt_tts_class/
├─ main_improved.py          ← 개선된 메인 앱 (권장)
├─ stt_improved.py          ← 개선된 음성 인식
├─ tts_improved.py          ← 개선된 음성 합성
├─ audio_diagnostic.py      ← 진단 도구
├─ main.py                  ← 원본 (참고용)
├─ stt.py                   ← 원본
└─ tts.py                   ← 원본
```

---

## 🚀 사용 방법

### Step 1: 진단 도구 실행
다른 PC에서 먼저 시스템을 진단하세요:

```bash
python audio_diagnostic.py
```

**진단 항목:**
- ✓ 마이크 감지 및 연결 상태
- ✓ 스피커/오디오 출력 장치
- ✓ Google Speech Recognition API 연결
- ✓ Edge TTS 서비스 연결

### Step 2: 메인 앱 실행
```bash
streamlit run main_improved.py
```

---

## ❌ 일반적인 문제 및 해결 방법

### 📥 음성 입력 문제

#### 문제 1: "마이크 오류"
**원인:**
- 마이크가 연결되지 않음
- 마이크가 비활성화됨
- 다른 앱이 마이크를 사용 중

**해결 방법:**
```
Windows:
1. 설정 → 개인정보 → 마이크
2. "앱이 마이크에 액세스하도록 허용" 켜기
3. 마이크가 연결되어 있는지 확인
```

#### 문제 2: "Google API에 접근할 수 없습니다"
**원인:**
- 인터넷 연결 불안정
- 방화벽이 API 차단
- Google 서비스 차단

**해결 방법:**
```
1. 인터넷 연결 확인
2. 방화벽/백신 설정 확인
3. VPN 사용 시 VPN 변경
4. 회사/학교 네트워크: IT 부서에 문의
```

#### 문제 3: "음성을 인식할 수 없습니다"
**원인:**
- 배경음이 너무 큼
- 마이크 감도 부족
- 음성이 너무 작음

**해결 방법:**
```
1. 조용한 환경에서 시도
2. 마이크에 가까이 대고 말하기
3. Windows 마이크 볼륨 확인
4. 마이크 입력 수준 조정
```

---

### 📤 음성 출력 문제

#### 문제 1: "오디오 디바이스 오류"
**원인:**
- 스피커/헤드폰 연결 해제
- 오디오 출력 장치 비활성화
- pygame 라이브러리 문제

**해결 방법:**
```
Windows:
1. 설정 → 사운드 → 볼륨
2. 기본 재생 장치 확인
3. "음량" 확인

또는:
1. 제어판 → 사운드
2. 재생 탭에서 기본 장치 설정
```

#### 문제 2: 음성이 안 나옴
**원인:**
- 시스템 볼륨이 낮음
- 뮤트 상태
- 오디오 출력 포트 문제

**해결 방법:**
```
1. 작업 표시줄 볼륨 아이콘 확인
2. 헤드폰 케이블 확인
3. 다른 앱에서 오디오 테스트 (유튜브 등)
```

#### 문제 3: pygame 오류
**원인:**
- pygame 설치 미흡
- 호환성 문제

**해결 방법:**
```bash
pip uninstall pygame -y
pip install pygame --upgrade
```

---

## 🔧 고급 설정

### 마이크 선택 (여러 마이크가 있는 경우)
`stt_improved.py` 수정:
```python
# 특정 마이크 사용 (인덱스 변경)
with sr.Microphone(device_index=1) as source:  # 0→1 등으로 변경
    ...
```

### 음성 인식 언어 변경
`main_improved.py` 수정:
```python
# English
recognized_text = speech_to_text(language="en-US")

# Japanese
recognized_text = speech_to_text(language="ja-JP")

# Chinese
recognized_text = speech_to_text(language="zh-CN")
```

### TTS 목소리 커스텀
`tts_improved.py`의 `text_to_speech` 함수:
```python
# 다른 목소리 옵션:
# ko-KR-SunHiNeural    - 여성 (밝음)
# ko-KR-InJoonNeural   - 남성 (낮음)
# ko-KR-BongJinNeural  - 남성 (표준)
```

---

## 📊 진단 도구 읽기

```bash
python audio_diagnostic.py
```

**출력 예시:**
```
============================================================
   🔊 음성 입출력 시스템 진단 도구
============================================================

============================================================
  마이크 진단
============================================================
사용 가능한 마이크:
  ✓ 마이크 #0
  ✓ 마이크 #1

기본 마이크 테스트 중...
  ✓ 마이크 연결됨
  ✓ 주변음 조정 완료

...

============================================================
진단 결과 요약
============================================================
✓ 마이크: 정상
✓ 스피커: 정상
✓ Google API: 정상
✓ Edge TTS: 정상

🎉 모든 시스템이 정상입니다!
```

---

## 📦 필수 패키지 확인

다른 PC에서 이 패키지들이 모두 설치되어 있는지 확인하세요:

```bash
pip list | findstr -E "streamlit|openai|edge-tts|pygame|pyaudio|speechrecognition"
```

**필수 패키지:**
- `streamlit` >= 1.56.0
- `speechrecognition` >= 3.10.0
- `edge-tts` >= 7.2.0
- `pygame` >= 2.6.0
- `pyaudio` >= 0.2.14 (마이크 입력용)
- `openai` >= 2.30.0

---

## 🆘 패키지 재설치

```bash
# 모든 패키지 재설치
pip install streamlit>=1.56.0 speechrecognition>=3.10.0 edge-tts>=7.2.0 pygame>=2.6.0 pyaudio>=0.2.14 openai>=2.30.0 -U

# 또는 pyproject.toml에서 설치
pip install -e .
```

### PyAudio 설치 문제 해결 (Windows)

PyAudio는 설치가 까다로울 수 있습니다:

```bash
# 방법 1: 미리 컴파일된 wheel 사용
pip install pipwin
pipwin install pyaudio

# 방법 2: 특정 버전 설치
pip install pyaudio==0.2.11

# 방법 3: 직접 컴파일 (Visual Studio 필요)
pip install pyaudio --no-binary :all: --force-reinstall
```

PyAudio 설치 불가 시:
- 마이크 대신 Streamlit 내장 녹음 사용 고려
- 클라우드 음성 API 사용 고려

---

## 🌐 네트워크 환경에서

### 회사/학교 네트워크
Google API, Edge TTS 접근이 차단될 수 있습니다:

**해결 방법:**
1. IT 부서에 API 접근 권한 요청
2. 프록시 설정 확인
3. VPN 사용
4. 로컬 음성 인식 모델 사용 고려 (Vosk, Whisper 등)

---

## 📝 체크리스트

다른 PC에서 문제 발생 시 확인사항:

- [ ] 마이크/스피커 물리적 연결 확인
- [ ] Windows 사운드 설정에서 기본 장치 확인
- [ ] 마이크/스피커 앱 권한 활성화
- [ ] 인터넷 연결 확인
- [ ] 방화벽/백신 설정 확인
- [ ] 모든 필수 패키지 설치 확인
- [ ] `python audio_diagnostic.py` 실행으로 진단
- [ ] 다른 브라우저/앱에서 마이크/스피커 테스트
- [ ] 관리자 권한으로 실행 시도

---

## 💡 추가 팁

### 1. Streamlit 앱 실행 옵션
```bash
# 포트 변경
streamlit run main_improved.py --server.port 8502

# 서버 정보 표시 안 함
streamlit run main_improved.py --logger.level=error

# 캐시 초기화
streamlit cache clear
```

### 2. 로그 확인
```bash
# 상세 로그 확인
streamlit run main_improved.py --logger.level=debug
```

### 3. 문제 보고 정보
문제 발생 시 수집해야 할 정보:
- OS 버전 (Windows 10/11?)
- Python 버전
- 각 패키지 버전
- 오류 메시지 전체
- `audio_diagnostic.py` 실행 결과

---

## 📞 추가 도움

더 많은 정보:
- [SpeechRecognition 문서](https://pypi.org/project/SpeechRecognition/)
- [edge-tts GitHub](https://github.com/rany2/edge-tts)
- [pygame 문서](https://www.pygame.org/docs/)

---

**작성일:** 2026-04-09  
**버전:** 1.0
