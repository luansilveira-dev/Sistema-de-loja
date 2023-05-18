from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from view import *
import datetime 
'''
Identificação básica do cliente: Nome completo do cliente.

Detalhes da venda: Data da venda, número do pedido e forma de pagamento.

Produtos vendidos: Descrição do produto, quantidade e preço total.

Registro de vendas: Manter um histórico simples das vendas realizadas, incluindo informações sobre produtos e valores.

'''
data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year
    
formas_de_pagamento = [
    "Dinheiro",
    "PIX",
    "Cartão de crédito",
    "Cartão de débito",
    "Transferência bancária",
    "Boleto bancário",
    "PayPal",
    "Carteiras digitais"]
## CORES
roxo_escuro = '#27032A'
roxo = '#4B083D'
branco = '#FBFBF2'
branco_ = '#FFFDD9'
verde = '#23A80C'
vermelho = '#BE2028'
azul_claro = '#46B3FB'
laranja = '#E36433'

janela = Tk()
janela.title('')
janela.iconbitmap('img/logo.ico')
janela.geometry('1080x600')
janela.configure(background=roxo)
janela.resizable(width=FALSE, height=FALSE)


style = ttk.Style(janela)
style.theme_use('clam')
style.configure('BotaoClicado.TButton', background='#23A80C', foreground=roxo)


frame_titulo = Frame(janela, width=1078, height=50, bg=branco_ ,relief=FLAT)
frame_titulo.grid(column=0, row=0, pady=1)

frame_form = Frame(janela, width=1078, height=303, bg=branco_, pady=20, relief=FLAT )
frame_form.grid(column=0, row=1, padx=0, pady=1, sticky=NSEW)

frame_tabela = Frame(janela, width=1078, height=300, bg=branco, relief=FLAT)
frame_tabela.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)


'''##############################################################################
###############################  FUNÇÕES PRINCIPAIS  ############################
#################################################################################'''
global tree


def criar_banco_():
    pass
###### Função de menu configuraçêos avançadas 
def abrir_conf():
    janela_conf = Tk()
    janela_conf.title('')
    janela_conf.iconbitmap('img/logo.ico')
    janela_conf.geometry('720x300')
    janela_conf.resizable(width=FALSE, height=FALSE)

    
    frame_conf = Frame(janela_conf, width=800, height=600, bg=branco, relief=FLAT, pady=0)
    frame_conf.grid(column=0, row=0)
    
    
    def deletar_banco_():
        try:
            resposta = messagebox.askokcancel("Atenção", "Tem certeza de que deseja excluir o banco de dados? Essa ação é irreversível e todos os dados serão perdidos.")
            if resposta:
                deletando_database()
                criando_database()
                janela_conf.destroy()
                messagebox.showinfo("Sucesso", "O banco de dados foi excluído com sucesso!")
                mostrar_tabela()
                
            
        except:
            ...
    
    mensagem = "O botão 'Deletar Banco de Dados' irá deletar permanentemente o  banco de dados existente. \n E automaticamente irá criar um novo banco de dados vazio."
   
    Label(janela_conf,justify='center' ,text='ATENÇÂO', width=500,font='Arial 12 bold', anchor=NW, compound=LEFT, bg=branco, fg=vermelho).place(x=300, y=10)
    
    Label(janela_conf,justify='center' ,text=mensagem, width=500,font='Arial 12 bold', anchor=NW, compound=LEFT, bg=branco, fg=roxo_escuro).place(x=10, y=40)
    
    
    Button(frame_conf, command=deletar_banco_, text='Deletar \nbanco de dados'.upper(), font='Ivy 11 bold', width=20, bg=vermelho, fg=branco).place(x=250, y=200)
    

### função de de INSERIR DADOS 
def inserir(): 
    produto = entry_produto.get()
    marca  = entry_marca.get()
    data_venda = f"{dia:02d}/{mes:02d}/{ano}"
    hora_venda = datetime.datetime.now().strftime("%H:%M")
    formas_pagamento = entry_F_pagamento.get()
    valor = entry_valor.get()

    if marca == '':
        marca = '-'
    
    lista_inserir = [produto, marca, data_venda, hora_venda ,formas_pagamento, valor]
    
    for i in lista_inserir:
        if i  == '':
            messagebox.showerror('', 'Erro: Preencha todos os campos. (Marca não é obrigatória)')
            return
    
    inserir_dados(lista_inserir)
    messagebox.showinfo('', 'Sucesso: Venda foi realizada com sucesso!!!')
    
    entry_produto.delete(0, 'end')
    entry_marca.delete(0, 'end')
    entry_F_pagamento.delete(0, 'end')
    entry_valor.delete(0, 'end')
    
    entry_F_pagamento.current(0)
    
    mostrar_tabela()

