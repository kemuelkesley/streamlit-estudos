import streamlit as st;
import Controllers.ClienteController as ClienteController
import pandas as pd


def List():
    # Criando colunas e seus tamanhos
    colms = st.columns((1, 2, 1, 2, 1, 1))
    # Criando os titulos das colunas.
    campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar'] 
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in ClienteController.selecionar_todos():
        col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
        
        col1.write(item.id) 
        col2.write(item.nome) 
        col3.write(item.idade) 
        col4.write(item.profissao) 

        #Botão Excluir
        button_space_excluir = col5.empty()
        on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' +  str(item.id))
        
        # Botão Alterar.
        button_space_alterar = col6.empty()
        on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' +  str(item.id))

        if on_click_excluir:
            ClienteController.excluir(item.id)
        
        # if on_click_alterar:
        #     st.experimental_get_query_params(
        #         id=[item.id]
        #     )
    # Listando todos os clientes que estão no banco de dados.
    # st.title("Lista de Clientes")

    # # Criando uma lista vazia
    # costumer_list = []

    # # Adicionando cada item na lista
    # for item in ClienteController.selecionar_todos():
    #     costumer_list.append([item.nome, item.idade, item.profissao])
    #     print(costumer_list)


    # # Criando um DataFrame com Pandas
    # df = pd.DataFrame(
    #     costumer_list,
    #     columns=['Nome', 'Idade', 'Profissão']
    # )

    # # st.table(df)
    # st.dataframe(df)
