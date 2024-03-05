import streamlit as st
import pandas as pd

st.write("Hello world!")
st.markdown("This is _italics_ and this is **bold**")
st.title("This is my first title")
st.header("This is a header :)")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
st.dataframe(df)