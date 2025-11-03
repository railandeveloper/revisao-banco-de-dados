import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()


cursor.execute(
    """
    SELECT  estudantes.nome, disciplinas.nome_disciplina FROM disciplinas JOIN estudantes ON disciplinas.id_estudante == estudantes.id
    """
)

print(cursor.fetchall())