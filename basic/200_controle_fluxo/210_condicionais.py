idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de atingir a maioridade!")
else:
    print("Você é maior de idade.")