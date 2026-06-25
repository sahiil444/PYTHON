import streamlit as st
from datetime import date

st.title('Welcome To Age Predicter')
st.subheader('We Can Predict Your Age')
dob = st.date_input('Enter Your Age')
st.write(f"Your current age {dob}")
today = date.today()


if dob > today:
    st.write(f"BSDK Future se aya hai kya !!!!!!!")
else:
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Your age.{age}")
