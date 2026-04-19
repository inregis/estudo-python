nome = "rEgIs"

print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.title())
print(nome.swapcase())

texto = "   Olá, Mundo!   "
print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"
print("####" + menu + "####")
print(menu.center(14, "#"))
print("-".join(menu))
print("-".join(nome))