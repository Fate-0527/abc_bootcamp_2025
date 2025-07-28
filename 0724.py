from dotenv import load_dotenv
load_dotenv() # .env 파일이 있으면 환경변수로 로딩한다.

import os
API_KEY = os.environ["OPENAI_API_KEY"]

from openai import OpenAI
client = OpenAI(api_key = API_KEY)  # OPENAI_API_KEY 환경변수 지정이 필요

i = 0
i += 1
i += 2

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn in korean.",
)
print("usage :", response.usage)
print(response.output_text)
