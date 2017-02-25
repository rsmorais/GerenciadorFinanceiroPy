from tkinter import *
from Classes.Windows.win_sobre import WinSobre
from Classes.Windows.Cadastro.win_indisponivel import *
class Main_menu:
	
    def __init__(self, argWindow):
        self.myWindow = argWindow
        
    def arquivo_alterar_BD(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def arquivo_desconectar(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def arquivo_quit(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def cadastro_lancamento(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def cadastro_forma_pagamento(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def cadastro_tipo_pagamento(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def cadastro_cartao(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def relatorio_lancamentos(self):
        obj = WinIndisponivel(self.myWindow)
        obj.load_jan()
        
    def sobre(self):
        obj = WinSobre(self.myWindow)
        obj.load_jan()
                    
    def getMenu(self):
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
        menuCadastro.add_command(label='Forma de Pag...', command = self.cadastro_forma_pagamento)
        menuCadastro.add_command(label='Tipo de pag...', command = self.cadastro_tipo_pagamento)
        menuCadastro.add_command(label='Cartão', command = self.cadastro_cartao)
        
        #submenu de RELATORIO
        menuRelatorio.add_command(label='Lançamentos...', command = self.relatorio_lancamentos)
        
        return menubar
        
		
		
		
		
		
		
		
		
		
		
		
		
		
		
