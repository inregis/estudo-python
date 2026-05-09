salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()  # Criando uma cópia da lista para evitar modificar a original
    lista_aux.append(2)
    print(f"lista aux= {lista_aux}")  # Output: [1, 2]
    salario += bonus
    return salario

lista = [1]

novo_salario = salario_bonus(500, lista)
print(novo_salario)  # Output: 2500
print(lista)  # Output: [1]