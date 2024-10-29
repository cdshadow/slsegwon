import streamlit as st
import pandas as pd

# GitHub CSV file path
file_path = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/slsegwon.csv'

# Caching the data loading process
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    return data

# Load data file
data = load_data(file_path)

# Display the table with the specified title
st.title('소규모 체육시설 서비스가 필요한 1인가구 슬세권')
st.table(data)
