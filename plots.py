import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

chart_data=pd.DataFrame(np.random.randn(20,2),columns=["line-1","line-2"])
st.subheader("plotting the line chart")
st.line_chart(chart_data)

st.subheader("plotting the Area chart")
st.area_chart(chart_data)

st.subheader("plotting the Bar chart")
st.bar_chart(chart_data)

st.subheader("Data visualization with matplotlib and seaborn")
# st.subheader("plotting the Area chart")
# st.area_chart(chart_data)
df=pd.read_csv('C:\\Users\Kondu\OneDrive\Desktop\streamlit\iris.csv')
st.dataframe(df)

# fig=plt.figure(figsize=(15,8))
# df["species"].value_counts().plot(kind="bar")
# st.pyplot(fig)

fig=plt.figure(figsize=(15,8))
df["species"].value_counts().plot(kind="bar")
st.pyplot(fig)

fig=plt.figure(figsize=(15,8))
sns.distplot(df["sepal_length"])
st.pyplot(fig)

st.header("3. mulitple graphs")
col1,col2=st.columns(2)
with col1:
    col1.header="KDE =False"
    fig1=plt.figure()
    sns.distplot(df["sepal_length"])
    st.pyplot(fig1)
with col2:
    col2.header="Hist =False"
    fig2=plt.figure()
    sns.distplot(df["sepal_length"],hist=False)
    st.pyplot(fig2)

col1,col2=st.columns(2)
with col1:
    fig1=plt.figure()
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df["petal_length"],hist=False)
    st.pyplot(fig1)
with col2:
    fig2=plt.figure()
    sns.set_theme(context="poster",style="darkgrid")
    sns.distplot(df["petal_length"],hist=False)
    st.pyplot(fig2)


st.header("Exploring different types of graphs")
st.subheader("Scatter Plot")
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("box plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x="species",y="petal_length")
st.pyplot(fig)

st.subheader("count plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x="species")
st.pyplot(fig)


st.subheader("violin plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="species",y="petal_length")
st.pyplot(fig)
