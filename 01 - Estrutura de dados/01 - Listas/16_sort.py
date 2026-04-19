linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort()  # Ordena os elementos da lista em ordem alfabética
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(reverse=True)  # Ordena os elementos da lista em ordem alfabética reversa
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x))  # Ordena os elementos da lista pelo comprimento das strings
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordena os elementos da lista pelo comprimento das strings em ordem reversa
print(linguagens)

