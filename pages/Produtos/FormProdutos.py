import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
    
def Form_Produtos():  
    if "widget" not in st.session_state:
        st.session_state.widget = ""

    if 'Descricao' not in st.session_state:
        st.session_state.Descricao = ''
    
    ut.Divisor('Adicionar Produto', 'cart-plus', 'rgb(20,80,90)', 'key_produto1')

    with st.form(key = 'form_produto', clear_on_submit = True):
        row_0_col1, row_0_col2 = st.columns([8, 0.01]) 
        row_4_col1, row_4_col2, row_4_col3, row_4_col4, row_4_col5= st.columns([2, 2, 1, 2, 2]) 
        
        # Linha 00
        with row_0_col1:
            st.session_state.Descricao = st.text_input('Descrição', key='key_Descricao')
            if not st.session_state.Descricao:
                st.error('O campo "Descrição" é Obrigatorio.')
        
        with row_0_col2:   
            st.write('') 
        
      
        # Linha 04        
        with row_4_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_4_col2:   
            st.write('')

        with row_4_col1:   
            st.write('')
        
        with row_4_col2:
           st.write('')   
            
        with row_4_col3: 
            form_submit_button_produto = st.form_submit_button('Salvar')
            
        with row_4_col4: 
            st.write('') 
        
        with row_4_col5: 
            st.write('') 
            
        if form_submit_button_produto:
            if st.session_state.Descricao:
                adicionar_produtos(st.session_state.Descricao)           
            else:
                ut.Alerta('','Parametros para incluir um novo produto incompleto')   
    
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_produto2')