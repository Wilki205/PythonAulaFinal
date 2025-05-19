with open("Nomes.txt", "a") as arquivo:
    nome = input("Digite seu nome: ")
    arquivo.write(f"{nome}\n")