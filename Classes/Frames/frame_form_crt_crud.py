from tkinter import *
from Classes.DB.modulo_cursor import ModuloCursor
from Classes.Scripts.scriptSQL import RecuperaCRT
from Classes.DB.tbl_CRT import TBL_CRT_Cartao as CRT
from Classes.Util.popup_multi import PopupMulti

class FrameFormCrtCRUD:
    #cria um frame com os botões utilizados no CRUD
    def __init__(self, master):
        self.master = master

        self.frame = Frame(self.master)
        self.Titulo = Label(self.frame, text='---Formulario---')
        self.idCartao = None
        self.row_count = 0
        
        self.lbNmCartao = Label(self.frame, text='Nome Cartão: ')
        self.lbDiaFechamento = Label(self.frame, text='Dia de Fechamento: ')        
        self.lbDiaVencimento = Label(self.frame, text='Dia de Vencimento: ')
        self.txtNmCartao = Entry(self.frame)
        self.txtDtFechamento = Entry(self.frame)        
        self.txtDiaVencimento = Entry(self.frame)
        
        self.Titulo.grid(row=0, column=0, columnspan=4, sticky=E+W)
        self.lbNmCartao.grid(row=1, column=0)
        self.lbDiaFechamento.grid(row=2, column=0)
        self.lbDiaVencimento.grid(row=3, column=0)
        self.txtNmCartao.grid(row=1, column=1)
        self.txtDtFechamento.grid(row=2, column=1)    
        self.txtDiaVencimento.grid(row=3, column=1)

        obj = RecuperaCRT()
        self.sql = obj.get_sql()
    
    #retorna o frame, para caso o usuário queira
    #altera a posição do mesmo na interface    
    def get_frame(self):
        return self.frame

    #método que foi setado ao botão recuperar da key
    #ele chama o objeto reponsavel pela consulta 
    def retrieve(self, arg):
        cursor = ModuloCursor()
        self.dataSQL = cursor.retrieve(self.sql, arg)
        self.pos_retrieve()

    #metodo executado logo após o retrieve
    #responsavel por setar os valores obtidos no retrieve
    def pos_retrieve(self):
        if len(self.dataSQL) > 0:
            if len(self.dataSQL) > 1:
                args = []
                args.append(self.return_popup)
                args.append('---Selecione o Cartão---')
                args.append(1)
                self.popup = PopupMulti(self.master, self.dataSQL)
                self.popup.load_jan(args)

            else:
                self.idCartao = self.dataSQL[0][0]
                self.txtNmCartao.delete(0, 'end')
                self.txtNmCartao.insert(0, self.dataSQL[0][1])
                self.txtDiaVencimento.delete(0, 'end')
                self.txtDiaVencimento.insert(0, self.dataSQL[0][2])
                self.txtDtFechamento.delete(0, 'end')
                self.txtDtFechamento.insert(0, self.dataSQL[0][3])

        else:
            self.new_row()

    #Método que reseta os valores na form
    #Esse método é chamado pelo botão Novo da key
    def new_row(self):
        self.idCartao = None
        self.txtNmCartao.delete(0, 'end')
        self.txtDtFechamento.delete(0, 'end')
        self.txtDiaVencimento.delete(0, 'end')

    #Métdo executado antes do Update para fazer as validações
    def pre_update(self):
        return True

    #Método que pega os argumentos utilizados para o retrieve na Form
    def get_args(self):
        dic = {}
        self.listArgs = []
        dic['CRT_idCartao'] = self.idCartao
        dic['CRT_dsCartao'] = self.txtNmCartao.get()
        dic['CRT_dtVencimento'] = self.txtDiaVencimento.get()
        dic['CRT_dtFechamento'] = self.txtDtFechamento.get()
        self.listArgs.append(dic)

    #métodos executado pelo botão salvar do frame de botões Crud
    def update(self):
        if self.pre_update():
            self.get_args()
            bd = CRT()
            if(self.idCartao == None):                
                bd.insert(self.listArgs)
            else:
                bd.edit(self.listArgs)

    def pos_delete(self):
        self.new_row()

    def pre_delete(self):
        return True

    def delete(self):
        if self.pre_delete():
            self.get_args()
            bd = CRT()
            if(self.idCartao == None):                
                #exibir msm de erro
                pass
            else:
                bd.delete(self.listArgs)

            self.pos_delete();

    def return_popup(self, number):
        self.idCartao = self.dataSQL[number][0]
        self.txtNmCartao.delete(0, 'end')
        self.txtNmCartao.insert(0, self.dataSQL[number][1])
        self.txtDiaVencimento.delete(0, 'end')
        self.txtDiaVencimento.insert(0, self.dataSQL[number][2])
        self.txtDtFechamento.delete(0, 'end')
        self.txtDtFechamento.insert(0, self.dataSQL[number][3])
        self.popup.close_window()