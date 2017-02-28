from tkinter import *
from Classes.DB.modulo_cursor import ModuloCursor
from Classes.Scripts.scriptSQL import RecuperaTLA
import sys

class Espacador:
    #cria um frame com os botões utilizados no CRUD
    def __init__(self, master):
        self.master = master

        self.frame = Frame(self.master)
        self.lbVazio = Label(self.frame, text=' ', height=2)
        self.lbVazio.grid(row=1, column=1, sticky=W)
        
        obj = RecuperaTLA()
        self.sql = obj.get_sql()

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame