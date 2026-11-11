
import streamlit as st
import pandas as pd
def read_file(file):
    try:
        file.seek(0)
        df= pd.read_csv(
            file,
            on_bad_lines="error",
        )
        if df.empty:
            st.error("Your CSV has no data.")
            return None
        return df
    except pd.errors.EmptyDataError:
        st.error("Your CSV file is empty or has no headers.")
    except pd.errors.ParserError:
        st.error("Malformed CSV.")
    except OSError:
        st.error("Unable to read this file.")
    except Exception:
        st.error("Something went wrong while processing your CSV.")
    return None
