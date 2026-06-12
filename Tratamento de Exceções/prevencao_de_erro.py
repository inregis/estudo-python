numero = input("Digite um número: ")
if numero.isdigit():
    numero = int(numero)
    print(numero)
else:
    print("Entrada inválida: não é um número")