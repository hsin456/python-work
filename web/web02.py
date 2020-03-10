import streamlit as st
import pandas as pd

df=pd.DataFrame({
    "A":[56,88,4],
    "B":[94,12,61]
})

st.write(df)