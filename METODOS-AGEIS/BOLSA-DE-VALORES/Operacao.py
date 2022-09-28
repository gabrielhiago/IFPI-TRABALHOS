from tkinter import *
from tkinter import ttk

janela = Tk()

class aplicativo:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_de_tela()
        self.widgets_frame_1()
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
        self.btn_limpar = Button(self.frame_1, text='Limpar')
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão buscar
        self.btn_buscar = Button(self.frame_1, text='Buscar')
        self.btn_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão novo
        self.btn_novo = Button(self.frame_1, text='Novo')
        self.btn_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão alterar
        self.btn_alterar = Button(self.frame_1, text='Alterar')
        self.btn_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão apagar
        self.btn_apagar = Button(self.frame_1, text='Apagar')
        self.btn_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # LABELS =================================================================================

        # criação do label código ativo
        self.label_codigo_ativo = Label(self.frame_1, text='Código Ativo')
        self.label_codigo_ativo.place(relx=0.05, rely=0.05)

        self.entrada_codigo_ativo = Entry(self.frame_1)
        self.entrada_codigo_ativo.place(relx=0.05, rely=0.15, relwidth=0.13)

        # criação do label quantidade de ações
        self.label_qtd_acoes = Label(self.frame_1, text='Quantidade de Ações')
        self.label_qtd_acoes.place(relx=0.05, rely=0.35)

        self.entrada_qtd_acoes = Entry(self.frame_1)
        self.entrada_qtd_acoes.place(relx=0.05, rely=0.45, relwidth=0.4)

        # criação do label valor unitário
        self.label_valor_unitario = Label(self.frame_1, text='Valor Unitário')
        self.label_valor_unitario.place(relx=0.5, rely=0.35)

        self.entrada_valor_unitario = Entry(self.frame_1)
        self.entrada_valor_unitario.place(relx=0.5, rely=0.45, relwidth=0.4)

        # criação do label dia
        lista_dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        self.label_dia = Label(self.frame_1, text='Dia')
        self.label_dia.place(relx=0.05, rely=0.6)

        self.entrada_dia = ttk.Combobox(self.frame_1, values=lista_dias)
        self.entrada_dia.set()
        self.entrada_dia.place(relx=0.05, rely=0.7, relwidth=0.08)

        # criação do label mes
        self.label_telefone = Label(self.frame_1, text='Mes')
        self.label_telefone.place(relx=0.15, rely=0.6)

        self.entrada_telefone = Entry(self.frame_1)
        self.entrada_telefone.place(relx=0.15, rely=0.7, relwidth=0.08)

        # criação do label ano
        self.label_telefone = Label(self.frame_1, text='Ano')
        self.label_telefone.place(relx=0.25, rely=0.6)

        self.entrada_telefone = Entry(self.frame_1)
        self.entrada_telefone.place(relx=0.25, rely=0.7, relwidth=0.2)

        # criação do label tipo de operação
        self.label_tipo_operacao = Label(self.frame_1, text='Tipo de Operação')
        self.label_tipo_operacao.place(relx=0.5, rely=0.6)

        '''self.entrada_tipo_operacao = Entry(self.frame_1)
        self.entrada_tipo_operacao.place(relx=0.5, rely=0.7, relwidth=0.4)'''

        lista_operacoes = ['Compra', 'Venda']
        self.entrada_tipo_operacao = ttk.Combobox(self.frame_1, values=lista_operacoes)
        self.entrada_tipo_operacao.set('Compra')
        self.entrada_tipo_operacao.place(relx=0.5, rely=0.7, relwidth=0.4)


aplicativo()
