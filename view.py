from tkinter import messagebox
import sqlite3 as lite
import pandas as pd
import os

con = lite.connect('dados/dados_vendas.db')



'''###################################################################################
############################  CRIANDO  BANCO DE DADOS #########################'''

def criando_database():
    con = lite.connect('dados/dados_vendas.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE vendas(id INTEGER PRIMARY KEY AUTOINCREMENT, Produto TEXT, Marca TEXT, Data DATE, Hora TEXT, F_Pagamento TEXT,Valor DECIMAL)")

'''###################################################################################
############################  INSERIR DADOS NO BANCO DE DADOS #########################'''

def inserir_dados(i):
    con = lite.connect('dados/dados_vendas.db')
    with con:
        cur = con.cursor()
        query = ("INSERT INTO vendas(Produto, Marca, Data, Hora, F_Pagamento ,Valor) VALUES(?,?,?,?,?,?)")
        cur.execute(query, i)
        
'''#####################################################################################
###########################   VER DADOS DO BANCO DE DADOS  ##############################'''

def ver_dados():
    con = lite.connect('dados/dados_vendas.db')
    ver_dados =[]
    with con:
        cur = con.cursor()
        query = ("SELECT *  FROM vendas")
        cur.execute(query)
        
        rows = cur.fetchall()
        
        for row in rows:
            ver_dados.append(row)
        return ver_dados
'''######################################################################################
###########################    DELETAR DADOS DO BACO DE DADOS ############################'''

def deletar_dados(i):
    con = lite.connect('dados/dados_vendas.db')
    with con:
        cur = con.cursor()
        query = "DELETE FROM vendas WHERE id=?"
        cur.execute(query, i)
        
'''######################################################################################
##########################    ATUALIZAR DADOS DO BANCO DE DADOS #########################'''

##dados = ['Bermuda ', 'Jans', '16/05/2023', '03:52:56', 'Dinheiro', '200', 1]


def atualizar_dados(i):
    con = lite.connect('dados/dados_vendas.db')
    with con:
        cur = con.cursor()
        query = "UPDATE vendas SET Produto=?, Marca=?, Data=?, Hora=?, F_Pagamento=? ,Valor=?  WHERE id=?"
        cur.execute(query, i)
        
        
def inserir_excel():  
    con = lite.connect('dados/dados_vendas.db')
    with con:  
        query = "SELECT * FROM vendas"
        dados = pd.read_sql_query(query, con)
        
        
        total_venda = dados['Valor'].sum()
        
        dados['Total R$'] = ''
        
        dados.loc[0, 'Total R$'] = total_venda
        dados.to_excel('Dados Vendas.xlsx', index=False)


'''###################################################################################
############################  DELETAR BANCO DE DADOS #########################'''


def deletando_database():
    con.close()
    database_ = 'dados/dados_vendas.db'
    if os.path.exists(database_):
        os.remove(database_)
    else: 
        ...
