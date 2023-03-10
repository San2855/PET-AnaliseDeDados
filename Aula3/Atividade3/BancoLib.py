import random
import mysql.connector

con = mysql.connector.connect(user='sql10591880',
                              password='Uj8canyVDM',
                              host='sql10.freemysqlhosting.net',
                              port=3306,
                              database='sql10591880')

cursor = con.cursor()

class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.con = con
        self.cursor = self.con.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS CONTAS (NUM INT, SALDO REAL)''')
        self.con.commit()
        
    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        self.cursor.execute(f"INSERT INTO CONTAS (NUM, SALDO) VALUES ({num}, 0)")
        self.con.commit()
        return num

    def consultaSaldo(self, numConta):
        self.cursor.execute(f"SELECT SALDO FROM CONTAS WHERE NUM = {numConta}")
        saldo = self.cursor.fetchone()
        if saldo:
            return saldo[0]
        else:
            return -1

    def depositar(self, numConta, valor):
        self.cursor.execute(f"UPDATE CONTAS SET SALDO = SALDO + {valor} WHERE NUM = {numConta}")
        self.con.commit()

    def sacar(self, numConta, valor):
        self.cursor.execute(f"SELECT SALDO FROM CONTAS WHERE NUM = {numConta}")
        saldo = self.cursor.fetchone()
        if saldo and saldo[0] >= valor:
            self.cursor.execute(f"UPDATE CONTAS SET SALDO = SALDO - {valor} WHERE NUM = {numConta}")
            self.con.commit()
            return True
        else:
            return False
    
    def closeConnection(self):
        self.con.close()