# esse vai ser o inicializador da calculadora
from exe_001 import *

def test_adicionar():
    assert adicionar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 3) == 2

def test_multiplicar():
    assert multiplicar(4, 3) == 12

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_check_age(dicionario):
    try:
        for x in dicionario:
            print(dicionario)

    except Exception as e:
        print(f"Erro geral: {e}")

