linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(sorted(linguagens, key=lambda x: len(x)))
# O resultado é uma nova lista ordenada com base no comprimento das strings, do menor para o maior.


print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# O resultado é uma nova lista ordenada com base no comprimento das strings, do maior para o menor.
print(sorted(linguagens))
# O resultado é uma nova lista ordenada em ordem alfabética.
