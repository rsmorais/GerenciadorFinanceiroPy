from tkinter import *

class FrameCRUD:
    def __init__(self, master):
        self.master = master
        
    def getFrame(self):
        self.frame = Frame(self.master)
        self.btnSalvar = Button(self.frame, text="Salvar")
        self.btnDeletar = Button(self.frame, text="Deletar")
        
        self.btnSalvar.grid(row=0, column=0)
        self.btnDeletar.grid(row=0, column=1)
        return self.frame
        print('frame') 

			
