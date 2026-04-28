import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))'
    )

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()
  

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome ASC;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))
    
cliente = recuperar_cliente(cursor, 2)  
print(dict(cliente)) 

print(f'Seja bem-vindo, {cliente["nome"]}!')
print(f'Seja bem-vindo, {cliente[1]}!')

#dados = [
#    ('Regis', 'regis@gmail.com'),
 #   ('Merlen', 'merlen@gmail.com'),
 #   ('Wesley', 'wesley@gmail.com'),
 #  ('Wyllian', 'wyllian@gmail.com')
#]

#inserir_muitos(conexao, cursor, dados)


