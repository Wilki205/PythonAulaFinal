nomes = []

def menu():
    while True:
        print("\nMENU")
        print("1 - Adicionar nome")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_nomes()
        elif opcao == "2":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def inserir_nomes():
    nome = input("Digite o novo nome: ")
    nomes.append(nome)
    print("Nome adicionado!")

    with open("Nomes.txt", "a") as arquivo:
        arquivo.write(nome + "\n")

menu()
