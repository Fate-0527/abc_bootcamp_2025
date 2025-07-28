# ai.py

from openai import OpenAI

def get_personality_analysis(face_desc: str) -> str:
    """
    인자로 얼굴 설명을 받아, openai LLM API를 활용하여 성격과 미래를 분석합니다.
    """
    # doc string

    # 인자로 얼굴 설명을 받아, openai LLM API를 활용하여 성격과 미래를 분석합니다.
    # 주석은 파이썬 입장에서 무시하지만, """ 3개로 작성하게 된다면, 함수 위에서 설명을 도와줍니다


    # 원하는 어떠한 형태로든 지시문 문자열을 생성하실 수 있습니다.
    # 타입을 str로 지정
    prompt = "당신은 전문 관상가입니다. "
    prompt += "사람들의 얼굴 특징을 보고 성격과 미래를 친근하게 분석해주세요."
    prompt += "\n 얼굴 특징 : " + face_desc

    client = OpenAI()  # OPENAI_API_KEY 환경변수 지정이 필요

    response = client.responses.create(
        model="gpt-4o",  # 사용할 두뇌 지정
        input=prompt,
    )
    print("usage :", response.usage)

    return response.output_text