
import streamlit as st
st.title("Fill the form for lottery")
st.subheader("(Note: This website is only for making a website for study demo test don't fill your personal information here)")
name = st.text_input("Enter your name :")
Fname = st.text_input("Enter your father's name :")
adr = st.text_input("Enter your address :")
classdata = st.selectbox("Enter your class :", (1,2,3,4,5,6,7,8,9,10,11,12))
tc= st.text_input("Are you of more than 18+ and accepts the Terms and Conditions:")

button =st.button("Sumbit & done")
if button :
    st.markdown(f"""
                Name : {name}
                Father Name : {Fname}
                address : {adr}
                class : {classdata}""")