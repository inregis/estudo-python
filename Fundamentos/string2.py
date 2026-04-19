nome = "Regis"
idade = 44
profissao = "Programador"
linguagem = "Python"
saldo = 20250.355

dados = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem, "saldo": 20250.35}

print("Nome: %s Idade: %d Profissão: %s Linguagem: %s" % (nome, idade, profissao, linguagem))
print("Nome: {} Idade: {} Profissão: {} Linguagem: {}".format(nome, idade, profissao, linguagem))
print("Nome: {0} Idade: {1} Profissão: {2} Linguagem: {3}".format(nome, idade, profissao, linguagem))
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}")
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**locals()))
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**dados))
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo:,.2f}")
