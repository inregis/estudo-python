Lista = [1, "Python", [40, 50, 20]]

l2 = Lista.copy()

print(Lista)

print(id(l2), id(Lista))

l2[0] = 2

print(l2)
print(Lista)