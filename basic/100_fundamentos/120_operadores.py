# Operadores Aritméticos (Realizam operações matemáticas)
a = 10
b = 3

print(a + b)  # Soma -> 13
print(a - b)  # Subtração -> 7
print(a * b)  # Multiplicação -> 30
print(a / b)  # Divisão -> 3.3333...
print(a // b) # Divisão inteira -> 3
print(a % b)  # Módulo (resto da divisão) -> 1
print(a ** b) # Exponenciação -> 10³ = 1000

# Operadores de Comparação (Retornam True ou False)
x = 5
y = 8

print(x == y)  # Igualdade -> False
print(x != y)  # Diferente -> True
print(x > y)   # Maior que -> False
print(x < y)   # Menor que -> True
print(x >= y)  # Maior ou igual -> False
print(x <= y)  # Menor ou igual -> True

# . Operadores Lógicos (Usados para combinações de condições)
p = True
q = False

print(p and q)  # E lógico -> False
print(p or q)   # OU lógico -> True
print(not p)    # Negação -> False

# Operadores de Atribuição
n = 10
n += 5  # Equivalente a n = n + 5
print(n)  # 15

n -= 3  # n = n - 3
print(n)  # 12

n *= 2  # n = n * 2
print(n)  # 24

n /= 4  # n = n / 4
print(n)  # 6.0

n //= 2  # n = n // 2 (divisão inteira)
print(n)  # 3

n %= 2  # n = n % 2 (resto da divisão)
print(n)  # 1

n **= 3  # n = n ** 3 (potência)
print(n)  # 1

# Operadores de Identidade (is, is not)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (aponta para o mesmo objeto na memória)
print(a is c)   # False (c é outro objeto, mesmo com valores iguais)
print(a is not c)  # True

# Operadores de Associação (in, not in)
frutas = ["maçã", "banana", "uva"]

print("banana" in frutas)   # True
print("laranja" not in frutas)  # True
