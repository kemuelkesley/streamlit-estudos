# Tela de Login
import streamlit as st
import streamlit.components.v1 as components

# Criando tela de Login e Senha

def seleciona():
    with open('assets/css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        with st.form("login"):
            st.markdown("### Login")
            st.text_input("E-mail", placeholder="Digite seu E-mail")
            st.text_input("Senha", placeholder="Digite sua Senha", type="password")
            st.form_submit_button("Login")    