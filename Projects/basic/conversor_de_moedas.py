import requests

def converter_moeda(valor, de, para):
    url = f"https://api.exchangerate.host/convert?from={de}&to={para}&amount={valor}&access_key=11cf83f51778f1155f6872431288b025"
    #aqui to pegando um request da api
    resposta = requests.get(url)
    #utilizando o método get pra fazer a chamada e retornando um json
    
    dados = resposta.json()
    print(dados)

    if resposta.status_code == 200 and dados['success']:
        convertido = dados["result"]
        print(f"\n💱 {valor} {de} = {convertido:.2f} {para}")
    else:
        print("❌ Erro na conversão!")

print("=== Conversor de Moedas ===")
valor = float(input("Digite o valor: "))
de = input("Converter de (ex: BRL, USD, EUR): ").upper()
para = input("Para (ex: USD, EUR, BRL): ").upper()

converter_moeda(valor, de, para)
