import streamlit as st
import time

st.set_page_config(page_title="나의 장점 소개", page_icon="🏃‍♂️")

st.title("🏃‍♂️ 나의 장점: 엄청난 스피드!")
st.subheader("체력과 끈기, 그리고 누구보다 빠른 발을 가지고 있습니다.")

st.markdown("---")

# 시각적인 재미를 위한 컴포넌트
st.markdown("### ⚡ 얼마나 빠르냐고요?")

if st.button("제 달리기 속도 측정해보기 (클릭!)"):
    progress_text = "준비... 땅! 🏃‍♂️💨"
    my_bar = st.progress(0, text=progress_text)
    
    # 달리기 게이지가 차오르는 효과
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()
    
    st.success("🏁 눈 깜짝할 사이에 100m 도착! 순발력과 폭발적인 스피드가 저의 무기입니다.")

# 장점 상세 설명
st.markdown("### 📈 달리기가 가져다준 장점들")

st.write("""
1. **강인한 체력과 지구력**: 꾸준한 달리기를 통해 지치지 않는 에너지를 유지합니다.
2. **목표를 향한 집념**: 결승선을 향해 달릴 때처럼, 맡은 일은 끝까지 책임지고 빠르게 완수합니다.
3. **위기 대처 능력**: 빠른 상황 판단과 순발력으로 급한 도전에 유연하게 대처합니다.
""")
