from tkinter import *

class FrameBtnKey:
    #cria um frame com os botões utilizados no CRUD 
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.btnRecuperar = Button(self.frame, text="Recuperar")
        self.btnNovo = Button(self.frame, text="Novo")

        self.btnRecuperar.grid(row=0, column=0)
        self.btnNovo.grid(row=0, column=1)

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame
    
    def set_command(self, argBtn, argCommand):
        if argBtn == "btnRecuperar":
            self.btnRecuperar.config(command=argCommand) 
        if argBtn == "btnNovo":
            self.btnNovo.config(command=argCommand)

    def sair(self):
        self.master.destroy()
