#Herança Simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado")

    #somente com o método __srtr__ o print do objeto vai funcionar
    def __str__(self):
        return f"Veículo: {self.cor}, Placa: {self.placa}, Rodas: {self.numero_rodas}"
        

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass



moto = Motocicleta("preta", "ABC1234", 2)
print(moto)
moto.ligar_motor()