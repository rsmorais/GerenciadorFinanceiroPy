from tkinter import *

class PopupMulti:
    def __init__(self, master, args):
        self.master = master
        self.args = args
        self.win=Toplevel()

    def load_jan(self, args):        
        linhas = []
        i = 0
        self.Titulo = Label(self.win, text=args[1]).grid(row=0, column=0)
        self.opc = Label(self.win, text=' ')

        for linha in self.args:
            frame = Frame(self.win)
            l1=Label(frame, text= str(linha[args[2]]))
            lbtnSair=Button(frame, text='x', command = lambda j=i: args[0](j))
            l1.grid(row=0, column=1, sticky=W)
            lbtnSair.grid(row=0, column=0, sticky=W)
            linhas.append(frame)
            i += 1

        i = 1
        for linha in linhas:
            linha.grid(row=i, column=0, sticky=W)
            i += 1

        self.opc.grid(row=i, column=0, sticky=W)
        
        self.win.geometry('200x200')
        self.win.transient(self.master)
        self.win.focus_force()
        self.win.grab_set()
        
    def get_frame(self):
        return self.win

    def close_window(self):
        self.win.destroy()