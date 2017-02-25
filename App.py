#python 3.4
#coding: utf8

from tkinter import *
from tkinter.ttk import *
import zlib,base64
import appMenu
import os

def callback():
	lista = [(dsTipoLancamento.get(), 'rafael', '2017-02-23')]
	print(lista)
	tblTLA = b.TBL_TLA_TipoLancamento()	
	tblTLA.inserir(lista)

janela = Tk()
janela.title("Contabilidade")
janela.geometry("600x600")

icon = PhotoImage(file='Img/py.png')
janela.tk.call('wm', 'iconphoto', janela._w, icon)

obj= appMenu.Main_menu(janela)
mainMenu = obj.getMenu()
janela.config(menu=mainMenu)


janela.mainloop()
