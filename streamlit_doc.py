import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header("I am learning streamlit")
st.subheader("SRK")

st.write("nothing")
st.markdown("""
 ### Fav Movies
 - Sita Ramam
 - Asur
 - Stranger Things
""")

st.code("""
 def foo(input):
     return foo**2

x=foo(2)     
""")

st.latex("X^2 + Y^2 +2=0")

df = pd.DataFrame({
    'name': ['sourav', 'som', 'sagnik'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})
st.dataframe(df)
st.metric('Revenue', 'Rs 3L', '3%')

st.json({
    'name': ['sourav', 'som', 'sagnik'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})
st.image('Coding.jpg')
st.sidebar.title("side title")

col1, col2 = st.columns(2)

with col1:
    st.image('Coding.jpg')

with col2:
    st.image('Elon Musk (1).jpg')

st.error("login failed")
st.success("Login Sucessful")
st.info("info")
st.warning("warning")

bar = st.progress(0)

for i in range(1, 101):
    # time.sleep(0.1)
    bar.progress(i)
email = st.text_input("Enter Email")
age = st.number_input("enter age")
date = st.date_input("enter date")

email=st.text_input("enter email")
password=st.text_input("enter password")
gender=st.selectbox("select gender",["Male","Female","Others"])
cond=st.button("login karo")

if cond:
    if email == "sd309382@gmail.com" and password == "1234":
        st.success("login sucessfully")
        st.write(gender)
        st.balloons()
    else:
        st.error("login failed")


file =st.file_uploader("upload a csv file")

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())