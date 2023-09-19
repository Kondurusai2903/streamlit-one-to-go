import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
# import matplotlib.pyplot as plt
# import seaborn as sns

st.header("1.Altair Scatter Plot")
chart_data=pd.DataFrame(np.random.randn(500,5),columns=["a","b","c","d","e"])
chart=alt.Chart(chart_data).mark_circle().encode(x="a",y="b",size="c",
                tooltip=["a","b","c","d","e"])
st.altair_chart(chart)
