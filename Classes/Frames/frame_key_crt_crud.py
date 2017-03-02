from tkinter import *
from Classes.Frames.frame_btn_key import FrameBtnKey as Btn

class FrameKeyCrtCRUD:
    #cria um frame com os botões utilizados no CRUD
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Titulo = Label(self.frame, text='---Chaves de Busca---')
        self.lbNmCartao = Label(self.frame, text='Nome Cartão: ')
        self.txtNmCartao = Entry(self.frame)
        self.btnKey= Btn(self.frame)

        self.Titulo.grid(row=0, column=0, columnspan=4, sticky=E+W)
        self.lbNmCartao.grid(row=1, column=0)
        self.txtNmCartao.grid(row=1, column=1)
        self.btnKey.get_frame().grid(row=1, column=2, rowspan=4)

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame
    
    def set_command(self, argBtn, argCommand):
        self.btnKey.set_command(argBtn, argCommand) 


    def get_item(self, argItem):
        if argItem == "txtTipo":
            return self.txtNmCartao.get()