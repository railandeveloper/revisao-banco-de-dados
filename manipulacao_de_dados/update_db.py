import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()


cursor.execute(
    """
     UPDATE estudantes SET nome = ? WHERE id = ?
    """,
    ('joao', 2)
)

conexao.commit()
conexao.close()