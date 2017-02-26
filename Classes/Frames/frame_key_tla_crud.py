from tkinter import *

class FrameKeyTlaCRUD:
    #cria um frame com os botões utilizados no CRUD
    lbTipo = None
    txtTipo = None
    btnRecuperar = None
    btnNovo = None

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        lbTipo = Label(self.frame, text='Tipo: ')
        txtTipo = Entry(self.frame)
        self.btnRecuperar = Button(self.frame, text="Recuperar")
        btnNovo = Button(self.frame, text="Novo")
        
        lbTipo.grid(row=0, column=0)
        txtTipo.grid(row=0, column=1)
        self.btnRecuperar.grid(row=0, column=2)
        btnNovo.grid(row=0, column=3)

    #retorna o frame, para caso a pessoa queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame
    
    def set_command(self, argBtn, argCommand):
        if argBtn == "btnRecuperar":
            self.btnRecuperar.config(command=argCommand) 
        if argBtn == "btnNovo":
            btnNovo.bind("<Button-1>", argCommand) 