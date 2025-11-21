import streamlit as st
st.title('Student Enrollment Page')
subjects = st.multiselect(
    'Select Subjects', ['Maths', 'Science', 'Biology', 'Physics'])
st.write()
