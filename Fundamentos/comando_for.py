texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
     print()  # Imprime uma nova linha após o loop
     print("Executa no final do laço")

#exemplo de uso do função built-in com range
for numero in range(0, 51, 5):
    print(numero, end=" ")