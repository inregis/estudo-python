def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("obrigado por usar o nosso caixa eletrônico.")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("valor depositado!")
    print("o seu saldo atual é de R$ ", saldo)

sacar(100)       
depositar(200)