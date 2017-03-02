from tkinter import *
from Classes.Frames.frame_btn_crud import FrameBtnCRUD as Btn
from Classes.Frames.frame_key_crt_crud import FrameKeyCrtCRUD as Key
from Classes.Frames.frame_form_crt_crud import FrameFormCrtCRUD as Form
from Classes.Frames.frame_espacador import Espacador

class WinCadastroCRT:
    def __init__(self, master):
        self.master = master
        self.win=Frame(self.master)
        
    def load_jan(self):        
        self.Titulo = Label(self.win, text='CADASTRO DE CARTÕES')

        #instanciando objetos
        self.btnsCRUD = Btn(self.win)
        self.key = Key(self.win)
        self.form = Form(self.win)
        self.espacador = Espacador(self.win)

        #tornando os objetos visíveis
        self.Titulo.grid(row=0, column=0)     
        self.key.get_frame().grid(row=1, column=0)
        self.espacador.get_frame().grid(row=2, column=0, sticky=W)
        self.form.get_frame().grid(row=3, column=0, sticky=W)
        self.btnsCRUD.get_frame().grid(row=4, column=0, sticky=E)
        self.win.grid(row=0, column=0)

        #setando o evento do botão retrieve
        self.key.set_command("btnRecuperar", self.retrieve)
        self.key.set_command("btnNovo", self.new_row)
        self.btnsCRUD.set_command("btnSalvar", self.form.update)
        self.btnsCRUD.set_command("btnDeletar", self.form.delete)

        self.pos_load()

    def get_frame(self):
        return self.win

    def new_row(self):
        self.form.new_row()


    def retrieve(self):
        arg = self.key.get_item("txtTipo") + '%'
        self.form.retrieve((arg,))
        
    def pos_load(self):
        pass
        
    def pre_close(self):
        return True
        
    def close_window(self):
        if self.pre_close():
            self.win.destroy()

			
