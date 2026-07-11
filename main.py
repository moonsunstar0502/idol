import streamlit as st
import time

# 1. 페이지 설정 (가장 최상단 필수!)
st.set_page_config(
    page_title="나를 소개하는 공간",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 메뉴 구현 (호환성 에러 우회 ✨)
st.sidebar.title("📱 메뉴 선택")
menu = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["홈 화면", "나의 성격 소개", "나의 장점 소개"]
)

st.sidebar.markdown("---")

# 사이드바에 들어가는 아이돌 소속사 필터 기능
st.sidebar.header("⚙️ 소속사 필터")
selected_companies = st.sidebar.multiselect(
    "소속사를 선택하세요", 
    ['하이브', 'SM', 'JYP', 'YG']
)

# =========================================================
# 3. 각 메뉴별 페이지 콘텐츠 (if-elif 문으로 제어)
# =========================================================

# --- [메뉴 1: 홈 화면] ---
if menu == "홈 화면":
    st.title("👋 안녕하세요! 저를 소개합니다")
    st.subheader("저의 웹사이트에 오신 것을 환영합니다.")
    st.markdown("---")

    st.write(
        """
        이 웹사이트는 **Streamlit**을 활용하여 만든 저의 개인 소개 페이지입니다. 
        왼쪽 사이드바의 메뉴를 이용해 저에 대해 더 자세히 알아보세요!
        """
    )
    
    # 소속사 필터링 결과 출력 영역
    if selected_companies:
        st.markdown("### 🏢 선택하신 소속사 정보")
        st.write(f"현재 선택된 소속사: {', '.join(selected_companies)}")
        
        if '하이브' in selected_companies: st.write("- **하이브**: 방탄소년단(BTS), 뉴진스, 세븐틴 등")
        if 'SM' in selected_companies: st.write("- **SM**: 에스파, NCT, 라이즈 등")
        if 'JYP' in selected_companies: st.write("- **JYP**: 트와이스, 스트레이 키즈, 있지 등")
        if 'YG' in selected_companies: st.write("- **YG**: 블랙핑크, 베이비몬스터, 트레저 등")
    else:
        st.info("💡 사이드바 아래에서 관심 있는 소속사를 선택해 보세요!")

    st.balloons()

# --- [메뉴 2: 나의 성격 소개] ---
elif menu == "나의 성격 소개":
    st.title("✨ 나의 성격: 활발함과 긍정 에너지")
    st.subheader("사람들과 어울리고 에너지를 나누는 것을 좋아합니다!")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔥 활발한 에너지")
        st.write(
            """
            - 처음 보는 사람과도 금방 친해지는 친화력을 가지고 있습니다.
            - 팀 프로젝트나 모임에서 항상 분위기 메이커 역할을 자처합니다.
            - 가만히 있기보다는 새로운 활동을 찾아 나서는 것을 즐깁니다.
            """
        )

    with col2:
        st.markdown("### ☀️ 긍정적인 마인드")
        st.write(
            """
            - 어려운 상황이 찾아와도 '오히려 좋아!'라는 마음으로 극복합니다.
            - 주변 사람들에게 긍정적인 영향력과 웃음을 주려고 노력합니다.
            """
        )

    st.blockquote("“혼자 가면 빨리 가지만, 함께 가면 멀리 간다”는 말을 좋아합니다. 함께 에너지를 내는 시너지를 중요하게 생각해요!")

# --- [메뉴 3: 나의 장점 소개] ---
elif menu == "나의 장점 소개":
    st.title("🏃‍♂️ 나의 장점: 엄청난 스피드!")
    st.subheader("체력과 끈기, 그리고 누구보다 빠른 발을 가지고 있습니다.")
    st.markdown("---")

    st.markdown("### ⚡ 얼마나 빠르냐고요?")

    if st.button("제 달리기 속도 측정해보기 (클릭!)"):
        progress_text = "준비... 땅! 🏃‍♂️💨"
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.5)
        my_bar.empty()
        
        st.success("🏁 눈 깜짝할 사이에 100m 도착! 순발력과 폭발적인 스피드가 저의 무기입니다.")

    st.markdown("### 📈 달리기가 가져다준 장점들")
    st.write("""
    1. **강인한 체력과 지구력**: 꾸준한 달리기를 통해 지치지 않는 에너지를 유지합니다.
    2. **목표를 향한 집념**: 결승선을 향해 달릴 때처럼, 맡은 일은 끝까지 책임지고 빠르게 완수합니다.
    3. **위기 대처 능력**: 빠른 상황 판단과 순발력으로 급한 도전에 유연하게 대처합니다.
    """)
