import streamlit as st
import src.manage_data as cleaning
import pandas as pd

df = cleaning.load_dataframe()

st.write("Adventure time in data")
st.dataframe(df)

