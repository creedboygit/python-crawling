import os
from openai import OpenAI

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# API 키가 없으면 오류 발생
if not api_key:
    raise ValueError("API 키가 설정되지 않았습니다. OPENAI_API_KEY 환경 변수를 설정해주세요.")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# result = response.choices[0].message.content
# print(result)

# for chunk in response.chat.chunks:

result = ""
for chunk in response:
    delta_data = chunk.choices[0].delta
    if 'role' in delta_data:
        continue
    elif 'content' in delta_data:
        r_text = delta_data['content']
        result += r_text
        print(r_text, end="", flush=True)

print("*" * 10)
print(result)