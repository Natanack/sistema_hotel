from tkinter import *
from chamar_telas import *


class TelaLogin(Chamar_telas):
    def Wlogin(self):
        self.wlogin = Tk()

        self.Configwlogin()
        self.Widgetswlogin()
        self.Botoeswlogin()
        self.wlogin.mainloop()

    def Configwlogin(self):
        self.wlogin.geometry("500x400+600+300")
        #self.wlogin.config(bg='black')

    def Widgetswlogin(self):
        # entrys e labels
        self.lbl_usuario = Label(self.wlogin, text='Usuario')
        self.lbl_usuario.place(relx=0.3, rely=0.25)

        self.ent_usuario = Entry(self.wlogin)
        self.ent_usuario.place(relx=0.3, rely=0.3, relwidth=0.32)

        self.lbl_senha = Label(self.wlogin, text='Senha')
        self.lbl_senha.place(relx=0.3, rely=0.35)

        self.ent_senha = Entry(self.wlogin)
        self.ent_senha.place(relx=0.3, rely=0.4, relwidth=0.32)

    def Botoeswlogin(self):
        self.btn_acessar = Button(self.wlogin, text='Acessar')
        self.btn_acessar.bind("<Button-1>", self.telamenu)
        self.btn_acessar.place(relx=0.3, rely=0.47, relwidth=0.15)

        self.btn_cancelar = Button(self.wlogin, text='Cancelar')
        self.btn_cancelar.place(relx=0.47, rely=0.47, relwidth=0.15)

        self.btn_cadastrarse = Button(self.wlogin, text="Cadastrar-se",
                                      relief=FLAT, bd=0)
        self.btn_cadastrarse.bind("<Button-1>", self.telacadastrofuncionario)
        self.btn_cadastrarse.place(relx=0.38, rely=0.55)
