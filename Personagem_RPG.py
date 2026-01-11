class Personagem:
    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.forca = 10
        self.destreza = 10
        self.inteligencia = 10
    def exibir_ficha(self):
        print(f"Ficha:")
        print(f"Nome: {self.nome} | Raça: {self.raca} | Classe: {self.classe}")
        print(f"Nível: {self.nivel}")