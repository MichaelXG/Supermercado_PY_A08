import streamlit as st
import Utils as ut

def Create_Home():  
    with st.container(): 
        ut.Divisor('Supermercado - Lista de Compras', 'cart4','rgb(20,80,90)', 'Home01')
        st.write('\n \n')
        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            st.write('          ')

        with col2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrf1jDiORK0k7CpWajthVYhUI3YP-0bNQKpg&usqp=CAU', width=200,  use_column_width='auto') 
            
            st.markdown("""**[PY-A08]** Você está desenvolvendo um programa para gerenciar uma lista de compras. O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista. Além disso, o programa calcula o valor total de todos os produtos da lista.
                        \n **O programa oferece as seguintes opções:** 
                        \n **Adicionar produtos:** O usuário pode adicionar um novo produto à lista informando o **nome**, a **quantidade** e o **valor unitário** do produto. O programa calcula automaticamente o valor total do produto **(quantidade * valor unitário)** e atualiza o valor total de todos os produtos.
                        \n **Ver a lista de produtos:** O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.
                        \n **Atualizar produtos:** O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.
                        \n **Remover produto:** O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.
                        \n **Encerrar programa:** Encerra a execução do programa.
                        \n O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: **"produto"**, **"valor"**, **"quantidade"** e **"total"**. 
                        \n A variável **totalProdutos** é utilizada para armazenar o valor total de todos os produtos da lista.
                        \n A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.
                    """)
        
        with col3:
            st.write('')
        
        st.write('\n \n')
        ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'Home02')
