from tkinter import *

class FrameBtnCRUD:
    #cria um frame com os botões utilizados no CRUD 
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.btnSalvar = Button(self.frame, text="Salvar")
        self.btnDeletar = Button(self.frame, text="Deletar")
        self.btnSair = Button(self.frame, text="Sair", command=self.sair)
        
        self.show_salvar()
        self.show_deletar()
        self.show_sair()

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

    def show_salvar(self):
        self.btnSalvar.grid(row=0, column=0)
        
    def show_deletar(self):
        self.btnDeletar.grid(row=0, column=1)

    def show_sair(self):
        self.btnSair.grid(row=0, column=2)

    def hide_salvar(self):
        self.btnSalvar.grid_forget()

    def hide_deletar(self):
        self.btnDeletar.grid_forget()

    def hide_sair(self):
        self.btnSair.grid_forget()

