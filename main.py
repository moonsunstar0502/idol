import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="나를 소개하는 공간",
    page_icon="👋",
    layout="centered"
)

# 2. 홈 화면 타이틀 및 소개
st.title("👋 안녕하세요! 저를 소개합니다")
st.subheader("저의 웹사이트에 오신 것을 환영합니다.")
st.markdown("---")

st.write(
    """
    이 웹사이트는 **Streamlit**을 활용하여 만든 저의 개인 소개 페이지입니다. 
    왼쪽 사이드바의 메뉴를 이용해 저에 대해 더 자세히 알아보세요!
    """
)

# 3. 사이드바 - 아이돌 소속사 선택 (오류 수정된 부분 ✨)
st.sidebar.header("⚙️ 필터 설정")

# 한 줄로 길게 작성하거나 아래처럼 괄호 안에서 깔끔하게 마무리를 지어야 에러가 나지 않습니다.
selected_companies = st.sidebar.multiselect(
    "소속사를 선택하세요", 
    ['하이브', 'SM', 'JYP', 'YG']
)

# 소속사를 선택했을 때 화면에 보여줄 예시 콘텐츠
if selected_companies:
    st.markdown("### 🏢 선택하신 소속사 정보")
    st.write(f"현재 선택된 소속사: {', '.join(selected_companies)}")
    
    # 간단한 조건문 예시 (필요에 따라 데이터를 연결하시면 됩니다)
    if '하이브' in selected_companies:
        st.write("- **하이브**: 방탄소년단(BTS), 뉴진스, 세븐틴 등")
    if 'SM' in selected_companies:
        st.write("- **SM**: 에스파, NCT, 라이즈 등")
    if 'JYP' in selected_companies:
        st.write("- **JYP**: 트와이스, 스트레이 키즈, 있지 등")
    if 'YG' in selected_companies:
        st.write("- **YG**: 블랙핑크, 베이비몬스터, 트레저 등")
else:
    st.info("💡 사이드바에서 관심 있는 소속사를 선택해 보세요!")

st.markdown("---")

# 4. 멀티페이지 안내 카드
with st.container():
    st.success("💡 **사이드바 상단 메뉴 안내**\n"
               "- **1_Personality**: 저의 활발한 성격에 대해 이야기합니다.\n"
               "- **2_Strengths**: 저의 특별한 장점(달리기!)을 소개합니다.")

st.balloons()  # 환영 애니메이션 효과
