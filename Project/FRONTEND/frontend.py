#python -m streamlit run FRONTEND/frontend.py
import pandas as pd
import streamlit as st
from BACKEND.data import read_file
st.title("Hello world")
file = st.file_uploader(
    "Select a CSV file",#duh
    type=["csv"],#csv type
    accept_multiple_files=False, #self explanatory
    max_upload_size=80 #megabyte
)
max_r = 100000
max_c = 25
if file is not None:
    df = read_file(file)
    if df is not None:
        st.success("Dataset loaded successfully!")
        st.dataframe(df.head(10))
        r, c = df.shape
        st.write(f"Rows: {r}")
        st.write(f"Columns: {c}")
        st.write(f"Shape: {df.shape}")
        st.write(df.dtypes)
        st.write(df.isnull().sum())
        st.write("Total duplicate rows: "+str(df.duplicated().sum()))

with st.sidebar:
    st.title("Machine Learning Lab")
    st.divider() #horz line
    st.subheader("Navigation")
    page = st.radio(
        "Go to",
        ["Home", "Upload Dataset", "Data Analysis", "Model Training"],
        label_visibility="collapsed"
    )
    st.divider()
    st.caption("v0.0")

