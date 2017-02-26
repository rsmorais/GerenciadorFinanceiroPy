from tkinter import *
from Classes.DB.modulo_cursor import ModuloCursor
from Classes.Scripts.scriptSQL import RecuperaTLA
import sys

class FrameFormTlaCRUD:
    #cria um frame com os botões utilizados no CRUD
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.lbTipo = Label(self.frame, text='Tipo: ')
        self.lbDtAtualizacao = Label(self.frame, text=' ')
        self.lbDt = Label(self.frame, text='Data de Atualização: ')
        self.txtTipo = Entry(self.frame)
        
        self.lbTipo.grid(row=0, column=0, sticky=W)
        self.txtTipo.grid(row=0, column=1, sticky=W)
        self.lbDt.grid(row=1, column=0, sticky=W)
        self.lbDtAtualizacao.grid(row=1, column=1, sticky=W)
        
        obj = RecuperaTLA()
        self.sql = obj.get_sql()

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame

    def retrieve(self):
        cursor = ModuloCursor()
        print(self.sql)
        self.dataSQL = cursor.retrieve(self.sql, None)
        self.post_retrieve()

    def post_retrieve(self):
        print(self.dataSQL[0][0])
        self.txtTipo.insert(0, self.dataSQL[0][1])
        self.lbDtAtualizacao.config(text=self.dataSQL[0][3])

