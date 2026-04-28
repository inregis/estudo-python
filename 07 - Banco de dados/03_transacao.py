import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ('Teste 2', 'teste2@gmail.com'))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)", (2, 'Teste 3', 'teste3@gmail.com'))
    cursor.execute("DELETE FROM clientes WHERE id = 15")
    conexao.commit()
except Exception as exc:
    print(f"Erro ao inserir registros: {exc}")
    conexao.rollback()
finally:
    conexao.commit()

