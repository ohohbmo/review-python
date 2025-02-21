# Calculadora
# Calculate

# crie uma funcao que receba dois numero e retorne a soma entre eles 
# create a function that receives two numbers and returns the sum between them
def somar(x, y):
    z = x + y 
    return z

# crie uma funcao que receba dois numero e retorne a subtração entre eles 
# create a function that receives two numbers and returns the subtraction between them
def subtrair(x, y):
    return x - y

# crie uma funcao que receba dois numero e retorne a multiplicação entre eles 
# create a function that receives two numbers and returns the multiplication between them
def multiplicar(x, y):
    return x * y

# crie uma funcao que receba dois numero e retorne a divisão entre eles 
# create a function that receives two numbers and returns the division between them
def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero")
    return x / y