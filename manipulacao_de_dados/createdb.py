import sqlite3

conexao = sqlite3.connect('escola.db')  # cria e depois conecta

cursor = conexao.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER        
)
"""

)


cursor.execute(
    """CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            id_estudante INTEGER,
            FOREIGN KEY  (id_estudante) \
                REFERENCES estudantes(id)  
)
"""

)

conexao.commit()
conexao.close()