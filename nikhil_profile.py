import streamlit as st


st.set_page_config(page_title="My Profile", page_icon=":tada:", layout="wide")
from PIL import Image
img = Image.open("etcc.etcc.jpg")
st.image(img, width=200)
st.title("Hi, I am Nikhil Lanjewar😎️")
st.subheader("--Student|Dreamer--")
st.write("--Currently pursuing B.TECH Degree--")
st.write("S.B.Jain Institue of Technology Management and Research,Nagpur")
st.write("I am passionate about finding ways to solve problems")
st.write("[learn more with source Codes-github>](https://github.com/nikhillanjewar)")

