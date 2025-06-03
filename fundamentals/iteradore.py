def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

#aqui ele vai printar tudo que estiver dentro da funcao
for i in meu_gerador(numeros=[1,2,3,4,5]):
    print(i)