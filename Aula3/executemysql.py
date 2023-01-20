import mysql.connector

# Cria uma conexão com o banco de dados
cnx = mysql.connector.connect(user='sql10591880',
                              password='Uj8canyVDM',
                              host='sql10.freemysqlhosting.net',
                              port=3306,
                              database='sql10591880')

# Cria um cursor para executar consultas
cursor = cnx.cursor()

# Executa uma consulta para recuperar dados de uma tabela
cursor.execute("SELECT CURDATE()")

# Recupera todos os resultados da consulta
result = cursor.fetchone()

# Imprime os resultados
print(result)

# Fecha a conexão
cnx.close()