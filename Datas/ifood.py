

from datetime import datetime, timedelta

ifood_tempo = {
    "1": {"nome": "Cachorro Quente", "tempo": 30},
    "2": {"nome": "X-Salada", "tempo": 45},
    "3": {"nome": "X-Bacon", "tempo": 60},
    "4": {"nome": "X-Tudo", "tempo": 75},
    "5": {"nome": "Bauru", "tempo": 30},
    "6": {"nome": "Refrigerante", "tempo": 20}
}

def calcular_tempo_pedido(pedido):
    if pedido in ifood_tempo:
        #faltou essa lógica de diminuir o minuto com timedelta
        tempo_espera = datetime.now() - timedelta(minutes=ifood_tempo[pedido]["tempo"])
        nome_pedido = ifood_tempo[pedido]["nome"]
        #faltou a lógica de somar o tempo de espera
        
        print(f'Você está esperando um {nome_pedido}. Ele ficará pronto às {tempo_espera.strftime("%H:%M:%S")}.')
    else:
        print("❌ Pedido inválido. Escolha um número de 1 a 6.")

# Execução
print("Qual é o seu pedido?")
print("1 - Cachorro Quente\n2 - X-Salada\n3 - X-Bacon\n4 - X-Tudo\n5 - Bauru\n6 - Refrigerante")
#aqui eu pego os dados que o usuário escrever e jogo na função
pedido = input("Digite o número do seu pedido: ")
calcular_tempo_pedido(pedido)
