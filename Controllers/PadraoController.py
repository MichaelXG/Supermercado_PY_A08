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
lista_produtos = [    
    {'ID': 1, 'Nome': 'Café',     'Quantidade': 25, 'Valor': 15.34, 'Total': 383.5},
    {'ID': 2, 'Nome': 'Leite',    'Quantidade': 26, 'Valor': 28.1,  'Total': 730.6}, 
    {'ID': 3, 'Nome': 'Manteiga', 'Quantidade': 72, 'Valor': 11.42, 'Total': 822.24},
    {'ID': 4, 'Nome': 'Sal',      'Quantidade': 94, 'Valor': 24.32, 'Total': 2286.08},     
    {'ID': 5, 'Nome': 'Macarrão', 'Quantidade': 79, 'Valor': 10.13, 'Total': 800.27}, 
    {'ID': 6, 'Nome': 'Feijão',   'Quantidade': 68, 'Valor': 31.51, 'Total': 2142.68},  
    {'ID': 7, 'Nome': 'Farinha',  'Quantidade': 26, 'Valor': 36.66, 'Total': 953.16},  
    {'ID': 8, 'Nome': 'Macarrão', 'Quantidade': 47, 'Valor': 28.73, 'Total': 1350.31},
    {'ID': 9, 'Nome': 'Açúcar',   'Quantidade': 33, 'Valor': 27.4,  'Total': 904.2},     
    {'ID': 10,'Nome': 'Azeite',   'Quantidade': 68, 'Valor': 28.6,  'Total': 1944.8}, 
]
# Função para gerar nova ID
def gerar_id_produto():
    if lista_produtos:
        novo_id = max(produto['ID'] for produto in lista_produtos) + 1
    else:
        novo_id = 1
    return novo_id

# Função para estilizar linhas alternadas
def zebra_style(row):
    return ['background-color: #f2f2f2' if row.name % 2 == 0 else '' for _ in row]

# Função para formatar no padrão brasileiro
def format_money(valor):
    return 'R$ {:,.2f}'.format(valor).replace(',', 'v').replace('.', ',').replace('v', '.')

# Função para estilizar o DataFrame
def style_df(df):
    # Cálculo da soma do valor total de todos os produtos
    valor_total_geral = df['Total'].sum()
    # Criar uma linha de rodapé com a soma do valor total
    rodape = pd.DataFrame({'ID': [''], 'Nome': ['Total geral'], 'Quantidade': [''], 'Valor': [''], 'Total': [valor_total_geral]})
    # Concatenar a linha de rodapé ao DataFrame original
    df_com_rodape = pd.concat([df, rodape], ignore_index=True)
    
    # Aplicar os estilos
    styled_df = df_com_rodape.style.apply(zebra_style, axis=1)
    styled_df = styled_df.set_properties(**{'text-align': 'right'}, subset=['Quantidade', 'Valor', 'Total'])
    # styled_df = styled_df.format({
    #     'Quantidade': '{:.2f}',
    #     'Valor': format_money,
    #     'Total': format_money
    # })
    return styled_df

    # # Aplicar os estilos
    # styled_df = df.style.apply(zebra_style, axis=1)
    # styled_df = styled_df.set_properties(**{'text-align': 'right'}, subset=['Quantidade', 'Valor', 'Total'])
    # styled_df = styled_df.format({
    #     'Quantidade': '{:.2f}',
    #     'Valor': format_money,
    #     'Total': format_money
    # })
    # return styled_df

#  Função para adicionar uma novo veículo
def adicionar_produtos(Nome, Quantidade, Valor_Unitario):
    produto = {
        "ID": gerar_id_produto(),
        "Nome": Nome,
        "Quantidade": round(Quantidade, 2),
        "Valor": round(Valor_Unitario, 2),
        "Total": round(Valor_Unitario * Quantidade, 2)
    } 
    lista_produtos.append(produto)
    ut.Sucesso('', f'Produto "{Nome}" adicionado com sucesso!')

# Função para listar todas as produtos ou usando um filtro
def listar_produtos(pID=None, pNome=None):
    if not lista_produtos:
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver produtos
    
    # Criar um DataFrame
    df = pd.DataFrame.from_dict(lista_produtos)
    
    # Aplicar os filtros
    df_filtrado = df.copy()
    
    if pID is not None and pID != 0:
        df_filtrado = df_filtrado[df_filtrado['ID'] == pID]
    
    if pNome:
        # Alunos que começam com a string de busca
        inicio = df_filtrado[df_filtrado['Nome'].str.lower().str.startswith(pNome.lower())]
        # Alunos que contêm a string de busca
        contem = df_filtrado[df_filtrado['Nome'].str.lower().str.contains(pNome.lower())]
        # Remover duplicatas mantendo a ordem
        df_filtrado = pd.concat([inicio, contem]).drop_duplicates().reset_index(drop=True)
    
    return df_filtrado

def deletar_registro(ID_produto: int) -> bool:
    try:
        st.write(ID_produto)
        ID_produto = int(ID_produto)
    except ValueError:
        ut.Erro("", "o ID do produto deve ser um número inteiro.")
        return False
    
    if ID_produto in lista_produtos:
        del lista_produtos[ID_produto]
        return True
    
    if ID_produto not in lista_produtos:
        return True
