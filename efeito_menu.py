


class Efeitos_menu():
    def aumentafont_btn_visaogeral(self):
        self.btn_visaogeral.config(font="pelvica 11 bold")
        self.diminuirfont_btn_cadastros()
    def diminuirfont_btn_visaogeral(self):
        self.btn_visaogeral.config(font="pelvica 8")
    def aumentarfont_btn_cadastros(self):
        self.btn_cadastros.config(font="pelvica 11 bold")
        self.diminuirfont_btn_visaogeral()
    def diminuirfont_btn_cadastros(self):
        self.btn_cadastros.config(font="pelvica 8 ")
