from tkinter import *

janela = Tk()

class aplicativo:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_de_tela()
        self.widgets_frame_1()
        janela.mainloop()
    
    def tela(self):
        self.janela.title('Cadastro de Operações') # título da janela: aparece logo na barra de título
        self.janela.configure(background = '#1e3743') # cor de fundo da janela
        self.janela.geometry('700x500') # tamanho inicial da janela altura = 700 x largura = 500
        self.janela.resizable(True, True) # responsividade da tela, True True quer dizer que a tela vai ser responsiva na altura e na largura
        self.janela.maxsize(width = 900, height = 700) # cria um limite máximo de tamanho que a janela pode ter, nesse caso 900x700
        self.janela.minsize(width = 400, height = 300) # cria um limite mínimo de tamanho que a janela pode ter, nesse caso 400x300
        
    def frames_de_tela(self):
        # criação dos frames dentro da janela
        self.frame_1 = Frame(self.janela, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', hightlightthickness = 3)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.96)
        
        self.frame_2 = Frame(self.janela, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', hightlightthickness = 3)
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.96)
    
    def widgets_frame_1(self):
        # criação do botão limpar
        self.btn_limpar = Button(self.frame_1, text = 'Limpar')
        self.btn_limpar.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # criação do botão buscar
        self.btn_buscar = Button(self.frame_1, text = 'Buscar')
        self.btn_buscar.place(relx = 0.3, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # criação do botão novo
        self.btn_novo = Button(self.frame_1, text = 'Novo')
        self.btn_novo.place(relx = 0.6, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # criação do botão alterar
        self.btn_alterar = Button(self.frame_1, text = 'Alterar')
        self.btn_alterar.place(relx = 0.7, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # criação do botão apagar
        self.btn_apagar = Button(self.frame_1, text = 'Apagar')
        self.btn_apagar.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        
        # criação do label código
        self.label_codigo = Label(self.frame_1, text = 'Código')
        self.label_codigo.place(relx = '', rely = '', relwidth = '', relheight = '')

aplicativo()
