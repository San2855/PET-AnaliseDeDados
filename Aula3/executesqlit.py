import sqlite3

# Conecta a um banco de dados (cria um novo se ele não existir)
conn = sqlite3.connect('meu_banco.db')

# Cria um cursor para executar consultas
cursor = conn.cursor()

# Cria uma tabela
cursor.execute(
    '''CREATE TABLE minha_tabela (id INTEGER PRIMARY KEY, nome TEXT)''')

# Insere alguns dados na tabela
cursor.execute("INSERT INTO minha_tabela VALUES (1, 'Fulano')")
cursor.execute("INSERT INTO minha_tabela VALUES (2, 'Ciclano')")

# Faz o commit dos dados
conn.commit()

# Seleciona todos os dados da tabela
cursor.execute('SELECT * FROM minha_tabela')

# Recupera todos os resultados da consulta
results = cursor.fetchall()

# Imprime os resultados
for row in results:
    print(row)

# Fecha a conexão
conn.close()