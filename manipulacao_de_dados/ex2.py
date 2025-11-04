import sqlite3

conexao = sqlite3.connect('hotel_plus_db')
cursor = conexao.cursor()

cursor.execute(
    """
      INSERT INTO usuarios (nome, email)
      VALUES (?, ?)
    """,
    ('antonia', 'toniaadv.com')
)

conexao.commit()
conexao.close()