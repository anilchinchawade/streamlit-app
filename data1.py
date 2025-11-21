import streamlit as st
import pandas as pd
import matplotlib as plt

st.title('Student Performance Analysis')
st.write('Upload a csv file containing student data')

# File upload
uploaded_file = st.file_uploader('Choose File', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Raw Data')
    st.dataframe(df)
