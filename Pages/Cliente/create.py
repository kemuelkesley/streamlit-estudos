import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


def create():
    # id_alteracao = st.experimental_get_query_params()
    # st.write(id_alteracao)
    # Titulo 
    st.title("Adicionar Cliente")

    # Dados de entradas do formulario
    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Insira seu Nome", placeholder="Nome Completo ")
        input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
        input_occupation = st.selectbox("Selecione sua Profissão", options=["Selecione" ,"Desenvolvedor", "Músico", "Designer", "Professor"])
        input_button_submit = st.form_submit_button("Enviar")


    # Capturando os dados preenchidos pelo cliente.
    if input_button_submit:    
        ClienteController.incluir(cliente.Cliente(0, input_name, input_age, input_occupation)) 

        # Mensagem que tudo ocorreu bem.
        st.success("Cliente incluido com Sucesso.")
