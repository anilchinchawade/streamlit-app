import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Subject-wise students data")
st.write("This applicationis giving my different marks")

data = {'Subjects': ["DS", "DBMS", "DAA", "TOC"], 'Marks': [85, 78, 56, 45]}

df = pd.DataFrame(data)

st.subheader('Student Marks')

df.set_index('Subjects', inplace=True)
st.bar_chart(df)