## Função de deletar dados 

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        
        valor = treev_lista[0]
        deletar_dados([valor])
        mostrar_tabela()
        messagebox.showinfo('','Sucesso: Os dados foram deletados com sucesso.')
        
    except IndexError:
        messagebox.showerror('', 'Erro: Selecione um item da tabela que deseja deletar.')
     
### Função atualizar dados

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        
        
        entry_produto.delete(0, 'end')
        entry_marca.delete(0, 'end')
        entry_F_pagamento.delete(0, 'end')
        entry_valor.delete(0, 'end')
        
        id = int(treev_lista[0])
        
        entry_produto.insert(0, treev_lista[1])
        entry_marca.insert(0, treev_lista[2])
        entry_F_pagamento.insert(0, treev_lista[5])
        entry_valor.insert(0, treev_lista[6])
        
        def update():
            
            produto = entry_produto.get()
            marca  = entry_marca.get()
            data_venda = f"{dia:02d}/{mes:02d}/{ano}"
            hora_venda = datetime.datetime.now().strftime("%H:%M")
            formas_pagamento = entry_F_pagamento.get()
            valor = entry_valor.get()
            
            if marca == '':
                marca = '-'
            lista_atualizado = [produto, marca, data_venda, hora_venda ,formas_pagamento, valor, id]
            
            for i in lista_atualizado:
                if i == '':
                    messagebox.showerror('', 'Erro: Preencha todos os campos. (Marca não é obrigatória)')
                    return
            
            entry_produto.delete(0, 'end')
            entry_marca.delete(0, 'end')
            entry_F_pagamento.delete(0, 'end')
            entry_valor.delete(0, 'end')
            
            
            messagebox.showinfo('', 'Sucesso: Os dados foram atualizados.')
            atualizar_dados(lista_atualizado)
            entry_F_pagamento.current(0)
            button_update.destroy()
            mostrar_tabela()
            
        button_update = Button(frame_form, command=update, text='Confirmar'.upper(), font='Ivy 11 bold', width=23, height=1, bg=laranja, fg=branco)
        button_update.place(x=130, y=210)
    except IndexError:
        messagebox.showerror('', 'Erro: Selecione um item da tabela.')
        
def salvar_excel():
    try:
        inserir_excel()
        messagebox.showinfo('', 'Sucesso: Os dados foram salvos no Excel.')
    except:
        messagebox.showerror('', 'ERRO: Seu Excel está aberto. Feche-o para salvar os dados.')

img_logo = Image.open('img/logo.png')
img_logo = img_logo.resize((40,40))
img_logo = ImageTk.PhotoImage(img_logo)



logo_titulo = Label(janela, image=img_logo, text='Controle de Vendas'.upper(), font='verdana 20 bold', anchor=NW, compound=LEFT, bg=branco_, fg=roxo_escuro)
logo_titulo.place(x=345, y=2)

'''#####################################################################################
##############################    LABEL E ETRADA DO PROGRAMA  ##########################
########################################################################################'''


## Label dos produtos 
label_produto = Label(frame_form, text='Produto',font='Ivy 11 bold', bg=branco_, fg=roxo_escuro)
label_produto.place(x=15, y=10)
## Entrada dos produtos
entry_produto = Entry(frame_form, width=30, relief=SOLID, bg=branco, justify=LEFT, font='Aria 10')
entry_produto.place(x=130, y=11)

## Label do Descrição do Produto
label_marca = Label(frame_form, text='Marca/Modelo',font='Ivy 11 bold', bg=branco_, fg=roxo_escuro)
label_marca.place(x=15, y=40)
## Entrada do Descrição do Produto
entry_marca = Entry(frame_form, width=30, relief=SOLID, bg=branco, justify=LEFT, font='Aria 10')
entry_marca.place(x=130, y=41)



## Label do Forma de pagamento 
label_F_pagamento = Label(frame_form, text='Forma de pagamento',font='Ivy 11 bold', bg=branco_, fg=roxo_escuro)
label_F_pagamento.place(x=15, y=80)
## Entrada do Forma de pagarmento 
entry_F_pagamento = ttk.Combobox(frame_form, values=formas_de_pagamento, font='Aria 10', width=20)
entry_F_pagamento.current(0)
entry_F_pagamento.place(x=180, y=81)

