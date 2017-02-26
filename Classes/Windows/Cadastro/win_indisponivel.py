from tkinter import *
from Classes.Frames.frame_btn_crud import FrameBtnCRUD

class WinIndisponivel:
    def __init__(self, master):
        self.master = master
        
    def load_jan(self):
        self.win=Frame(self.master)
        #self.win=Toplevel()
        self.l1=Label(self.win, text='Essa interface ainda não foi implementada!')
        self.l2=Label(self.win, text='Utilizada para estudos.')
        self.l3=Label(self.win, text='Fevereiro de 2017.')
        #btnSair=Button(self.win, text='Fechar', command = self.close_window)
        obj = FrameBtnCRUD(self.win)
        self.btns = obj.getFrame()        
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()  
        #btnSair.pack()
        self.btns.pack()
        self.win.pack()
        
        #self.win.geometry('300x200')
        #self.win.transient(self.master)
        #self.win.focus_force()
        #self.win.grab_set()
        #pos_load()
        
    def pos_load(self):
        pass
        
    def pre_close(self):
        return True
        
    def close_window(self):
        if self.pre_close():
            self.win.destroy()

			
