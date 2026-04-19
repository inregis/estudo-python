MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Digite a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Você é menor de idade, não pode tirar a CNH.")   


if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH.")
else:
    print("Você é menor de idade, não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Você é menor de idade, mas pode fazer aulas teóricas, mas não pode fazer aulas práticas.")   
else:
    print("Você é menor de idade, não pode tirar a CNH.")