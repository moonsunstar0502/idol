import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="나를 소개하는 공간",
    page_icon="👋",
    layout="centered"
)

# 홈 화면 콘텐츠
st.title("👋 안녕하세요! 저를 소개합니다")
st.subheader("저의 웹사이트에 오신 것을 환영합니다.")

st.markdown("---")

st.write(
    """
    이 웹사이트는 **Streamlit**을 활용하여 만든 저의 개인 소개 페이지입니다. 
    왼쪽 사이드바의 메뉴를 이용해 저에 대해 더 자세히 알아보세요!
    """
)

# 간단한 프로필 카드 형태 구현
with st.container():
    st.info("💡 **사이드바 메뉴 안내**\n"
            "- **1_Personality**: 저의 활발한 성격에 대해 이야기합니다.\n"
            "- **2_Strengths**: 저의 특별한 장점(달리기!)을 소개합니다.")

st.balloons()  # 환영하는 의미의 풍선 애니메이션 효과
