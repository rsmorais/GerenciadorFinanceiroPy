from tkinter import *
from Classes.Windows.win_sobre import WinSobre
from Classes.Windows.Cadastro.win_indisponivel import *
from Classes.Windows.Cadastro.win_cadastro_TLA import *
from Classes.Windows.Cadastro.win_cadastro_CRT import *
class Main_menu:
	
    def __init__(self, argWindow):
        self.myWindow = argWindow
        self.frameFilho = None
        
    def arquivo_alterar_BD(self):
        self.close_window()
        obj = WinIndisponivel(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def arquivo_desconectar(self):
        self.close_window()
        obj = WinIndisponivel(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def arquivo_quit(self):
        self.close_window()
        obj = WinIndisponivel(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def cadastro_lancamento(self):
        self.close_window()
        obj = WinIndisponivel(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def cadastro_forma_pagamento(self):
        self.close_window()
        obj = WinIndisponivel(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def cadastro_tipo_lancamento(self):
        self.close_window()
        obj = WinCadastroTLA(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def cadastro_cartao(self):
        self.close_window()
        obj = WinCadastroCRT(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def relatorio_lancamentos(self):
        self.close_window()
        obj = WinIndisponivel(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
        
    def sobre(self):
        self.close_window()
        obj = WinSobre(self.myWindow)
        self.frameFilho = obj.get_frame()
        obj.load_jan()
                    
    def get_menu(self):
        #adicionando a barra de menu à janela
        menubar = Menu(self.myWindow)
        
        #criado as pastas à barra de menu
        menuArquivo = Menu(menubar)		#Arquivos
        menuCadastro = Menu(menubar)	#Cadastros
        menuRelatorio = Menu(menubar)	#Relatórios
        menuSobre = Menu(menubar)		#Sobre
        
        menubar.add_cascade(label='Arquivo', menu = menuArquivo)
        menubar.add_cascade(label='Cadastro', menu = menuCadastro)
        menubar.add_cascade(label='Relatório', menu = menuRelatorio)
        menubar.add_command(label='Sobre', command = self.sobre)
        
        #Submenu de ARQUIVO
        menuArquivo.add_command(label='Alterar BD', command = self.arquivo_alterar_BD)
        menuArquivo.add_command(label='Desconectar', command = self.arquivo_desconectar)
        menuArquivo.add_separator()
        menuArquivo.add_command(label='Sair', command = self.arquivo_quit)
        
        #submenu de CADASTRO
        menuCadastro.add_command(label='Lançamento', command = self.cadastro_lancamento)
        menuCadastro.add_command(label='Forma de Pagamento', command = self.cadastro_forma_pagamento)
        menuCadastro.add_command(label='Tipo de lançamento', command = self.cadastro_tipo_lancamento)
        menuCadastro.add_command(label='Cartão', command = self.cadastro_cartao)
        
        #submenu de RELATORIO
        menuRelatorio.add_command(label='Lançamentos...', command = self.relatorio_lancamentos)
        
        return menubar
    
    def close_window(self):
        if self.frameFilho != None:
           self.frameFilho.destroy()   
		
		
		
		
		
		
		
		
		
		
		
		
		
		
