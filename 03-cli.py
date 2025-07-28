from dotenv import load_dotenv
from ai import get_personality_analysis
# ai 파일에 있는 함수를 불러오기
print("# AI 관상가입니다. 얼굴 특징을 입력해주시면, 성격과 미래를 전망해드릴게요")
line = input("성격 특징 : ").strip()
# input 함수의 반환값은 문자열인데, 문자열 좌우의 연속된 whitespaces (스페이스바, 탭, new line 등등)을 제거해준다.
# 내가 아무리 스페이스바를 눌러도 다 제거해주고 실행해준다

if not line:
    print("얼굴 특징을 입력하지 않으셨습니다.")
else:
    print("입력하신 얼굴 특징 : ", line)
    print("분석 중")
    result = get_personality_analysis(line)
    print("분석 완료")
    print(result)

# repr : 값의 출력뿐만 아니라 구조를 잘 볼 수 있다.
# 탭이나 다양한 특수문자를 확인하기 좋다
# get_personality_analysis()