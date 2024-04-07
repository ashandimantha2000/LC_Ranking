import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World!")
x=st.text_input("Enter your name")
st.write("Hello",x)

st.write("My Cool Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.bar_chart(chart_data)

