import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

#cursor.execute(
#"""INSERT INTO estudantes(nome, idade) \
      # VALUES (?, ?)
   # """,
   ##)

cursor.execute(
    """
    INSERT INTO disciplinas (id_estudante, nome_disciplina)
    VALUES (?, ?)
    """,
    (2, 'Mtematica')
)


conexao.commit()
conexao.close()