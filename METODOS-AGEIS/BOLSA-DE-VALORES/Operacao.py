from tkinter import *
from tkinter import ttk
import sqlite3 # instalar o banco de dados no python usando pip

janela = Tk()

class funcoes:
    def id_op(self):
        self.entrada_id_operacao += 1
        return self.entrada_id_operacao

    def calculo_operacao(self):
        if self.entrada_tipo_operacao.get() == 'Compra':
            pass
        else:
            pass
        return self.valor_operacao

    def limpar_tela(self):
        self.entrada_codigo_ativo.delete(0, END)
        self.entrada_qtd_acoes.delete(0, END)
        self.entrada_valor_unitario.delete(0, END)
        self.entrada_dia.delete(0, END)
        self.entrada_mes.delete(0, END)
        self.entrada_ano.delete(0, END)
        self.entrada_tipo_operacao.delete(0, END)
    
    def conecta_banco(self):
        self.conector = sqlite3.conect('bolsa_de_valores.bd')
        self.cursor = self.conector.cursor()
        print('Conectando-se ao banco de dados...')
    
    def desconecta_banco(self):
        self.conector.close()
        print('Banco de dados desconectado...')
    
    def criar_tabela(self):
        self.conecta_banco()
        
        # criação da tabela operações
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS operacoes (
            id_operacao INTEGER PRIMARY KEY,
            codigo_operacao VARCHAR(10) NOT NULL,
            data DATE NOT NULL,
            qtd_acoes INTEGER NOT NULL,
            valor_unitario FLOAT NOT NULL,
            tipo_operacao CHAR(6) NOT NULL,
            taxa_corretagem FLOAT NOT NULL,
            taxa_b3 FLOAT NOT NULL,
            valor_operacao FLOAT NOT NULL
        );''')
        self.conector.commit()
        print('Banco de dados criado com sucesso!')
        self.desconecta_banco()
    
    def variaveis(self):
		self.id_oper = self.entrada_id_operacao.get()
        self.cod_ativo = self.entrada_codigo_ativo.get()
        self.data = f'{self.entrada_ano.get()}-{self.entrada_mes.get()}-{self.entrada_dia.get()}'
        # self.dia = self.entrada_dia.get()
        # self.mes = self.entrada_mes.get()
        # self.ano = self.entrada_ano.get()
        self.qtd = self.entrada_qtd_acoes.get()
        self.valor_unt = self.entrada_valor_unitario.get()
        self.tipo_op = self.entrada_tipo_operacao.get()
        # self.taxa_corr = self.entrada_taxa_corretagem.get()
        # self.tx_b3 = self.entrada_taxa_b3.get()
        self.valor_op = self.calculo_operacao()
	
	def adicionar_operacao(self):
        self.variaveis()        
        self.conectar_banco()
        
        self.cursor.execute('''INSERT INTO operacoes(codigo_operacao, data, qtd_acoes, valor_unitario, tipo_operacao, taxa_corretagem, taxa_b3, valor_operacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.cod_ativo, self.data, self.qtd, self.valor_unt, self.tipo_op, self.taxa_corr, self.tx_b3, self.valor_op))
        self.conector.commit()
        self.desconecta_banco()
        self.select_lista()
        self.limpar_tela()
    
    def select_lista(self):
        self.lista_operacoes.delete(* self.lista_operacoes.get_children())
        self.conectar_banco()
        lista = self.cursor.execute('''SELECT id_operacao, codigo_operacao, data, qtd_acoes, valor_unitario, tipo_operacao, taxa_corretagem, taxa_b3, valor_operacao FROM operacoes
            ORDER BY id_operacao ASC
        ''')
        for elemento in lista:
            self.lista_operacoes.insert('', END, values=elemento)
        self.desconectar_banco()
	
	def duplo_clique(self, event):
		self.limpar_tela()
		self.lista_operacoes.selection()
		
		for item in self.lista_operacoes.selection():
			col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.lista_operacoes.item(n, 'values')
			self.entrada_id_operacao.insert(END, col1)
			self.entrada_codigo_ativo.insert(END, col2)
			self.entrada_data.insert(END, col3)
			self.entrada_qtd_acoes.insert(END, col4)
			self.entrada_valor_unitario.insert(END, col5)
			self.entrada_tipo_operacao.insert(END, col6)
			self.entrada_taxa_corretagem.insert(END, col7)
			self.entrada_taxa_b3.insert(END, col8)
			self.calculo_operacao.insert(END, col9)
	
	def apagar_operacao(self):
		self.variaveis()
		self.conectar_banco()
		self.conector.execute('''DELETE FROM operacoes WHERE id_operacao = ?''', (self.id_oper))
		self.conector.commit()
		self.desconectar_banco()
		self.limpar_tela()
		self.select_lista()

