from tkinter import *
from Classes.Frames.frame_btn_crud import FrameBtnCRUD as Btn
from Classes.Frames.frame_key_tla_crud import FrameKeyTlaCRUD as Key
from Classes.Frames.frame_form_tla_crud import FrameFormTlaCRUD as Form
from Classes.Frames.frame_espacador import Espacador

class WinCadastroTLA:
    def __init__(self, master):
        self.master = master
        
    def load_jan(self):
        self.win=Frame(self.master)
        self.Titulo = Label(self.win, text='CADASTRO DE TIPOS DE LANÇAMENTO')

        #instanciando objetos
        self.btnsCRUD = Btn(self.win)
        self.key = Key(self.win)
        self.form = Form(self.win)
        self.espacador = Espacador(self.win)

        #tornando os objetos visíveis
        self.Titulo.grid(row=0, column=0)     
        self.key.get_frame().grid(row=1, column=0)
        self.form.get_frame().grid(row=3, column=0, sticky=W)
        self.espacador.get_frame().grid(row=2, column=0, sticky=W)
        self.btnsCRUD.get_frame().grid(row=4, column=0, sticky=E)
        self.win.grid(row=0, column=0)

        #setando o evento do botão retrieve
        self.key.set_command("btnRecuperar", self.retrieve)
        self.key.set_command("btnNovo", self.new_row)
        self.btnsCRUD.set_command("btnSalvar", self.form.update)

        self.pos_load()

    def new_row(self):
        self.form.new_row()


    def retrieve(self):        
        self.form.retrieve((self.key.get_item("txtTipo"),))
        
    def pos_load(self):
        pass
        
    def pre_close(self):
        return True
        
    def close_window(self):
        if self.pre_close():
            self.win.destroy()

			
