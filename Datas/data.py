from datetime import timedelta, datetime

# Definição dos tipos de carros e seus respectivos tempos
tipo_carro = {
    "p": {"nome": "PEQUENO", "tempo": 30},
    "m": {"nome": "MÉDIO", "tempo": 45},
    "g": {"nome": "GRANDE", "tempo": 60}
}

def calcular_saida(tipo):
    #calculo o tempo atual
    tempo_atual = datetime.now()
    #defino que o tipo que vai ser passado para minusculo
    tipo = tipo.lower()

    #tipo no caso é uma key, que seria uma chave do dicionario, porque esta sendo passada a esquerda do :
    # e tudo que está sendo passado a direita é um valor
    # ou seja, a chave p , tem os valores nome Pequeno e tempo 30
    if tipo in tipo_carro:
        tempo_espera = tipo_carro[tipo]["tempo"]
        #aqui para acessar, eu entro no dicionario, pego a key que vai ser informada e pego o valor que eu preciso
        nome_tipo = tipo_carro[tipo]["nome"]
        tempo_saida = tempo_atual + timedelta(minutes=tempo_espera)
        print(f"O carro ({nome_tipo}) vai sair às {tempo_saida.strftime('%H:%M:%S')}")
    else:
        print("❌ Tipo inválido. Os tipos aceitos são: P, M ou G.")

# Execução
print("Qual é o tamanho do seu carro? (P, M, G)")
entrada = input("Digite o tipo do carro: ")
calcular_saida(entrada)
