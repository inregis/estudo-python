def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a*2 + b*3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(5, 3, somar)       # Passando a função somar como argumento
exibir_resultado(5, 3, subtrair)    # Passando a função subtrair como argumento
exibir_resultado(5, 3, test)        # Passando a função test como argumento