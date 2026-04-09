import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refine_and_analyze(text, style, mood):
    mood_descriptions = {
        "romantic": "로맨틱한 분위기로",
        "comic": "코믹한 분위기로",
        "serious": "진지한 분위기로",
        "cute": "귀엽게",
        "neutral": "중립적으로"
    }
    mood_desc = mood_descriptions.get(mood, "")
    style_desc = "감성 가득한 시인 버전" if style == "poetic" else "깔끔한 직장인 버전"

    prompt = f"""
사용자의 고백 메시지를 더 자연스럽게 고쳐주세요.

다음 정보를 제공하세요:

[교정된 메시지]
교정된 고백 문장

[성공 확률]
고백 성공 확률 (0~100%)

[이유]
간단한 이유 (3-4줄 정도로)

톤 스타일: {style_desc}, 분위기: {mood_desc}
원본 메시지: {text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 고백 메시지를 다듬고 성공 확률을 평가하는 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    content = response.choices[0].message.content.strip()

    # Parse the response
    lines = content.split('\n')
    message = ""
    probability = ""
    reason = ""
    current_section = None

    for line in lines:
        if line.startswith('[교정된 메시지]'):
            current_section = 'message'
        elif line.startswith('[성공 확률]'):
            current_section = 'probability'
        elif line.startswith('[이유]'):
            current_section = 'reason'
        elif current_section == 'message' and not line.startswith('['):
            message += line + '\n'
        elif current_section == 'probability' and not line.startswith('['):
            probability += line + '\n'
        elif current_section == 'reason' and not line.startswith('['):
            reason += line + '\n'

    return {
        'message': message.strip(),
        'probability': probability.strip(),
        'reason': reason.strip()
    }
