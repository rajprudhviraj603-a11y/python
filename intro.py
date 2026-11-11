import streamlit as st
st.title("my first streamlit app created by prudhvi raj")
st.write("welcome! this app calculates the square of a number.")
st.header("select a number")
number = st.slider("pick a number", 0, 0, 5)
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")