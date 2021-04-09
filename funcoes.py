from tkinter import messagebox
from banco import Banco


class Funcoes(Banco):
    def Cadastro_funcionario(self, event):
        self.inserirfuncionarios()
        messagebox.showinfo("Aviso", "Funcionario Cadastrado")
        self.frm_cadfuncionario.destroy()
    
