from tkinter import *
from Classes.Frames.frame_btn_crud import FrameBtnCRUD as Btn
from Classes.Frames.frame_key_tla_crud import FrameKeyTlaCRUD as Key
from Classes.Frames.frame_form_tla_crud import FrameFormTlaCRUD as Form

class WinCadastroTLA:
    def __init__(self, master):
        self.master = master
        
    def load_jan(self):
        self.win=Frame(self.master)
        #instanciando objetos
        self.btnsCRUD = Btn(self.win)
        self.key = Key(self.win)
        self.form = Form(self.win)

        #pegando os widget
        
        #tornando os objetos visíveis
       
        self.key.get_frame().grid(row=0, column=0, sticky=W)
        self.form.get_frame().grid(row=1, column=0, sticky=W)
        self.btnsCRUD.get_frame().grid(row=2, column=0, sticky=E)
        self.win.grid(row=0, column=0)

        self.key.set_command("btnRecuperar", self.retrieve)

        self.pos_load()

    def retrieve(self):
        #self.key.txtTipo.get()
        self.form.retrieve()
        
    def pos_load(self):
        pass
        
    def pre_close(self):
        return True
        
    def close_window(self):
        if self.pre_close():
            self.win.destroy()

			
