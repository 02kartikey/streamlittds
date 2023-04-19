
pip install streamlit
import streamlit as st
a=st.number_input(input("First Number"))
b=st.number_input(input("Second Number"))
c=st.number_input(input("Third Number"))
if (a>=b) and (a>=c):

  la=a
elif (b>=a) and (b>=c):
  la=b
else:
  la=c
st.write("Largest number", la)