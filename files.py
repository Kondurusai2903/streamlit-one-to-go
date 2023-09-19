import streamlit as st
import pandas as pd
st.subheader("uploading the csv File")
file=st.file_uploader("upload the csv file",type=["csv","xlsl"])
data=pd.read_csv('C:\\Users\Kondu\OneDrive\Desktop\streamlit\Products.csv')
if data is not None:
    st.table(data.head())
# if file is not None:
#     st.

st.subheader("uploding the image file")
image_file  =st.file_uploader("upload the image file",type=["png"])
if image_file is not None:
    st.image(image_file)


st.subheader("uploding the video file")
video_file  =st.file_uploader("upload the image file",type=["mp4"])
if video_file is not None:
    st.video(image_file,start_time=0)


st.subheader("uploding the audio file")
audio_file  =st.file_uploader("upload the audio file",type=["mp3"])
if audio_file is not None:
    st.audio(audio_file.read())