## Label do valor da venda  
label_valor = Label(frame_form, text='Valor R$',font='Ivy 11 bold', bg=branco_, fg=roxo_escuro)
label_valor.place(x=15, y=120)
## Entrada do Forma de  Data da venda
entry_valor = Entry(frame_form, width=30, relief=SOLID, bg=branco, justify=LEFT, font='Aria 10')
entry_valor.place(x=130, y=121)

'''#################################################################
########################    TODOS OS BOTÕES  #######################
#####################################################################'''

''' ####################### BOTÂO DE COONFIRMAR #################
'''
button_cofirmar = Button(frame_form, command=inserir, text='Vender'.upper(), font='Ivy 11 bold', width=23, height=1, bg=verde, fg=branco)
button_cofirmar.place(x=130, y=210)


'''######################## Botão de Atualizar dados #############'''

button_atualizar = Button(frame_form, command=atualizar ,text='Atualizar'.upper(), font='Ivy 11 bold', width=10,bg=azul_claro, fg=branco)
button_atualizar.place(x=780, y=210)


'''##########################   Botão de deletar #################'''

button_deletar = Button(frame_form, command=deletar, text='Deletar'.upper(), font='Ivy 11 bold', width=10, bg=vermelho, fg=branco)
button_deletar.place(x=900, y=210)

'''##########################  Botão Salvar no excel  ################'''
button_seve_excel = Button(frame_form, command=salvar_excel, text='Salvar no Excel'.upper(), font='Ivy 11 bold', width=20, bg='#EED67B', fg=roxo_escuro)
button_seve_excel.place(x=850, y=10)

###################### LABEL E CONTROLE DE VALOR #########################

label_total = Label(frame_form, text='',width=20, height=2 ,fg=branco,bg='#ECB55F', anchor=CENTER, font=('Ivy 17 bold'))
label_total.place(x= 450, y=40)

label_total_ = Label(frame_form, text='Valor Total das vendas',width=28 ,fg=branco,bg='#ECB55F', anchor=CENTER, font=('Ivy 12 bold'))
label_total_.place(x= 450, y=20)



label_qtd = Label(frame_form, text='',width=20, height=2 ,fg=branco,bg='#ECB55F', anchor=CENTER, font=('Ivy 17 bold'))
label_qtd.place(x= 450, y=160)

label_qtd_ = Label(frame_form, text='Quantidade de vendas',width=28 ,fg=branco,bg='#ECB55F', anchor=CENTER, font=('Ivy 12 bold'))
label_qtd_.place(x= 450, y=140)

'''######################   BOTÕES DE MENU    #######################'''

button_menu = Button(frame_form, command=abrir_conf, text='Configurações \n avançadas'.upper(), font='Ivy 11 bold', width=20, bg=branco_, fg=roxo_escuro)
button_menu.place(x=850, y=60)


'''##################################################################################
###############################  TABELAS DE DADOS  ##################################
#####################################################################################'''
def mostrar_tabela():
    
    global tree
    lista_vendas = ver_dados()
    titulo_tabela = ['#Vendas','Produto','Marca/Modelo','Data da venda', 'Hora da venda','Forma de Pagamento','Valor da Venda']

    style.configure("Treeview", background=branco)

    #FBFBF2
    tree = ttk.Treeview(frame_tabela,style="Treeview" ,columns=titulo_tabela, selectmode='extended', show='headings')
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_tabela.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center", "center", "center", "center"]
    h = [70, 180,150,180,180,150, 150]
    n = 0

    for coluna in titulo_tabela:
        tree.heading(coluna, text=coluna.title(), anchor=CENTER)
        tree.column(coluna, width=h[n], anchor=hd[n])
        n+=1

    for vendas in lista_vendas:
        tree.insert('', 'end', values=vendas)
        
        
    quantidade =[]

    for venda in lista_vendas:
        quantidade.append(venda[6])

    Total_valor = sum(quantidade)
    Total_vendas = len(quantidade)

    label_qtd['text'] = Total_vendas

    def ocultar_valor():
        label_total['text'] = 'R$ ***'
        button_mostrar = Button(frame_form, command=mostrar_valor, text='-'.upper(), font='Ivy 11 bold', width=4, bg='#ECB55F', fg=branco, border=0)
        button_mostrar.place(x=690, y=20)
        
    def mostrar_valor():
        label_total['text'] = 'R${:,.2f}'.format(Total_valor)
        
        button_ocultar = Button(frame_form, command=ocultar_valor, text='-'.upper(), font='Ivy 11 bold', width=4, bg='#ECB55F', fg=branco, border=0)
        button_ocultar.place(x=690, y=20)
    
    mostrar_valor()

mostrar_tabela()
janela.mainloop()