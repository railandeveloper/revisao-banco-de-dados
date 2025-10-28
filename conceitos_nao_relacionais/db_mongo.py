from pymongo import MongoClient

# Conecta ao servidor do MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Cria ou acessa o banco
db = client['escola']

# Cria ou acessa a coleção
estudantes = db['estudantes']

# Insere um documento
estudantes.insert_one({'nome': 'Pedro', 'idade': 22})

# Mostra todos os documentos
for estudante in estudantes.find():
    print(estudante)
