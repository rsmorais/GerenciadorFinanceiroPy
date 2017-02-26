#python 3.4
#coding: utf8

from tkinter import *
from tkinter.ttk import *
import appMenu

class Application:
    def __init__(self):
        self.window = Tk()
        self.window.title("Contabilidade")
        self.window.geometry("600x600")
        icon = PhotoImage(file='Img/py.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, icon)

    def load_menu(self):
        obj= appMenu.Main_menu(self.window)
        mainMenu = obj.get_menu()
        self.window.config(menu=mainMenu)
        self.window.mainloop()

    def main_loop(self):
        self.window.mainloop()




app = Application()
app.load_menu()
app.main_loop()








