print("Hello world!")

#Pode se declarar várias váriaveis na mesma linha em python
age,name = (23, "Eduardo")
print(f'Meu nome é {name} e tenho {age} anos') #o f antes, permite inserir variáveis dentro da string

#Python não tem constante, tudo que for constante deve ser escrito em maiúsculo
PI = 3.14
AGE = 23
NAME = "Eduardo"

#Conversão de tipos
number = 10.7
preco = int(number) 
print(preco)

#Conveter string para number
new_price = "10.7"
preco = float(new_price)

#entrada - input 
your_name = input("Qual o seu nome? ")
print(f'Olá {your_name}, tudo bem?')

#Operações matemáticas
saldo = 1000
saque = 100
novo_saldo = saldo -saque
print(f'Seu saldo é {saldo > saque}')

#Mesma posição de memória
#Quer dizer que as duas variáveis estão apontando para o mesmo objeto
curso = "Python"
nome_curso = curso
print(curso is nome_curso) 

#Associação de valores

frutas = ["maçã", "banana", "laranja"]
print("laranja" in frutas)

#Condicionais 

digite = int(input("Quantos anos você tem?"))
if digite >= 18:
        print("Você é maior de idade")

#Estrutura de repetição

  #FOR
texto = input("Digite um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print("Vogal")

#RANGE
#Range argumentos
#range(stop)
print(list(range(10)))

#range (start, stop) - aqui mostra um ponto de partida e um de parada
print(list(range(2,10)))

#range(start, stop, step) - aqui eu vou começar no2, terminar no10 e ir de 5 em 5
print(list(range(2,50, 5)))

#Fatiamento 
#pega os valores do index 
nome = "Eduardo Alves Palhares Júnior"
print(nome[0:6]) #Eduardo 
print(nome[7:12]) #Alves
print(nome[13:20]) #Palhares
print(nome[::-1]) #inverte a string


#