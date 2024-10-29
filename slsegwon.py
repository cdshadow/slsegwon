import streamlit as st
import pandas as pd

# GitHub CSV file path
file_path = 'https://raw.githubusercontent.com/cdshadow/slsegwon/main/slsegwon.csv'

# Caching the data loading process
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)  # , encoding='cp949'
    data['서비스 상태 지수'] = data['서비스 상태 지수'].round(0).astype(int)  # '서비스 상태 지수' 컬럼을 정수로 변환
    return data

# Load data file
data = load_data(file_path)

# Center align title
st.markdown("<h3 style='text-align: center;'>소규모 체육시설 서비스가 필요한 1인가구 슬세권</h3>", unsafe_allow_html=True)

# Center align table contents using CSS
st.markdown(
    """
    <style>
        .css-1p05t4e tr, .css-1p05t4e th, .css-1p05t4e td {
            text-align: center;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Display table
st.table(data)
