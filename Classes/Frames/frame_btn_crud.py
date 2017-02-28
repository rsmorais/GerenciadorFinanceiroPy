from tkinter import *

class FrameBtnCRUD:
    #cria um frame com os botões utilizados no CRUD 
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.btnSalvar = Button(self.frame, text="Salvar")
        self.btnDeletar = Button(self.frame, text="Deletar")
        self.btnSair = Button(self.frame, text="Sair", command=self.sair)
        
        self.btnSalvar.grid(row=0, column=0)
        self.btnDeletar.grid(row=0, column=1)
        self.btnSair.grid(row=0, column=2)

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame
    
    def set_command(self, argBtn, argCommand):
        if argBtn == "btnSalvar":
            self.btnSalvar.config(command=argCommand) 
        elif argBtn == "btnDeletar":
            self.btnDeletar.config(command=argCommand) 
        elif argBtn == "btnSair":
            self.btnSair.config(command=argCommand)

    def sair(self):
        self.master.destroy()
