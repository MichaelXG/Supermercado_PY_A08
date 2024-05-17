import streamlit as st

class NavegadorRegistros:
    
    def __init__(self, dados):
        if isinstance(dados, list) and all(isinstance(item, dict) for item in dados):
            self.registros = dados
            self.indice_atual = 0 if self.registros else None
        else:
            raise ValueError("O argumento 'dados' deve ser uma lista de dicionários.")
        
    def editar(self, index_n: int):
        if self.registros:
            self.indice_atual = index_n
            st.session_state.index = self.indice_atual
            return self.registros[self.indice_atual]  
    
    def refresh(self, index_n: int):
        if self.registros:
            self.indice_atual = index_n
            st.session_state.index = self.indice_atual
            return self.registros[self.indice_atual]  
    
    def first_registro(self):
        if self.registros:
            self.indice_atual = 0
            st.session_state.index = self.indice_atual
            return self.registros[self.indice_atual]

    def registro_prior(self, index_n):
        if self.registros and index_n > 0:
            self.indice_atual = index_n - 1
            st.session_state.index = self.indice_atual
            return self.registros[self.indice_atual]

    def next_registro(self, index_n):
        if self.registros and index_n < len(self.registros) - 1:
            self.indice_atual = index_n + 1
            st.session_state.index = self.indice_atual
            return self.registros[self.indice_atual]

    def last_registro(self):
        if self.registros:
            self.indice_atual = len(self.registros) - 1
            st.session_state.index = self.indice_atual
            return self.registros[self.indice_atual]
