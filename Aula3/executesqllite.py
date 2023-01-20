import sqlite3

con = sqlite3.connect("BancoDeDados.db")

#CRIO A TABELA
cursor = con.cursor()
cursor.execute('''DROP TABLE ALUNO''')
con.commit()
#DEFINO DADOS
cursor.execute('''CREATE TABLE ALUNO(MATRICULA INTEGER, CPF INT, NOME VARVCHAR(20))''')

#INSIRO DADOS
cursor.execute("INSERT INTO ALUNO VALUES(10, 1, 'Neto')")

cursor.execute("INSERT INTO ALUNO VALUES(20, 2, 'Waldemar')")
cursor.execute("INSERT INTO ALUNO(MATRICULA, NOME) VALUES(11, 'Pires')")
con.commit()

#DELETO DADOS
cursor.execute("DELETE FROM ALUNO WHERE MATRICULA = 11")
con.commit()

#CONSULTO DADOS
cursor.execute("SELECT NOME FROM ALUNO")
result = cursor.fetchall()
for a in result:
  print(a)


cursor.close()
con.close()

