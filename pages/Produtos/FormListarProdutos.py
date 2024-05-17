import streamlit as st
from Controllers.PadraoController import *
import Utils as ut

def Form_ListarProdutos(pDescricao):  
    
    ut.Divisor('Listar Produtos', 'clipboard2-data', 'rgb(20,80,90)', 'ListarProdutos01')

    with st.container(border=True):
        # Chama a função listar_Produtoss com os filtros selecionados
        df_filtrado = listar_produtos(pDescricao)

        # Mostra as Produtoss filtradas em um DataFrame do Pandas
        if not df_filtrado.empty:
            st.dataframe(df_filtrado, hide_index=True)
        else:
            st.write("Não há Produtos correspondentes aos filtros selecionados.")
           
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'ListarProdutos02')