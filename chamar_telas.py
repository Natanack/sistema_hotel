from frm_cadastro import *
from frm_menu import *
from efeito_menu import *
class Chamar_telas(TelaCadfuncionario,
                   TelaMenu,
                   Efeitos_menu):
    def telacadastrofuncionario(self,event):
        self.Wcadfuncionario()
    def telamenu(self,event):
        self.Wmenu()
    def tela_visaogeral(self,event):
        self.frame_info_funcionario()
        self.widgets_info_funcionario()
        self.frame_graficos_menu()
        self.frame_info_apartamentos()
        self.widgets_info_apartamentos()
        self.widgets_info_acomodacoes_ocupadas()
        self.widgets_info_acomodacoes_vagas()
        #self.aumentafont_btn_visaogeral()
    
