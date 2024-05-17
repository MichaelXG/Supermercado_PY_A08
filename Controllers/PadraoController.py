'''
Class for do PadraoController
'''
import Utils as ut
import pandas as pd 
import streamlit as st

# criar lista de Login
login = []

login = [{"Apelido":'Suporte',"Password": '123'},
         {"Apelido":'Visitante',"Password": 'visitante123'},
         {"Apelido":'Maria',"Password": 'Maria@123'}
        ]
apelidos = ['Suporte', 'Visitante', 'Maria']

# Lista para armazenar as produtos
produtos = [
    "Camiseta", "Calça jeans", "Tênis", "Mochila", "Notebook", "Fones de ouvido",
    "Smartphone", "Relógio", "Óculos de sol", "Garrafa de água", "Câmera", 
    "Console de jogos", "Livros", "Mesa", "Cadeira", "Luminária de mesa", 
    "Caderno", "Estojo", "Marcadores", "Pincéis de pintura", "Tela de pintura", 
    "Violão", "Teclado", "Microfone", "Drone", "Barraca de camping", "Saco de dormir", 
    "Botas de caminhada", "Bússola", "Lanterna", "Bicicleta", "Capacete", "Skate", 
    "Patins", "Bola de basquete", "Bola de futebol", "Taco de beisebol", 
    "Tacos de golfe", "Vara de pescar", "Raquete de tênis", "Roupa de banho", 
    "Protetor solar", "Toalha de praia", "Cesta de piquenique", "Churrasqueira", 
    "Cooler", "Jogos de tabuleiro", "Relógio de parede", "Ferro de passar roupa", 
    "Aspirador de pó", "Vaso de flores", "Chaleira", "Panela de pressão"
]
#  Função para adicionar uma novo veículo
def adicionar_produtos(Descricao):
    produtos.append(Descricao )
    st.write("Produto adicionado com sucesso!")

# Função para listar todas as produtos ou usando um filtro
def listar_produtos(pDescricao):
    if not produtos:
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver produtos
        
    df = pd.DataFrame(produtos, columns=['Produto'])
    df.insert(0, 'ID', range(1, len(df) + 1))
    
    # Aplicar os filtros
    if (pDescricao is None or pDescricao == ''):
        df_filtrado = df
    else:
         # Produtos que começam com a string de busca
        inicio = df[df['Produto'].str.lower().str.startswith(pDescricao.lower())]
    
        # Produtos que contêm a string de busca
        contem = df[df['Produto'].str.lower().str.contains(pDescricao.lower())]
    
        # Remover duplicatas mantendo a ordem
        df_filtrado = pd.concat([inicio, contem]).drop_duplicates().reset_index(drop=True)
    
    return df_filtrado

