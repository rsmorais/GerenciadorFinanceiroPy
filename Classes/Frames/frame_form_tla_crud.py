from tkinter import *
from Classes.DB.modulo_cursor import ModuloCursor
from Classes.Scripts.scriptSQL import RecuperaTLA
from Classes.DB.tbl_TLA import TBL_TLA_TipoLancamento as TLA
import sys

class FrameFormTlaCRUD:
    #cria um frame com os botões utilizados no CRUD
    def __init__(self, master):
        self.master = master

        self.frame = Frame(self.master)
        self.Titulo = Label(self.frame, text='---Formulario---')
        self.idTipo = None
        self.row_count = 0
        
        self.lbTipo = Label(self.frame, text='Tipo: ')
        self.lbDtAtualizacao = Label(self.frame, text=' ')
        self.lbDt = Label(self.frame, text='Data de Atualização: ')
        self.txtTipo = Entry(self.frame)
        
        self.Titulo.grid(row=0, column=0, columnspan=2, sticky=E+W)
        self.lbTipo.grid(row=1, column=0, sticky=E)
        self.txtTipo.grid(row=1, column=1, sticky=W)
        self.lbDt.grid(row=2, column=0, sticky=E)
        self.lbDtAtualizacao.grid(row=2, column=1, sticky=W)

        obj = RecuperaTLA()
        self.sql = obj.get_sql()
    
    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame

    def retrieve(self, arg):
        cursor = ModuloCursor()
        self.dataSQL = cursor.retrieve(self.sql, arg)
        self.post_retrieve()

    def post_retrieve(self):
        if len(self.dataSQL) > 0:
            print(self.dataSQL[0])
            self.idTipo = self.dataSQL[0][0]
            self.txtTipo.delete(0, 'end')
            self.txtTipo.insert(0, self.dataSQL[0][1])
            print(type(self.dataSQL[0][2]))
            self.lbDtAtualizacao.config(text=self.dataSQL[0][2])

    def new_row(self):
        self.idTipo = None
        self.txtTipo.delete(0, 'end')
        print(type(""))
        self.lbDtAtualizacao.config(text="")

    def pre_update(self):
        return True

    def get_args(self):
        dic = {}
        self.listArgs = []
        dic['TLA_dsTipoLancamento'] = self.txtTipo.get()
        dic['TLA_idTipoLancamento'] = self.idTipo
        self.listArgs.append(dic)

    def update(self):
        print('update')
        if self.pre_update():
            self.get_args()
            bd = TLA()
            if(self.idTipo == None):                
                bd.insert(self.listArgs)
            else:
                bd.edit(self.listArgs)