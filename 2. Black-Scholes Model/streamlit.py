import streamlit as st
import pandas as pd
import numpy as np

st.title("This is a Cool Title")
st.header("This is a header")
st.subheader("This is a sub-header")
st.text("This is a text that developers use inplace of paragraph tag")

st.title("Another Title")

st.write("Creating a Table")
st.write(pd.DataFrame(
    {
        "firstColumn": [1, 2, 3, 4],
        "secondColumn": [5, 6, 7, 8]
    }
))

"Hello This is a random text without any function"

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)