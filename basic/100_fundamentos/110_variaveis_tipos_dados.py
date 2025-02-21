# variaveis (mutaveis)

nome = "Alice"  # Variável do tipo string
idade = 25      # Variável do tipo inteiro
altura = 1.75   # Variável do tipo float

print(nome, idade, altura)

# constantes (imutaveis)
PI = 3.14159
GRAVIDADE = 9.8
print(PI, GRAVIDADE)

# Inteiro (int)
idade = 25  
print(type(idade))  # <class 'int'>

# Ponto flutuante (float)
altura = 1.75  
print(type(altura))  # <class 'float'>

# Número complexo (complex)
numero_complexo = 3 + 4j  
print(type(numero_complexo))  # <class 'complex'>

# strings
nome = "Alice"
print(type(nome))  # <class 'str'>

# Boleano 
ativo = True
print(type(ativo))  # <class 'bool'>

# Listas
numeros = [1, 2, 3, 4, 5]
print(type(numeros))  # <class 'list'>

# tuplas
coordenadas = (10, 20)
print(type(coordenadas))  # <class 'tuple'>


# conjuntos
valores_unicos = {1, 2, 3, 3, 4}
print(type(valores_unicos))  # <class 'set'>


# dicionarios
#pessoa = {"nome": "Carlos", "idade": 30, "cidade": "São Paulo"}
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
    }

print(type(pessoa))  # <class 'dict'>
