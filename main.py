import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="Idol Data Hub",
    page_icon="🎤",
    layout="wide"
)

# 2. 샘플 데이터 생성 (나중에 보유하신 CSV 파일 등으로 대체 가능)
@st.cache_data
def load_data():
    # 예시 데이터: 그룹명, 멤버, 데뷔일, 소속사, 대표곡, 팬덤 수(가상), 유튜브 조회수(가상)
    data = {
        "그룹명": ["NewJeans", "IVE", "aespa", "LE SSERAFIM", "RIIZE", "TWS"],
        "소속사": ["ADOR", "Starship", "SM", "SOURCE MUSIC", "SM", "PLEDIS"],
        "멤버수": [5, 6, 4, 5, 6, 6],
        "데뷔연도": [2022, 2021, 2020, 2022, 2023, 2024],
        "대표곡": ["Hype Boy", "Love Dive", "Supernova", "Perfect Night", "Get A Guitar", "첫 만남은 계획대로 되지 않아"],
        "해외팬덤지수": [85, 80, 90, 78, 70, 65],
        "유튜브조회수_백만": [350, 420, 280, 210, 120, 95]
    }
    return pd.DataFrame(data)

df = load_data()

# 3. 사이드바 - 검색 및 필터 기능
st.sidebar.header("🔍 검색 및 필터")

# 텍스트 검색 (그룹명 또는 대표곡)
search_query = st.sidebar.text_input("아이돌 그룹명 또는 대표곡 검색", "")

# 소속사 멀티 선택 필터
companies = df["소속사"].unique()
selected_companies = st.sidebar.multiselect("소
