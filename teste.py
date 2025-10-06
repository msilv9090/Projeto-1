import streamlit as st 

st.write("Alô mundo")
st.tittle("Meu programa")

nome = st.text_input("Digite o seu nome: ")
if nome:
   st.write(nome.upper())
