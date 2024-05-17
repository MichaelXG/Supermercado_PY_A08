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
    {'ID': 1, 'Nome': 'Café',     'Quantidade': 1,  'Valor': 19.98, 'Total': 19.98},
    {'ID': 2, 'Nome': 'Leite',    'Quantidade': 24, 'Valor': 5.98,  'Total': 143.52}, 
    {'ID': 3, 'Nome': 'Manteiga', 'Quantidade': 2,  'Valor': 11.42, 'Total': 22.84},
    {'ID': 4, 'Nome': 'Sal',      'Quantidade': 1,  'Valor': 4.59,  'Total': 4.59},     
    {'ID': 5, 'Nome': 'Macarrão', 'Quantidade': 2,  'Valor': 3.25,  'Total': 6.50}, 
    {'ID': 6, 'Nome': 'Feijão',   'Quantidade': 3,  'Valor': 8.99,  'Total': 26.97},  
    {'ID': 7, 'Nome': 'Farinha',  'Quantidade': 1,  'Valor': 6.45,  'Total': 6.45},  
    {'ID': 8, 'Nome': 'Tapioca',  'Quantidade': 2,  'Valor': 5.73,  'Total': 11.46},
    {'ID': 9, 'Nome': 'Açúcar',   'Quantidade': 1,  'Valor': 13.4,  'Total': 13.4},     
    {'ID': 10,'Nome': 'Azeite',   'Quantidade': 2,  'Valor': 39.89, 'Total': 79.78}, 
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

# Função para formatar money
def format_money(valor):
    if isinstance(valor, (int, float)):
        return 'R$ {:,.2f}'.format(valor).replace(',', 'v').replace('.', ',').replace('v', '.')
    return valor

# Função para estilizar o DataFrame
def style_df(df):
    # Cálculo da soma do valor total de todos os produtos
    valor_total_geral = df['Total'].sum()
    # Criar uma linha de rodapé com a soma do valor total
    rodape = pd.DataFrame({'ID': [''], 'Nome': ['Total Geral:'], 'Quantidade': [''], 'Valor': [''], 'Total': [valor_total_geral]})
    # Concatenar a linha de rodapé ao DataFrame original
    df_com_rodape = pd.concat([df, rodape], ignore_index=True)
    
    # Aplicar os estilos
    styled_df = df_com_rodape.style.apply(zebra_style, axis=1)
    
    # Alinhar colunas à direita
    styled_df = styled_df.set_properties(**{'text-align': 'right'}, subset=['Quantidade', 'Valor', 'Total'])
    
    # Aplicar formatação monetária às colunas de valor, exceto na última linha (rodapé)
    styled_df = styled_df.format({
        'Valor': format_money,
        'Total': format_money
    })
    
    # Formatar a coluna 'Quantidade' sem aplicar ao rodapé
    styled_df = styled_df.format({
        'Quantidade': '{:.2f}'
    }, subset=pd.IndexSlice[:-1, ['Quantidade']])
    
    # Estilizar o rodapé em negrito e aplicar a formatação monetária no rodapé
    styled_df = styled_df.set_table_styles([{
        'selector': 'tr:last-child',
        'props': [('font-weight', 'bold')]
    }])

    return styled_df

# Função para adicionar um novo produto a lista
def adicionar_produtos(Nome, Quantidade, Valor_Unitario):
    # Verificar se o produto já existe na lista 
    for produto in lista_produtos:
        if (produto['Nome'].lower() == Nome.lower()):
            ut.Erro('', f'Produto "{Nome}" já existe na lista!')
            return

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
        # Produtos que começam com a string de busca
        inicio = df_filtrado[df_filtrado['Nome'].str.lower().str.startswith(pNome.lower())]
        # Produtos que contêm a string de busca
        contem = df_filtrado[df_filtrado['Nome'].str.lower().str.contains(pNome.lower())]
        # Remover duplicatas mantendo a ordem
        df_filtrado = pd.concat([inicio, contem]).drop_duplicates().reset_index(drop=True)
    
    return df_filtrado

def deletar_registro(ID_produto: int) -> bool:
    try:
        st.write(ID_produto)
        ID_produto = int(ID_produto)
    except ValueError:
        ut.Erro("", "O ID do produto deve ser um número inteiro.")
        return False
    
    for i, produto in enumerate(lista_produtos):
        if produto['ID'] == ID_produto:
            del lista_produtos[i]
            ut.Sucesso('', f'Produto com ID {ID_produto} foi removido com sucesso.')
            return True
    
    if ID_produto not in lista_produtos:
        return True

def alterar_produto(ID, novo_nome, nova_quantidade, novo_valor):
    for produto in lista_produtos:
        if produto['ID'] == ID:
            produto['Nome'] = novo_nome
            produto['Quantidade'] = nova_quantidade
            produto['Valor'] = novo_valor
            produto['Total'] = nova_quantidade * novo_valor
            ut.Sucesso('', f'Produto "{novo_nome}" alterado com sucesso!')
            return True
    ut.Erro('', f'Produto com ID {ID} não encontrado.')
    return False