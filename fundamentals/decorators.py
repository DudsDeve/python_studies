def meu_decorator (funcao):
    def envelope(*args, **kwargs): 
        print ("antes da funcao")
        funcao(*args, **kwargs)
        print ("depois da funcao")
    return envelope
#aqui basicamente é uma função dentro de uma função

#o @meu_decorator serve para chamar a funcao envelope

#com o *args e o **kwargs eu posso passar quantos parametros eu quiser
@meu_decorator
def minha_funcao (nome, idade, peso, altura) :
    print (f'ola {nome}{idade} {peso} {altura}')

minha_funcao("Eduardo", 28, 15 , 35)