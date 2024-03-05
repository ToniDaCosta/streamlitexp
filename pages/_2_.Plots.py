import streamlit as st
import src.manage_data as cleaning
import plotly.express as px
import codecs
import streamlit.components.v1 as components
import pandas as pd

# 1. Create a bar chart


st.write("""
# Plotting page""")
data_bar = cleaning.bar_1()
st.bar_chart(data_bar)
df = cleaning.load_dataframe()
characters = list(df["character_name"].unique()) # all the characters
person = st.selectbox("Choose one character", characters)
                      
data_for_plot = cleaning.graph(person)
fig = px.line(data_for_plot, y="polarity")
st.plotly_chart(fig)


#Tableau map

f = codecs.open("data/tableau.html", "r")
tableau = f.read()

components.html(tableau, height=500, scrolling=True)
