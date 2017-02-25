from tkinter import *

class WinSobre:
    def __init__(self, master):
        self.master = master
        
    def load_jan(self):
        self.win=Toplevel()
        self.l1=Label(self.win, text='Aplicação de gerenciamento financeiro!')
        self.l2=Label(self.win, text='Utilizada para estudos.')
        self.l3=Label(self.win, text='Fevereiro de 2017.')
        btnSair=Button(self.win, text='Fechar', command = self.close_window)
        
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()  
        btnSair.pack()
        
        self.win.geometry('300x200')
        self.win.transient(self.master)
        self.win.focus_force()
        self.win.grab_set()
        
    def close_window(self):
        self.win.destroy()

			
