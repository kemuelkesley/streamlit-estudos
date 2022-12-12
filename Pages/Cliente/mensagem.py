# Tela de Login
import streamlit as st
import streamlit.components.v1 as components

# Criando tela de Login e Senha

def criar_mensagem():
    with st.form(key="include_mensagem", clear_on_submit=True):

        st.title("Mensagem")
        
        input_email = st.text_input(label="E-mail:" ,placeholder="Informe seu e-mail")
        input_texto = st.text_area(label="Escreva aqui:", placeholder="Escreva aqui.")

        botao = st.form_submit_button(label="Enviar", disabled=False)

        if not input_email:
            st.warning("Por favor coloque o seu email.")          
            st.stop()
        st.success("Muito obrigado.")    
        if not input_texto:
            st.warning("Por favor coloque o seu texto.")
            st.stop()
        st.success("Muito obrigado.")    

        # if button:
        #     # st.sidebar.success("Dados incluidos com sucesso.")
        #     st.success("Enviado com sucesso.")
        #     st.success(f"E-mail:{input_email}")
        #     st.success(f"Mensagem:{input_texto}")


      
