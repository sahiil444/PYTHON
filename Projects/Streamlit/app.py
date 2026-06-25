import streamlit as st

st.title('Welcome To World Of Languages')
language = st.selectbox("Select your language",['C','C++','JAVA','Python','javaScript'])
st.write(f"Your choise {language}. Excellent")
st.success('You correctly registered')
st.text('See you soon')


