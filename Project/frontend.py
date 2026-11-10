import pandas as pd
import streamlit as st
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
    try:
        df = pd.read_csv(file)
        r, c = df.shape # row column number
        if r==0:
            st.error("Your CSV file is empty.")
        elif r >max_r:
            st.error(f"Too many rows. The max is: {max_r:,}")
        elif c >max_c:
            st.error(f"Too many columns. The max is: {max_c}")
        else:
            st.success("Dataset uploaded!")
            st.write("Dataset Preview")
            st.dataframe(df.head(10))
            st.write(f"Rows: {r:,}")
            st.write(f"Columns: {c}")
    except Exception:
        st.error("Unable to read this file. Try again later!")

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