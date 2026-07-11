import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="IDOL INSIGHT Dashboard", page_icon="🎤", layout="wide")

# 2. 샘플 데이터 생성 (실제 데이터 파일이 있다면 pd.read_csv 등으로 대체 가능)
@st.cache_data
def load_data():
    data = {
        '이름': ['BTS V', 'BLACKPINK Jennie', 'NewJeans Hanni', 'IVE Wonyoung', 'Stray Kids Hyunjin'],
        '그룹': ['BTS', 'BLACKPINK', 'NewJeans', 'IVE', 'Stray Kids'],
        '소속사': ['HYBE', 'YG', 'ADOR', 'Starship', 'JYP'],
        '데뷔년도': [2013, 2016, 2022, 2021, 2018],
        '활동상태': ['활동중', '활동중', '활동중', '활동중', '활동중'],
        '국적': ['한국', '한국', '베트남', '한국', '한국']
    }
    return pd.DataFrame(data)

df = load_data()

# 3. 사이드바 검색 및 필터링
st.sidebar.header("🔍 검색 및 필터")
search_term = st.sidebar.text_input("아이돌 이름 또는 그룹 검색")
company_filter = st.sidebar.multiselect("소속사 선택", options=df['소속사'].unique(), default=df['소속사'].unique())

# 필터링 적용
filtered_df = df[
    (df['이름'].str.contains(search_term, case=False) | df['그룹'].str.contains(search_term, case=False)) &
    (df['소속사'].isin(company_filter))
]

# 4. 메인 화면 구성
st.title("🎤 IDOL INSIGHT: 아이돌 데이터 분석")
st.markdown("---")

# KPI 지표
col1, col2, col3 = st.columns(3)
col1.metric("검색된 아이돌 수", len(filtered_df))
col2.metric("참여 그룹 수", filtered_df['그룹'].nunique())
col3.metric("최신 데뷔", filtered_df['데뷔년도'].max())

st.markdown("### 📊 데이터 상세 보기")
st.dataframe(filtered_df, use_container_width=True)

# 5. 시각화 섹션
st.markdown("### 📈 소속사별 분포 및 데뷔 트렌드")
c1, c2 = st.columns(2)

with c1:
    fig_pie = px.pie(filtered_df, names='소속사', title='소속사별 비중', hole=0.4,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

with c2:
    fig_hist = px.histogram(filtered_df, x='데뷔년도', title='연도별 데뷔 분포', 
                            nbins=10, color_discrete_sequence=['#ff823a'])
    st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("---")
st.info("💡 깃허브에 코드를 푸시한 후 Streamlit Cloud에서 'main.py'를 연결하여 배포하세요.")
