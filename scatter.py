import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hrs & Marks")
st.write("Relation between marks and hrs studied")

hrs = [1, 2, 3, 4, 5, 6, 6.5, 8, 9.5]
score = [40, 50, 52, 60, 62, 56, 70, 80, 90]

fig, ax = plt.subplots()
ax.scatter(hrs, score, color='blue')
ax.set_xlabel('Hrs Studied')
ax.set_ylabel('Marks Obtained')
ax.set_title('Hrs vs Marks Scatter Plot')
st.pyplot(fig)
