# stt_tts_class

## AI Confession Message Refiner 💌

A fun AI application that helps users express their feelings more beautifully using **Speech Recognition, LLM, and Text-to-Speech**.

---

## Features

* 🎤 **Speech-to-Text (STT)**
  Convert user's spoken message into text.

* 🤖 **LLM-based Message Refinement**
  Improve the message with different tones and styles.

* 🎭 **Tone / Style Control**
  Example styles:

  * Romantic poet
  * Polite office worker
  * Casual confession

* 🔊 **Text-to-Speech (TTS)**
  Play the refined message with a natural voice.

---

## Concept

**고백 교정기 💖**
진심을 전하기 서툰 분들을 위한 AI 솔루션입니다.

1. 사용자가 대충 쓴 진심을 입력합니다.
   예: *"나 너 좋아하는데 사귈래?"*

2. AI가 메시지를 더 매력적으로 다듬어 줍니다.
   예:

   * 감성 시인 버전
   * 깔끔한 직장인 버전

3. 완성된 메시지를 **TTS 음성으로 재생**합니다.

---

## Run

Run the improved version with Streamlit:

```
streamlit run main_improved.py
```

---

## Tech Stack

* Python
* Streamlit
* Speech-to-Text
* LLM
* Text-to-Speech


# 🎙️ 음성 입출력 개선 패키지

다른 PC에서 음성 입력(STT)과 음성 출력(TTS)가 제대로 작동하지 않는 문제를 해결하기 위한 개선 버전입니다.

## ✨ 주요 개선사항

### 1. **향상된 에러 처리**
- 모든 에러 메시지가 명확하고 사용자 친화적으로 개선
- 각 단계마다 진행 상황을 사용자에게 보여줌
- 문제 발생 시 구체적인 해결 방법 제시

### 2. **디바이스 진단**
- 마이크 연결 상태 확인
- 오디오 출력 장치 확인
- API 연결 상태 확인

### 3. **자동 설치 스크립트**
- Windows: `setup.bat`
- macOS/Linux: `setup.sh`

### 4. **진단 도구**
- 모든 시스템 컴포넌트 자동 진단
- 문제 원인 파악 및 해결책 제시

---

## 🚀 빠른 시작

### Step 1: 설치 (다른 PC에서)

#### Windows
```bash
setup.bat
```

#### macOS/Linux
```bash
bash setup.sh
```

### Step 2: 시스템 진단

```bash
python audio_diagnostic.py
```

모든 항목이 ✓ 표시되면 정상입니다.

### Step 3: 앱 실행

```bash
streamlit run main_improved.py
```

---

## 📁 파일 설명

| 파일 | 설명 |
|------|------|
| `main_improved.py` | ✨ 개선된 메인 앱 (권장) |
| `stt_improved.py` | 개선된 음성 인식 모듈 |
| `tts_improved.py` | 개선된 음성 합성 모듈 |
| `audio_diagnostic.py` | 종합 진단 도구 |
| `quick_mic_test.py` | 마이크만 빠르게 테스트 |
| `quick_speaker_test.py` | 스피커만 빠르게 테스트 |
| `setup.bat` | Windows 자동 설치 스크립트 |
| `setup.sh` | macOS/Linux 자동 설치 스크립트 |
| `AUDIO_TROUBLESHOOTING.md` | 상세 문제 해결 가이드 |

---

## 🔧 빠른 테스트

### 마이크 테스트만
```bash
python quick_mic_test.py
```

### 스피커 테스트만
```bash
python quick_speaker_test.py
```

---

## ❌ 일반적인 문제

### 음성 입력 안 됨
1. 마이크가 물리적으로 연결되어 있는지 확인
2. Windows 설정에서 마이크 권한 활성화 확인
3. `python quick_mic_test.py` 실행하여 테스트
4. `python audio_diagnostic.py` 실행하여 완전 진단

### 음성 출력 안 됨
1. 스피커/헤드폰 연결 확인
2. Windows 사운드 설정에서 기본 재생 장치 확인
3. `python quick_speaker_test.py` 실행하여 테스트
4. 시스템 볼륨 확인

### Google API 오류
1. 인터넷 연결 확인
2. 방화벽/백신 설정 확인
3. 회사/학교 네트워크: IT 부서에 문의
4. VPN 변경 시도

---

## 📊 성능 비교

| 항목 | 원본 | 개선된 버전 |
|------|------|----------|
| 에러 처리 | 기본 | 상세 |
| 사용자 피드백 | 없음 | 단계별 표시 |
| 진단 기능 | 없음 | 종합 진단 |
| 오류 메시지 | 기술적 | 친화적 + 해결책 |
| 설치 안내 | 수동 | 자동 스크립트 |

---

## 🆘 추가 도움

### 상세 가이드
[AUDIO_TROUBLESHOOTING.md](AUDIO_TROUBLESHOOTING.md) 참고

### 원본 파일 (참고용)
- `main.py` - 원본 메인 앱
- `stt.py` - 원본 음성 인식
- `tts.py` - 원본 음성 합성

---

## ✅ 체크리스트

다른 PC에서 설정할 때:

- [ ] `setup.bat` 또는 `setup.sh` 실행
- [ ] `python audio_diagnostic.py` 실행해서 모두 ✓ 확인
- [ ] 마이크/스피커 물리적 연결 확인
- [ ] `streamlit run main_improved.py` 실행
- [ ] 음성 입력/출력 테스트

---

## 버전 정보

- **작성일**: 2026-04-09
- **버전**: 1.0
- **Python 버전**: 3.12+
- **테스트 환경**: Windows 10/11

---

**문제가 발생하면 `AUDIO_TROUBLESHOOTING.md`를 참고하세요!**
