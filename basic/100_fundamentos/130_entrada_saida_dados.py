#  Entrada de dados (input())
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")
idade = int(input("Digite sua idade: "))  # Converte a entrada para inteiro
print("Daqui a 10 anos, você terá", idade + 10, "anos.")

#Saída de dados (print())
print("Olá, mundo!")  # Saída: Olá, mundo!
nome = "Alice"
idade = 25
print("Nome:", nome, "| Idade:", idade)
nome = "Carlos"
altura = 1.75
print(f"{nome} tem {altura}m de altura.")  # Usa `f` antes da string para interpolação
with open("saida.txt", "w") as arquivo:
    arquivo.write("Esse texto será salvo no arquivo!")
