class Cachorro:

    #eu inicializo 
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe Cachorro")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    #depois quando não preciso utilizar mais eu removo
    def __del__ (self):
        print("Destruindo a classe Cachorro")
    
    
    def falar(self):
        print("auauau")

    def criar_cachorro():
        c = Cachorro("Rex", "preto", False)

c = Cachorro("Rex", "preto")
c.falar()
print(c.nome)