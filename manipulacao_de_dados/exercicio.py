import sqlite3

conexao = sqlite3.connect('hotel_plus_db')
cursor = conexao.cursor()

cursor.execute(
    """
      CREATE TABLE IF NOT EXISTS usuarios(
          id INTEGER PRIMARY KEY,
          nome TEXT,
          email TEXT
      )
    """
)

conexao.commit()
conexao.close()