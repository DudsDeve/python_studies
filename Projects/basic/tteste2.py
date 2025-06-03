class Usuario:
    def __init__(self, nome, email, senha, saldo, limite_aprovado):
        self.nome = nome
        self.email = email
        self._senha = senha
        self._saldo = saldo
        self.limite_aprovado = limite_aprovado

    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nSaldo: R${self._saldo:.2f}\nLimite Aprovado: R${self.limite_aprovado:.2f}"

# Função para cadastrar usuário
def cadastrar_usuario():
    print("=== Cadastro de Novo Usuário ===")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    saldo = float(input("Saldo Inicial: R$ "))
    limite = float(input("Limite Aprovado: R$ "))
    
    print("\n✅ Usuário cadastrado com sucesso!\n")
    print(Usuario(nome, email, senha, saldo, limite))
    
   

cadastrar_usuario()