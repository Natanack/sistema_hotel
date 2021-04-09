from tkinter import *
from funcoes import Funcoes
from efeito_menu import *

class TelaMenu(Funcoes,Efeitos_menu):
    def Wmenu(self):
        self.wlogin.destroy()
        self.frm_menu = Tk()
        self.Configwmenu()
        self.frames_menu()
        self.frame_info_funcionario()
        self.widgets_info_funcionario()
        self.frame_graficos_menu()
        self.frame_info_apartamentos()
        self.widgets_info_apartamentos()
        self.widgets_info_acomodacoes_ocupadas()
        self.widgets_info_acomodacoes_vagas()
        self.navbotoes()
        
        self.frm_menu.mainloop()

    def Configwmenu(self):
        self.frm_menu.geometry("1024x768+400+50")
        self.frm_menu.config(bg='#fff')
    def frames_menu(self):
        self.frame_left = Frame(self.frm_menu, bd=2, relief=GROOVE,bg='#313e51')
        self.frame_left.place(relx=0, rely=0.1, relwidth=0.1, relheight=0.5)

        self.frame_principal = Frame(self.frm_menu, bd=2, relief=GROOVE,bg='#fff')
        self.frame_principal.place(relx=0.15, rely=0.1, relwidth=0.8, relheight=0.8)

        self.frame_top = Frame(self.frm_menu, bd=2, relief=GROOVE,bg='#1cb397')
        self.frame_top.place(relx=0.15, rely=0, relwidth=0.8, relheight=0.1)
    def frame_info_funcionario(self):
        self.frame_funcionario = Frame(self.frame_principal,bd=1.5,relief=GROOVE,bg='#fff')
        self.frame_funcionario.place(relx=0,rely=0,relwidth=0.3,relheight=0.3)
    def widgets_info_funcionario(self):
        self.lbl_boas_vindas = Label(self.frame_funcionario,text='Seja bem vindo,',bg='#fff')
        self.lbl_boas_vindas.place(relx=0.02,rely=0.02,relwidth=0.35)

        self.lbl_nome_funcionario = Label(self.frame_funcionario,text='Nome',bg='#fff')
        self.lbl_nome_funcionario.place(relx=0.4,rely=0.02,relwidth=0.15)
    def frame_graficos_menu(self):
        self.frame_grafico = Frame(self.frame_principal,bd=1.5,relief=GROOVE,bg='#fff')
        self.frame_grafico.place(relx=0,rely=0.3,relwidth=0.999,relheight=0.699)
    def frame_info_apartamentos(self):
        self.frame_info_apt = Frame(self.frame_principal,bd=1.5,relief=GROOVE,bg='#fff')
        self.frame_info_apt.place(relx=0.3,rely=0,relwidth=0.7,relheight=0.3)

        self.frame_qtd_hospede = Frame(self.frame_info_apt,bd=1.5,relief=FLAT,bg='#1cb397')
        self.frame_qtd_hospede.place(relx=0.02,rely=0.14,relwidth=0.3,relheight=0.7)

        self.frame_acomodacoes_ocupadas = Frame(self.frame_info_apt,bd=1.5,relief=FLAT,bg='#24c5c9')
        self.frame_acomodacoes_ocupadas.place(relx=0.35,rely=0.14,relwidth=0.3,relheight=0.7)

        self.frame_acomodacoes_vagas = Frame(self.frame_info_apt,bd=1.5,relief=FLAT,bg='#f9ab5a')
        self.frame_acomodacoes_vagas.place(relx=0.68,rely=0.14,relwidth=0.3,relheight=0.7)

    def widgets_info_apartamentos(self):
        self.lbl_quantidade_hospede = Label(self.frame_qtd_hospede,text='Quantidade Hospedes',font=('verdana',9),bg='#1cb397',fg='#fff')
        self.lbl_quantidade_hospede.place(relx=0.05,rely=0.1)

        self.lbl_hoje = Label(self.frame_qtd_hospede,text='Hoje',font=('verdana',10,"bold"),bg='#1cb397',fg='#fff')
        self.lbl_hoje.place(relx=0.35,rely=0.25)

        self.lbl_num_quantidade_hospede = Label(self.frame_qtd_hospede,text='0',font=('verdana',12,"bold"),bg='#1cb397',fg='#fff')
        self.lbl_num_quantidade_hospede.place(relx=0.42,rely=0.5)
    def widgets_info_acomodacoes_ocupadas(self):
        self.lbl_acomodacoes_ocupadas = Label(self.frame_acomodacoes_ocupadas,text='Acomodaçoes Ocupadas',font=('verdana',9),bg='#24c5c9',fg='#fff')
        self.lbl_acomodacoes_ocupadas.place(relx=0.02,rely=0.1)

        self.lbl_hoje_acomodacoes_ocupadas = Label(self.frame_acomodacoes_ocupadas,text='Hoje',font=('verdana',10,"bold"),bg='#24c5c9',fg='#fff')
        self.lbl_hoje_acomodacoes_ocupadas.place(relx=0.35,rely=0.25)

        self.lbl_num_ocupadas = Label(self.frame_acomodacoes_ocupadas,text='0',font=('verdana',12,"bold"),bg='#24c5c9',fg='#fff')
        self.lbl_num_ocupadas.place(relx=0.42,rely=0.5)

    def widgets_info_acomodacoes_vagas(self):
        self.lbl_acomodacoes_vagas = Label(self.frame_acomodacoes_vagas,text='Acomodacoes Vagas',font=('verdana',9),bg='#f9ab5a',fg='#fff')
        self.lbl_acomodacoes_vagas.place(relx=0.05,rely=0.1)

        self.lbl_hoje_vagas= Label(self.frame_acomodacoes_vagas,text='Hoje',font=('verdana',10,"bold"),bg='#f9ab5a',fg='#fff')
        self.lbl_hoje_vagas.place(relx=0.35,rely=0.25)

        self.lbl_num_vagas= Label(self.frame_acomodacoes_vagas,text='0',font=('verdana',12,"bold"),bg='#f9ab5a',fg='#fff')
        self.lbl_num_vagas.place(relx=0.42,rely=0.5)
    def navbotoes(self):
        self.btn_visaogeral = Button(
            self.frame_left, text="Visão Geral", bd=0, relief=FLAT,bg='#313e51',fg='#fff')
        self.btn_visaogeral.bind("<Button-1>",self.tela_visaogeral)
        self.btn_visaogeral.place(relx=0.1, rely=0.05)

        self.btn_reservas = Button(
            self.frame_left, text="Reservas", bd=0, relief=FLAT,bg='#313e51',fg='#fff')
        self.btn_reservas.place(relx=0.1, rely=0.15)

        self.btn_cadastros = Button(
            self.frame_left, text="Cadastros", bd=0, relief=FLAT,bg='#313e51',fg='#fff')
        self.btn_cadastros.place(relx=0.1, rely=0.25)

        self.btn_reservas = Button(
            self.frame_left, text="Caixa", bd=0, relief=FLAT,bg='#313e51',fg='#fff')
        self.btn_reservas.place(relx=0.1, rely=0.35)

        self.btn_reservas = Button(
            self.frame_left, text="Estoque", bd=0, relief=FLAT,bg='#313e51',fg='#fff')
        self.btn_reservas.place(relx=0.1, rely=0.45)

        self.btn_reservas = Button(
            self.frame_left, text="Relatorios", bd=0, relief=FLAT,bg='#313e51',fg='#fff')
        self.btn_reservas.place(relx=0.1, rely=0.55)

    
