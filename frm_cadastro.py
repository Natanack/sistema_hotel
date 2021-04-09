from tkinter import *
from funcoes import *
from banco import Banco


class TelaCadfuncionario(Funcoes):
    def Wcadfuncionario(self):
        self.frm_cadfuncionario = Toplevel()
        self.configfrmcadfuncionario()
        self.widgetscadfuncionario()
        self.botoescadfuncionario()

    def configfrmcadfuncionario(self):
        self.frm_cadfuncionario.geometry("200x300+730+300")
        #self.frm_cadfuncionario.config(bg='black')

    def widgetscadfuncionario(self):
        self.lbl_nomeFuncionario = Label(self.frm_cadfuncionario,
                                         text="Nome", fg='black')
        self.lbl_nomeFuncionario.place(relx=0.2, rely=0.25)

        self.ent_nomeFuncionario = Entry(self.frm_cadfuncionario)
        self.ent_nomeFuncionario.place(relx=0.2, rely=0.32)

        self.lbl_usuarioFuncionario = Label(self.frm_cadfuncionario,
                                            text="usuario", fg='black')
        self.lbl_usuarioFuncionario.place(relx=0.2, rely=0.39)

        self.ent_usuariouncionario = Entry(self.frm_cadfuncionario)
        self.ent_usuariouncionario.place(relx=0.2, rely=0.46)

        self.lbl_senhaFuncionario = Label(self.frm_cadfuncionario,
                                          text="Senha", fg='black')
        self.lbl_senhaFuncionario.place(relx=0.2, rely=0.53)

        self.ent_senhaFuncionario = Entry(self.frm_cadfuncionario)
        self.ent_senhaFuncionario.place(relx=0.2, rely=0.59)

    def botoescadfuncionario(self):
        self.btn_cadastrarfuncionario = Button(
            self.frm_cadfuncionario, text='Cadastrar')
        self.btn_cadastrarfuncionario.bind(
            "<Button-1>", self.Cadastro_funcionario)
        self.btn_cadastrarfuncionario.place(relx=0.33, rely=0.68)

        self.btn_voltar = Button(self.frm_cadfuncionario, text='Voltar')
        self.btn_voltar.config(command=self.frm_cadfuncionario.destroy)
        self.btn_voltar.place(relx=0.38, rely=0.78)
