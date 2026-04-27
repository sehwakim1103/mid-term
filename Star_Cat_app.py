import streamlit as st
import pandas as pd
import time



st.set_page_config(page_title="스타캣 매칭 테스트", page_icon="*")
st.markdown("""
<style>
.stApp {
    background-color: #FFF0F5;
}
</style>
""", unsafe_allow_html=True)

st.image("images/StarCat.png", width=800)

st.title(" ✬나와 잘 맞는 스타캣 찾기!✬")

st.info("""
과제 제출자 정보  
- 학번: 2025205090
- 이름: 김세화
""")

st.write("질문에 답하면 4마리의 스타캣중 나와 가장 잘 맞는 캐릭터를 매칭해주는 테스트입니다!.")


if "login" not in st.session_state:
    st.session_state.login = False


st.header(" 로그인")

USER_ID = "sehwa"
USER_PW = "1234"

if not st.session_state.login:
    user_id = st.text_input("아이디")
    user_pw = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if user_id == "sehwakim1103" and user_pw == "110305":
            st.session_state.login = True
            st.success("로그인 성공!")
            st.rerun()
        else:
            st.error("로그인 실패! 다시 입력해주세요.")

else:
    st.success("로그인 완료!")

    if st.button("로그아웃"):
        st.session_state.login = False
        st.rerun()

    st.divider()

  
    @st.cache_data
    def load_quiz_data():
        time.sleep(1)

        questions = [
            {
                "question": "Q1. 쉬는 날 나는?",
                "options": {
                    "A. 집에서 조용히 쉰다": "몽글이",
                    "B. 친구들과 약속을 잡는다": "뿅뿅이",
                    "C. 해야 할 일을 먼저 끝낸다": "차차",
                    "D. 갑자기 하고 싶은 걸 한다": "루루",
                    "E. 그날 기분에 따라 다르다": "루루"
                }
            },
            {
                "question": "Q2. 친구들이 보는 나의 이미지는?",
                "options": {
                    "A. 조용하고 편안한 사람": "몽글이",
                    "B. 밝고 에너지 넘치는 사람": "뿅뿅이",
                    "C. 꼼꼼하고 믿음직한 사람": "차차",
                    "D. 개성 있고 자유로운 사람": "루루",
                    "E. 알다가도 모르겠는 사람": "루루"
                }
            },
            {
                "question": "Q3. 마음에 드는 물건을 고를 때 나는?",
                "options": {
                    "A. 귀엽고 포근한 느낌을 고른다": "몽글이",
                    "B. 눈에 확 띄는 걸 고른다": "뿅뿅이",
                    "C. 실용적인 걸 고른다": "차차",
                    "D. 남들이 잘 안 고르는 걸 고른다": "루루",
                    "E. 그냥 끌리는 걸 고른다": "몽글이"
                }
            },
            {
                "question": "Q4. 단체 활동을 할 때 나는?",
                "options": {
                    "A. 조용히 필요한 일을 돕는다": "몽글이",
                    "B. 분위기를 띄운다": "뿅뿅이",
                    "C. 계획을 세우고 정리한다": "차차",
                    "D. 새로운 아이디어를 낸다": "루루",
                    "E. 상황에 맞춰 움직인다": "차차"
                }
            },
            {
                "question": "Q5. 가장 끌리는 분위기는?",
                "options": {
                    "A. 따뜻하고 몽글몽글한 분위기": "몽글이",
                    "B. 신나고 활기찬 분위기": "뿅뿅이",
                    "C. 깔끔하고 안정적인 분위기": "차차",
                    "D. 독특하고 자유로운 분위기": "루루",
                    "E. 신비롭고 상상력 있는 분위기": "루루"
                }
            },
            {
                "question": "Q6. 새로운 환경에 가면 나는?",
                "options": {
                    "A. 조용히 상황을 지켜본다": "몽글이",
                    "B. 먼저 다가가서 말을 건다": "뿅뿅이",
                    "C. 해야 할 일을 먼저 파악한다": "차차",
                    "D. 흥미로운 것부터 찾아본다": "루루",
                    "E. 분위기에 따라 다르게 행동한다": "루루"
                }
            },
            {
                "question": "Q7. 스트레스를 받으면 나는?",
                "options": {
                    "A. 혼자만의 시간을 가진다": "몽글이",
                    "B. 친구들과 떠들며 푼다": "뿅뿅이",
                    "C. 문제를 해결하려고 노력한다": "차차",
                    "D. 새로운 걸 하면서 잊는다": "루루",
                    "E. 그냥 아무 생각 안 하려고 한다": "몽글이"
                }
            },
            {
                "question": "Q8. 가장 끌리는 취미는?",
                "options": {
                    "A. 영화/음악 감상": "몽글이",
                    "B. 운동이나 활동적인 것": "뿅뿅이",
                    "C. 공부나 자기계발": "차차",
                    "D. 여행이나 새로운 경험": "루루",
                    "E. 옷 쇼핑하기": "루루"
                }
            },
            {
                "question": "Q9. 친구가 고민 상담을 하면 나는?",
                "options": {
                    "A. 조용히 들어주고 공감해준다": "몽글이",
                    "B. 분위기를 밝게 바꿔준다": "뿅뿅이",
                    "C. 해결 방법을 같이 고민해준다": "차차",
                    "D. 새로운 시각을 제시해준다": "루루",
                    "E. 상황에 따라 다르게 반응한다": "차차"
                }
            },
            {
                "question": "Q10. 내가 가장 중요하게 생각하는 것은?",
                "options": {
                    "A. 편안함과 안정감": "몽글이",
                    "B. 재미와 즐거움": "뿅뿅이",
                    "C. 계획과 책임감": "차차",
                    "D. 자유와 개성": "루루",
                    "E. 균형과 유연함": "루루"
                }
            }
        ]

        return questions

    @st.cache_data
    def load_character_data():
        characters = {
            "몽글이": {
                "emoji": "✶",
                "image": "images/mongle.jpeg",
                "description": "❤ 조용하고 따뜻한 감성을 가진 캐릭터입니다. 소극적이지만 섬세하고 깊은 마음을 가지고 있어요!❤"
            },
            "뿅뿅이": {
                "emoji": "✲",
                "image": "images/bbyong.jpeg",
                "description": "❤ 밝고 활발한 에너지를 가진 캐릭터입니다. 밝은 에너지로 주변 사람들을 기분 좋게해요❤"
            },
            "차차": {
                "emoji": "⁂",
                "image": "images/chacha.jpeg",
                "description": "❤차분하고 계획적인 캐릭터입니다.꼼꼼하고 신중한 성격으로 믿음직한 친구가 되어줘요 ❤"
            },
            "루루": {
                "emoji": "✸",
                "image": "images/lulu.jpeg",
                "description": "❤ 자유롭고 개성 있는 캐릭터입니다. 독특한 감각과 남다른 패션센스로 어딜가나 주목받아요❤"
            }
        }
        return characters

   

    questions = load_quiz_data()
    characters = load_character_data()

    st.divider()

    
    st.header("⍟캐릭터 매칭 테스트⍟")

    score = {
        "몽글이": 0,
        "뿅뿅이": 0,
        "차차": 0,
        "루루": 0
    }

    for i, q in enumerate(questions):
        st.subheader(q["question"])

        selected = st.radio(
            "하나를 선택하세요",
            list(q["options"].keys()),
            key=f"question_{i}"
        )

        matched_character = q["options"][selected]
        score[matched_character] += 1

    if st.button("결과 확인하기⇨"):
        result = max(score, key=score.get)

        st.divider()
        st.header("⚝결과 발표⚝")

        st.success(f"{characters[result]['emoji']} {result} 캐릭터!")

        st.image(characters[result]["image"], width=250)

        st.write(characters[result]["description"])

        st.write("### 캐릭터별 점수↴")
        st.write(score) 