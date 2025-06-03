
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): 
 #self é o objeto que está sendo criado, como se fosse um this no jscript
       #precisamos do init para poder criar o objeto bicicleta
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor

    def buzinar(self): 
        print("bi bi bi")

    def parar(self): 
        print("parando")

    def correr(self): 
        print("correndo")

    #def __str__(self): 
    #    return f"Bicicleta({self.cor}, {self.modelo}, {self.ano}, {self.valor})"
    def __str__(self): 
        return f"{self.__class__.__name__} : {','.join([f'{chave} é {valor}' for chave, valor in self.__dict__.items()])}"
    #{self.__class__.__name__} - pega o nome da classe que é Bicicleta
    #','.join - junta os valores em uma string
    #f'{chave} é {valor}' for chave, valor - basicamente pra cada index eu tenho um value, então vou fazer um loop for, para pegar todos os index e values
    #self.__dict__.items() - o looping será feito dentro do dicionário, que é o __dict__, que é um dicionário que contém todos os atributos e valores do objeto



caloi = Bicicleta("azul", "caloi", 2020, 1000)
caloi.buzinar()
print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

#SEMPRE QUE EU CHAMAR PRINT, com somente o objeto dentro dele, ele vai chamar o __str__ do objeto
print(caloi)

monark = Bicicleta("vermelha", "monark", 2021, 1500)
