from tkinter import *
from Classes.DB.modulo_cursor import ModuloCursor
from Classes.Scripts.scriptSQL import RecuperaTLA
from Classes.DB.tbl_TLA import TBL_TLA_TipoLancamento as TLA
from Classes.Util.popup_multi import PopupMulti
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
        
        self.Titulo.grid(row=0, column=0, columnspan=4, sticky=E+W)
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
        self.pos_retrieve()

    def pos_retrieve(self):
        if len(self.dataSQL) > 0:
            if len(self.dataSQL) > 1:
                args = []
                args.append(self.return_popup)
                args.append('---Selecione o Tipo de Lançamento---')
                args.append(1)
                self.popup = PopupMulti(self.master, self.dataSQL)
                self.popup.load_jan(args)

            else:
                self.idTipo = self.dataSQL[0][0]
                self.txtTipo.delete(0, 'end')
                self.txtTipo.insert(0, self.dataSQL[0][1])
                self.lbDtAtualizacao.config(text=self.dataSQL[0][2])

        else:
            self.new_row()

    def new_row(self):
        self.idTipo = None
        self.txtTipo.delete(0, 'end')
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
        if self.pre_update():
            self.get_args()
            bd = TLA()
            if(self.idTipo == None):                
                bd.insert(self.listArgs)
            else:
                bd.edit(self.listArgs)

    def pos_delete(self):
        self.new_row()

    def pre_delete(self):
        return True

    def delete(self):
        if self.pre_delete():
            self.get_args()
            bd = TLA()
            if(self.idTipo == None):                
                #exibir msm de erro
                pass
            else:
                bd.delete(self.listArgs)

            self.pos_delete();
    
    def return_popup(self, number):
        self.idTipo = self.dataSQL[number][0]
        self.txtTipo.delete(0, 'end')
        self.txtTipo.insert(0, self.dataSQL[number][1])
        self.lbDtAtualizacao.config(text=self.dataSQL[number][2])
        self.popup.close_window()