class aplicativo(funcoes):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_de_tela()
        self.widgets_frame_1()
        self.widgets_frame_2()
        self.criar_tabela()
        self.select_lista()
        janela.mainloop()

    def tela(self):
        self.janela.title('Cadastro de Operações')  # título da janela: aparece logo na barra de título
        self.janela.configure(background='#1e3743')  # cor de fundo da janela
        self.janela.geometry('700x500')  # tamanho inicial da janela altura = 700 x largura = 500
        self.janela.resizable(True, True)  # responsividade da tela, True True quer dizer que a tela vai ser responsiva na altura e na largura
        self.janela.maxsize(width=900, height=700)  # cria um limite máximo de tamanho que a janela pode ter, nesse caso 900x700
        self.janela.minsize(width=400, height=300)  # cria um limite mínimo de tamanho que a janela pode ter, nesse caso 400x300

    def frames_de_tela(self):
        # criação dos frames dentro da janela
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        # BOTÕES =================================================================================
        # criação do botão limpar
        self.btn_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpar_tela)
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão buscar
        self.btn_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.btn_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão novo
        self.btn_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.adicionar_operacao)
        self.btn_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão alterar
        self.btn_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.btn_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão apagar
        self.btn_apagar = Button(self.frame_1, text='Apagar',bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.apagar_operacao)
        self.btn_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # LABELS =================================================================================

        # criação do label ID operação
        self.label_id_operacao = Label(self.frame_1, text='ID Operação', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_id_operacao.place(relx=0.05, rely=0.05)

        self.entrada_id_operacao = Entry(self.frame_1, values=self.id_op())
        self.entrada_id_operacao.place(relx=0.05, rely=0.15, relwidth=0.13)
        
        # criação do label código ativo
        self.label_codigo_ativo = Label(self.frame_1, text='Código Ativo', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_codigo_ativo.place(relx=0.05, rely=0.05)

        self.entrada_codigo_ativo = Entry(self.frame_1)
        self.entrada_codigo_ativo.place(relx=0.05, rely=0.15, relwidth=0.13)

        # criação do label quantidade de ações
        self.label_qtd_acoes = Label(self.frame_1, text='Quantidade de Ações', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_qtd_acoes.place(relx=0.05, rely=0.35)

        self.entrada_qtd_acoes = Entry(self.frame_1)
        self.entrada_qtd_acoes.place(relx=0.05, rely=0.45, relwidth=0.4)

        # criação do label valor unitário
        self.label_valor_unitario = Label(self.frame_1, text='Valor Unitário', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_valor_unitario.place(relx=0.5, rely=0.35)

        self.entrada_valor_unitario = Entry(self.frame_1)
        self.entrada_valor_unitario.place(relx=0.5, rely=0.45, relwidth=0.4)

        # criação do label dia
        self.label_dia = Label(self.frame_1, text='Dia', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_dia.place(relx=0.05, rely=0.6)
        
        lista_dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        self.entrada_dia = ttk.Combobox(self.frame_1, values=lista_dias)
        self.entrada_dia.set(1)
        self.entrada_dia.place(relx=0.05, rely=0.7, relwidth=0.08)

        # criação do label mes
        self.label_mes = Label(self.frame_1, text='Mes', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_mes.place(relx=0.15, rely=0.6)

        self.entrada_mes = Entry(self.frame_1)
        self.entrada_mes.place(relx=0.15, rely=0.7, relwidth=0.08)

        # criação do label ano
        self.label_ano = Label(self.frame_1, text='Ano', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_ano.place(relx=0.25, rely=0.6)

        self.entrada_ano = Entry(self.frame_1)
        self.entrada_ano.place(relx=0.25, rely=0.7, relwidth=0.2)

        # criação do label tipo de operação
        self.label_tipo_operacao = Label(self.frame_1, text='Tipo de Operação', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_tipo_operacao.place(relx=0.5, rely=0.6)

        '''self.entrada_tipo_operacao = Entry(self.frame_1)
        self.entrada_tipo_operacao.place(relx=0.5, rely=0.7, relwidth=0.4)'''

        lista_operacoes = ['Compra', 'Venda']
        self.entrada_tipo_operacao = ttk.Combobox(self.frame_1, values=lista_operacoes)
        self.entrada_tipo_operacao.set('Compra')
        self.entrada_tipo_operacao.place(relx=0.5, rely=0.7, relwidth=0.4)
        
        # criação do label taxa corretagem
        self.label_taxa_corretagem = Label(self.frame_1, text='Tx Corretagem', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_taxa_corretagem.place(relx=0.25, rely=0.6)

        self.entrada_taxa_corretagem = Entry(self.frame_1)
        self.entrada_taxa_corretagem.place(relx=0.25, rely=0.7, relwidth=0.2)
        
        # criação do label taxa B3
        self.label_taxa_b3 = Label(self.frame_1, text='Tx B3', bg='#dfe3ee', fg='#1e3743', font('verdana', 8, 'bold'))
        self.label_taxa_b3.place(relx=0.25, rely=0.6)

        self.entrada_taxa_b3 = Entry(self.frame_1)
        self.entrada_taxa_b3.place(relx=0.25, rely=0.7, relwidth=0.2)
        
    def widgets_frame_2(self):
        # LISTAGEM COM A EXIBIÇÃO DOS DADOS
        self.lista_operacoes =  ttk.Treeview(self.frame_2, height=3, column('coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5', 'coluna6', 'coluna7', 'coluna8', 'coluna9'))
        self.lista_operacoes.heading('#0', text='')
        self.lista_operacoes.heading('#1', text='Id Op.')
        self.lista_operacoes.heading('#2', text='Cód.')
        self.lista_operacoes.heading('#3', text='Data')
        self.lista_operacoes.heading('#4', text='Qtd')
        self.lista_operacoes.heading('#5', text='Valor Unt.')
        self.lista_operacoes.heading('#6', text='Tipo Op.')
        self.lista_operacoes.heading('#7', text='Tax. Corret.')
        self.lista_operacoes.heading('#8', text='Taxa B3')
        self.lista_operacoes.heading('#9', text='Valor Op.')
        
        # a soma dos widths da lista com exceção do item 0, tem que dar 500
        self.lista_operacoes.column('#0', width=1)
        self.lista_operacoes.column('#1', width=25)
        self.lista_operacoes.column('#2', width=25)
        self.lista_operacoes.column('#3', width=100)
        self.lista_operacoes.column('#4', width=25)
        self.lista_operacoes.column('#5', width=50)
        self.lista_operacoes.column('#6', width=100)
        self.lista_operacoes.column('#7', width=25)
        self.lista_operacoes.column('#8', width=50)
        self.lista_operacoes.column('#9', width=100)
        
        self.lista_operacoes.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        # criação da barra de rolagem
        self.barra_rolagem = Scrollbar(self.frame_2, orient='vertical')
        self.lista_operacoes.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
		
		self.lista_operacoes.bind('<Double1>', self.duplo_clique)
        
aplicativo()
