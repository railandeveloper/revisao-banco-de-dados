import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()


#cursor.execute(
#    """
#        SELECT * FROM estudantes
#    """
#)


cursor.execute(
    """
    SELECT * FROM disciplinas
    """
)

disciplinas = cursor.fetchall()
conexao.commit()

for materia in disciplinas:
    print(materia)
    
conexao.close()    
# conexao.commit()

# estudantes = cursor.fetchall()
# for aluno in estudantes:
#     print(aluno)
    
# conexao.close()    