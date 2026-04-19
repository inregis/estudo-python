conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso docheque especial!")
    else:
        print("Saldo insuficiente para realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque!")

else:
    print("O sistema não reconheceu o tipo de conta. Por favor, verifique com o seu gerente.")