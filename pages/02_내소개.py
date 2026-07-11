import streamlit as st

st.set_page_config(page_title="나의 성격 소개", page_icon="✨")

st.title("✨ 나의 성격: 활발함과 긍정 에너지")
st.subheader("사람들과 어울리고 에너지를 나누는 것을 좋아합니다!")

st.markdown("---")

# 성격 특징 레이아웃 분할
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

# 인용구 추가
st.blockquote("“혼자 가면 빨리 가지만, 함께 가면 멀리 간다”는 말을 좋아합니다. 함께 에너지를 내는 시너지를 중요하게 생각해요!")
