from  dotenv import load_dotenv
import streamlit as st
from ai import get_personality_analysis

load_dotenv()

st.title("AI 관상 보기 프로그램")
st.write("---")

st.write("안녕하세요! AI 관상가입니다.")
st.write("당신의 얼굴 특징을 알려주시면 성격과 미래를 분석해드릴게요")

face_desc = st.text_area("얼굴 특징을 입력하세요")
face_desc = face_desc.strip()
# .strip() 문자열 좌우의 연속된 화이트 스페이스를 제거합니다.

if st.button("관상 보기", type="primary"):
    if face_desc:
        with st.spinner("관상을 분석중입니다..."):
            # 작업이 진행중임을 시각적으로 보여주는 스피너
            result = get_personality_analysis(face_desc)
            st.write("----")
            # "----" 는 마크다운이다.
            st.write("관상 분석이 끝났습니다. ")
            st.info(result)
            # 해당 스피너가 내부에 있는 코드 st.write를 읽을 때 계속 돌지만
            # 반복문 외부로 넘어가면 스피너를 종료합니다.
    else:
        st.error("얼굴 특징을 입력하고, 관상 보기 버튼을 클릭해주세요.")
        #st.warning("얼굴 특징을 입력하고, 관상 보기 버튼을 클릭해주세요.")
        #st.write("얼굴 특징을 입력하고, 관상 보기 버튼을 클릭해주세요.")
