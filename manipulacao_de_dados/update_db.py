import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()


cursor.execute(
    """
     UPDATE disciplinas SET nome_disciplina = ? WHERE id = ?
    """,
    ('python', 2)
)

conexao.commit()
conexao.close()