import pandas as pd
import sqlite3
from scipy import stats


# Abre o arquivo CSV
with open('Teste\Dados_PET\ITM-22-111-Am-08-CBI22-077-POLARIZACAO_CV-_Final-05-01-23_.csv', 'r') as arquivo_csv:
    # Lê o arquivo CSV
    leitor_csv = pd.read_csv(arquivo_csv, sep=',', on_bad_lines='skip', low_memory=False)
    leitor_csv['Current'] = pd.to_numeric(leitor_csv['Current'], errors='coerce')
    leitor_csv['Voltage'] = pd.to_numeric(leitor_csv['Voltage'], errors='coerce')
    leitor_csv['Step'] = pd.to_numeric(leitor_csv['Step'], errors='coerce')
    leitor_csv['AhCha'] = pd.to_numeric(leitor_csv['AhCha'], errors='coerce')
    leitor_csv['AhDch'] = pd.to_numeric(leitor_csv['AhDch'], errors='coerce')
    leitor_csv['AhStep'] = pd.to_numeric(leitor_csv['AhStep'], errors='coerce')
    leitor_csv['AhAccu'] = pd.to_numeric(leitor_csv['AhAccu'], errors='coerce')
    leitor_csv['WhAccu'] = pd.to_numeric(leitor_csv['WhAccu'], errors='coerce')
    leitor_csv['WhCha'] = pd.to_numeric(leitor_csv['WhCha'], errors='coerce')
    leitor_csv['WhDch'] = pd.to_numeric(leitor_csv['WhDch'], errors='coerce')
    leitor_csv['WhStep'] = pd.to_numeric(leitor_csv['WhStep'], errors='coerce')
    leitor_csv = leitor_csv.fillna(0)
    p = leitor_csv.groupby('Step').last()
 
    

    # Conecta ao banco de dados SQLite3
    conexao = sqlite3.connect('POLARIZACAO.db')

    # Cria uma tabela chamada "dados"
    conexao.execute('''CREATE TABLE IF NOT EXISTS dados
                     (Time_Stamp TEXT, Step TEXT, Status TEXT, Prog_Time TEXT, Step_Time TEXT, Cycle TEXT, Cycle_Level TEXT, Procedure TEXT, Voltage REAL, Current REAL, AhCha REAL, AhDch REAL, AhStep TEXT, AhAccu REAL, WhAccu REAL, WhCha REAL, WhDch REAL, WhStep TEXT)''')

    # Insere as informações do arquivo CSV na tabela "dados"
    for linha in leitor_csv.itertuples(index=False):
        Time_Stamp = linha[2]
        Step = linha[3]
        Status = linha[4]
        Prog_Time = linha[5]
        Step_Time = linha[6]
        Cycle = linha[7]
        Cycle_Level = linha[8]
        Procedure = linha[9]
        Voltage = linha[10]
        Current = linha[11]
        AhCha = linha[12]
        AhDch = linha[13]
        AhStep = linha[14]
        AhAccu = linha[15]
        WhAccu = linha[16]
        WhCha = linha[17]
        WhDch = linha[18]
        WhStep = linha[19]
        
        
        

        # Insere os valores na tabela "dados"
        conexao.execute("INSERT INTO dados (Time_Stamp, Step, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (Time_Stamp, Step, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep))
        
    # Salva as alterações no banco de dados
    conexao.commit()
    
    # Fecha a conexão com o banco de dados
    conexao.close()
    
    # Conecta ao banco de dados SQLite3
    conexao = sqlite3.connect('Step_Polarização.db')

    # Cria uma tabela chamada "rel"
    conexao.execute('''CREATE TABLE IF NOT EXISTS rel
                     (Time_Stamp TEXT, Status TEXT, Prog_Time TEXT, Step_Time TEXT, Cycle TEXT, Cycle_Level TEXT, Procedure TEXT, Voltage REAL, Current REAL, AhCha REAL, AhDch REAL, AhStep TEXT, AhAccu REAL, WhAccu REAL, WhCha REAL, WhDch REAL, WhStep TEXT)''')

    # Insere as informações do conjunto CSV na tabela "rel"
    for linha in p.itertuples(index=False):
        Time_Stamp = linha[2]
        Status = linha[3]
        Prog_Time = linha[4]
        Step_Time = linha[5]
        Cycle = linha[6]
        Cycle_Level = linha[7]
        Procedure = linha[8]
        Voltage = linha[9]
        Current = linha[10]
        AhCha = linha[11]
        AhDch = linha[12]
        AhStep = linha[13]
        AhAccu = linha[14]
        WhAccu = linha[15]
        WhCha = linha[16]
        WhDch = linha[17]
        WhStep = linha[18]
        
        
        

        # Insere os valores na tabela "rel"
        conexao.execute("INSERT INTO rel (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep))
        
    # Salva as alterações no banco de dados
    conexao.commit()
    # Deleta os dados indesejaveis
    conexao.execute("DELETE FROM rel WHERE Voltage = 0;")
    conexao.execute("DELETE FROM rel WHERE ROWID = 14;")
    conexao.execute("DELETE FROM rel WHERE ROWID = 15;")

    # Salve as alterações no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()
   