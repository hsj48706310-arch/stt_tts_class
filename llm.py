import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refine_text(text, style):
    if style == "poetic":
        prompt = f"다음 텍스트를 감성 가득한 시인 버전으로 다듬어주세요: {text}"
    elif style == "professional":
        prompt = f"다음 텍스트를 깔끔한 직장인 버전으로 다듬어주세요: {text}"
    else:
        return text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 텍스트를 다듬는 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content.strip()