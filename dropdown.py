import streamlit as st

st.title("Dropdown Example")

fruit = st.selectbox("Pick a fruit:",["Apple", "Banana", "Cherry"])
st.write("You chose:", fruit)