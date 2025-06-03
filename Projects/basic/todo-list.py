import json  # Biblioteca para trabalhar com arquivos JSON
import os    # Biblioteca para interagir com o sistema de arquivos

# Nome do arquivo onde as tarefas serão salvas
ARQUIVO = "tarefas.json"

# Função para carregar as tarefas salvas no arquivo
def carregar_tarefas():
    # Verifica se o arquivo já existe
    if os.path.exists(ARQUIVO):
        # Abre o arquivo no modo leitura
        with open(ARQUIVO, "r") as f:
            # Lê o conteúdo JSON e retorna como lista
            return json.load(f)
    # Se o arquivo não existir, retorna uma lista vazia
    return []

# Função para salvar as tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    # Abre o arquivo no modo escrita
    with open(ARQUIVO, "w") as f:
        # Salva a lista de tarefas no formato JSON
        json.dump(tarefas, f, indent=2)
        
        #indent=2: deixa o arquivo bonito e legível, com indentação de 2 espaços (ex: formata em estilo árvore).



# Função para exibir as tarefas no terminal
def exibir_tarefas(tarefas):
    print("\n📋 Suas tarefas:")
    # Se a lista estiver vazia, mostra mensagem
    if not tarefas:
        print("Nenhuma tarefa.")
    # Exibe cada tarefa com número (começando do 1)
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

# Função principal com o menu
def menu():
    # Carrega as tarefas do arquivo (ou lista vazia)
    tarefas = carregar_tarefas()

    # Loop principal do programa
    while True:
        # Exibe o menu
        print("\n=== To-Do List ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        # Adiciona nova tarefa
        if opcao == "1":
            nova = input("Digite a nova tarefa: ")
            tarefas.append(nova)               # Adiciona na lista
            salvar_tarefas(tarefas)            # Salva no arquivo
            print("✅ Tarefa adicionada!")

        # Exibe tarefas existentes
        elif opcao == "2":
            exibir_tarefas(tarefas)

        # Remove uma tarefa
        elif opcao == "3":
            exibir_tarefas(tarefas)
            # Solicita o número da tarefa para remover
            idx = int(input("Número da tarefa a remover: ")) - 1
            # Verifica se o índice é válido
            if 0 <= idx < len(tarefas):
                removida = tarefas.pop(idx)    # Remove da lista
                salvar_tarefas(tarefas)        # Salva alteração
                print(f"❌ Tarefa removida: {removida}")
            else:
                print("Número inválido.")

        # Sai do programa
        elif opcao == "0":
            print("👋 Saindo...")
            break

        # Opção inválida
        else:
            print("Opção inválida!")

# Inicia o programa chamando o menu
menu()
