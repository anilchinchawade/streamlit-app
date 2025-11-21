import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the Streamlit app
st.title("Simple Line Chart Example")

# Create some sample data using Pandas DataFrame
# The index of the DataFrame will be used as the x-axis by default
# Each column will represent a separate line on the chart
data = {
    'Time': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']),
    'Value A': [10, 12, 8, 15, 11],
    'Value B': [5, 7, 10, 6, 9]
}
df = pd.DataFrame(data)

# Set 'Time' column as the index for plotting
df = df.set_index('Time')

# Display the DataFrame (optional)
st.write("Original DataFrame:")
st.dataframe(df)

# Create the line chart
st.write("Line Chart:")
st.line_chart(df)

# Example with specific x and y columns
# If you don't want to use the index as x, you can specify x and y
st.write("Line Chart with specified x and y:")
df_reset = df.reset_index()  # Reset index to use 'Time' as a regular column
st.line_chart(df_reset, x='Time', y=['Value A', 'Value B'])
