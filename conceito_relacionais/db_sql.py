import sqlite3


conexao = sqlite3.connect('escola.banco')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)                                             
""")

cursor.execute(
    'INSERT INTO estudantes (nome, idade)\
     VALUES (?, ?)', ('JOAO', 20)
)

conexao.commit()

cursor.execute('SELECT * FROM estudantes')
print(cursor.fetchall())

conexao.close()