#Listas
frutas = ["maça", "banana", "laranja"]
print(frutas)

#Com o list, eu separo uma string em letras
letras =list("velozesEFuriosos")
print(letras)

#pegar o primeiro item 
frutas = ["maça", "banana", "laranja"]
frutas[0] #pega o primeiro item
frutas[-1] #pega o último item

#Matriz
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

matriz[0] #pega a primeira linha = [1,2,3]
matriz[0][0] #pega o primeiro item da primeira linha = 1
matriz[0][-1] #pega o último item da primeira linha = 3
matriz[2][1] #pega o segundo item da terceira linha = 8

name = "Eduardo"
print(name.split()) #['E', 'd', 'u', 'a', 'r', 'd', 'o']

#Loops em listas 
carros = ["Fusca", "Civic", "Palio"]

for indice, carro in enumerate(carros):
    print(f"Carro {indice}: {carro}")
    #preciso passar o enumerate, quando tiver duas listas, para saber qual é o índice de cada item
    #assim o primeiro valor do for, vai ser o indice e o segundo o valor o nome


#Exemplos de filtros
numeros = [1,2,3,4,5,6,7,"edu",4,8,9,]
pares = []

numeros.remove("edu")
print(numeros)
print(numeros.count(4))

for numero in numeros: 
    if numero % 2 == 0:
        pares.append(numero)
# se o numero for par eu vou colocar dentro da lista de pares
print(pares)


