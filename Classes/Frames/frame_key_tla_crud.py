from tkinter import *
from Classes.Frames.frame_btn_key import FrameBtnKey as Btn

class FrameKeyTlaCRUD:
    #cria um frame com os botões utilizados no CRUD
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Titulo = Label(self.frame, text='---Chaves de Busca---')
        self.lbTipo = Label(self.frame, text='Tipo: ')
        self.txtTipo = Entry(self.frame)
        self.btnKey= Btn(self.frame)

        self.Titulo.grid(row=0, column=0, columnspan=4, sticky=E+W)
        self.lbTipo.grid(row=1, column=0)
        self.txtTipo.grid(row=1, column=1)
        self.btnKey.get_frame().grid(row=1, column=2)

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame
    
    def set_command(self, argBtn, argCommand):
        self.btnKey.set_command(argBtn, argCommand) 


    def get_item(self, argItem):
        if argItem == "txtTipo":
            return self.txtTipo.get()