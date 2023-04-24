import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

####################################################################################################
# Abre o arquivo CSV
with open('Dados\ITM-22-111-Am-08-CBI22-077-POLARIZACAO_CV-_Final-05-01-23_.csv', 'r') as arquivo_csv:
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
    conexao = sqlite3.connect('Polarização_AM08.db')

    # Cria uma tabela chamada "am08"
    conexao.execute('''CREATE TABLE IF NOT EXISTS am08
                     (Time_Stamp TEXT, Status TEXT, Prog_Time TEXT, Step_Time TEXT, Cycle TEXT, Cycle_Level TEXT, Procedure TEXT, Voltage REAL, Current REAL, AhCha REAL, AhDch REAL, AhStep TEXT, AhAccu REAL, WhAccu REAL, WhCha REAL, WhDch REAL, WhStep TEXT)''')

    # Insere as informações do conjunto CSV na tabela "am08"
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
        
        
        

        # Insere os valores na tabela "am08"
        conexao.execute("INSERT INTO am08 (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep))
        
    # Salva as alterações no banco de dados
    conexao.commit()
    # Deleta os dados indesejaveis
    conexao.execute("DELETE FROM am08 WHERE Voltage = 0;")
    conexao.execute("DELETE FROM am08 WHERE ROWID = 14;")
    conexao.execute("DELETE FROM am08 WHERE ROWID = 15;")
    
    

    # Salve as alterações no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()
####################################################################################################
# Abre o arquivo CSV
with open('Dados\ITM-22-111-Am-07-CBI22-077-POLARIZACAO_CV-_Final-05-01-23_.csv', 'r') as arquivo_csv:
    # Lê o arquivo CSV
    leitor_am07 = pd.read_csv(arquivo_csv, sep=',', on_bad_lines='skip', low_memory=False)
    leitor_am07['Current'] = pd.to_numeric(leitor_am07['Current'], errors='coerce')
    leitor_am07['Voltage'] = pd.to_numeric(leitor_am07['Voltage'], errors='coerce')
    leitor_am07['Step'] = pd.to_numeric(leitor_am07['Step'], errors='coerce')
    leitor_am07['AhCha'] = pd.to_numeric(leitor_am07['AhCha'], errors='coerce')
    leitor_am07['AhDch'] = pd.to_numeric(leitor_am07['AhDch'], errors='coerce')
    leitor_am07['AhStep'] = pd.to_numeric(leitor_am07['AhStep'], errors='coerce')
    leitor_am07['AhAccu'] = pd.to_numeric(leitor_am07['AhAccu'], errors='coerce')
    leitor_am07['WhAccu'] = pd.to_numeric(leitor_am07['WhAccu'], errors='coerce')
    leitor_am07['WhCha'] = pd.to_numeric(leitor_am07['WhCha'], errors='coerce')
    leitor_am07['WhDch'] = pd.to_numeric(leitor_am07['WhDch'], errors='coerce')
    leitor_am07['WhStep'] = pd.to_numeric(leitor_am07['WhStep'], errors='coerce')
    leitor_am07 = leitor_am07.fillna(0)
    t =leitor_am07.groupby('Step').last()
 
    # Conecta ao banco de dados SQLite3
    conexao = sqlite3.connect('Polarização_AM07.db')

    # Cria uma tabela chamada "am07"
    conexao.execute('''CREATE TABLE IF NOT EXISTS am07
                     (Time_Stamp TEXT, Status TEXT, Prog_Time TEXT, Step_Time TEXT, Cycle TEXT, Cycle_Level TEXT, Procedure TEXT, Voltage REAL, Current REAL, AhCha REAL, AhDch REAL, AhStep TEXT, AhAccu REAL, WhAccu REAL, WhCha REAL, WhDch REAL, WhStep TEXT)''')

    # Insere as informações do conjunto CSV na tabela "am07"
    for linha in t.itertuples(index=False):
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
        
        
        

        # Insere os valores na tabela "am07"
        conexao.execute("INSERT INTO am07 (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep))
        
    # Salva as alterações no banco de dados
    conexao.commit()
    
    # Deleta os dados indesejaveis
    conexao.execute("DELETE FROM am07 WHERE Voltage = 0;")
    conexao.execute("DELETE FROM am07 WHERE ROWID = 14;")
    conexao.execute("DELETE FROM am07 WHERE ROWID = 15;")
    

    # Salve as alterações no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()
   #################################################################################################
# Abre o arquivo CSV
with open('Dados\ITM-22-111-Am-03-CBI22-076-POLARIZACAO_CV-_Final-05-01-23_.csv', 'r') as arquivo_csv:
    # Lê o arquivo CSV
    leitor_am03 = pd.read_csv(arquivo_csv, sep=',', on_bad_lines='skip', low_memory=False)
    leitor_am03['Current'] = pd.to_numeric(leitor_am03['Current'], errors='coerce')
    leitor_am03['Voltage'] = pd.to_numeric(leitor_am03['Voltage'], errors='coerce')
    leitor_am03['Step'] = pd.to_numeric(leitor_am03['Step'], errors='coerce')
    leitor_am03['AhCha'] = pd.to_numeric(leitor_am03['AhCha'], errors='coerce')
    leitor_am03['AhDch'] = pd.to_numeric(leitor_am03['AhDch'], errors='coerce')
    leitor_am03['AhStep'] = pd.to_numeric(leitor_am03['AhStep'], errors='coerce')
    leitor_am03['AhAccu'] = pd.to_numeric(leitor_am03['AhAccu'], errors='coerce')
    leitor_am03['WhAccu'] = pd.to_numeric(leitor_am03['WhAccu'], errors='coerce')
    leitor_am03['WhCha'] = pd.to_numeric(leitor_am03['WhCha'], errors='coerce')
    leitor_am03['WhDch'] = pd.to_numeric(leitor_am03['WhDch'], errors='coerce')
    leitor_am03['WhStep'] = pd.to_numeric(leitor_am03['WhStep'], errors='coerce')
    leitor_am03 = leitor_am03.fillna(0)
    z =leitor_am03.groupby('Step').last()
 
    # Conecta ao banco de dados SQLite3
    conexao = sqlite3.connect('Polarização_AM03.db')

    # Cria uma tabela chamada "am03"
    conexao.execute('''CREATE TABLE IF NOT EXISTS am03
                     (Time_Stamp TEXT, Status TEXT, Prog_Time TEXT, Step_Time TEXT, Cycle TEXT, Cycle_Level TEXT, Procedure TEXT, Voltage REAL, Current REAL, AhCha REAL, AhDch REAL, AhStep TEXT, AhAccu REAL, WhAccu REAL, WhCha REAL, WhDch REAL, WhStep TEXT)''')

    # Insere as informações do conjunto CSV na tabela "am03"
    for linha in z.itertuples(index=False):
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
        
        
        

        # Insere os valores na tabela "am03"
        conexao.execute("INSERT INTO am03 (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep))
        
    # Salva as alterações no banco de dados
    conexao.commit()
    
    # Deleta os dados indesejaveis
    conexao.execute("DELETE FROM am03 WHERE Voltage = 0;")
    conexao.execute("DELETE FROM am03 WHERE ROWID = 14;")
    conexao.execute("DELETE FROM am03 WHERE ROWID = 15;")
    
    

    # Salve as alterações no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()
    ################################################################################################
    with open('Dados\ITM-22-111-Am-04-CBI22-076-POLARIZACAO_CV-_Final-05-01-23_.csv', 'r') as arquivo_csv:
    # Lê o arquivo CSV
        leitor_am04 = pd.read_csv(arquivo_csv, sep=',', on_bad_lines='skip', low_memory=False)
        leitor_am04['Current'] = pd.to_numeric(leitor_am04['Current'], errors='coerce')
        leitor_am04['Voltage'] = pd.to_numeric(leitor_am04['Voltage'], errors='coerce')
        leitor_am04['Step'] = pd.to_numeric(leitor_am04['Step'], errors='coerce')
        leitor_am04['AhCha'] = pd.to_numeric(leitor_am04['AhCha'], errors='coerce')
        leitor_am04['AhDch'] = pd.to_numeric(leitor_am04['AhDch'], errors='coerce')
        leitor_am04['AhStep'] = pd.to_numeric(leitor_am04['AhStep'], errors='coerce')
        leitor_am04['AhAccu'] = pd.to_numeric(leitor_am04['AhAccu'], errors='coerce')
        leitor_am04['WhAccu'] = pd.to_numeric(leitor_am04['WhAccu'], errors='coerce')
        leitor_am04['WhCha'] = pd.to_numeric(leitor_am04['WhCha'], errors='coerce')
        leitor_am04['WhDch'] = pd.to_numeric(leitor_am04['WhDch'], errors='coerce')
        leitor_am04['WhStep'] = pd.to_numeric(leitor_am04['WhStep'], errors='coerce')
        leitor_am04 = leitor_am04.fillna(0)
        b =leitor_am04.groupby('Step').last()
 
    # Conecta ao banco de dados SQLite3
    conexao = sqlite3.connect('Polarização_AM04.db')

    # Cria uma tabela chamada "am04"
    conexao.execute('''CREATE TABLE IF NOT EXISTS am04
                     (Time_Stamp TEXT, Status TEXT, Prog_Time TEXT, Step_Time TEXT, Cycle TEXT, Cycle_Level TEXT, Procedure TEXT, Voltage REAL, Current REAL, AhCha REAL, AhDch REAL, AhStep TEXT, AhAccu REAL, WhAccu REAL, WhCha REAL, WhDch REAL, WhStep TEXT)''')

    # Insere as informações do conjunto CSV na tabela "am04"
    for linha in b.itertuples(index=False):
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
        
        
        

        # Insere os valores na tabela "am04"
        conexao.execute("INSERT INTO am04 (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (Time_Stamp, Status, Prog_Time, Step_Time, Cycle, Cycle_Level, Procedure, Voltage, Current, AhCha, AhDch, AhStep, AhAccu, WhAccu, WhCha, WhDch, WhStep))
        
    # Salva as alterações no banco de dados
    conexao.commit()
    
    # Deleta os dados indesejaveis
    conexao.execute("DELETE FROM am04 WHERE Voltage = 0;")
    conexao.execute("DELETE FROM am04 WHERE ROWID = 14;")
    conexao.execute("DELETE FROM am04 WHERE ROWID = 15;")
    

    # Salve as alterações no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()
    ################################################################################################
corrente_78 = [(p['Current'][i] + t['Current'][i])/2 for i in range(2, 13)]
tensao_78 = [(p['Voltage'][i] + t['Voltage'][i])/2 for i in range(2, 13)]
corrente_34 = [(b['Current'][i] + z['Current'][i])/2 for i in range(2, 13)]
tensao_34 = [(z['Voltage'][i] + b['Voltage'][i])/2 for i in range(2, 13)]

df = pd.DataFrame({'Média-de-Tensão-CBI22-077': tensao_78,
                   'Média-de-Corrente-CBI22-077': corrente_78,
                   'Média-de-Tensão-CBI22-076': tensao_34,
                   'Média-de-Corrente-CBI22-076': corrente_34})

# Conectar ao banco de dados
conexao = sqlite3.connect('medias.db')

# Criar uma tabela
conexao.execute('''CREATE TABLE medias
             (id INTEGER PRIMARY KEY,
             Media_tensaoCBI22_077 REAL,
             Media_correnteCBI22_077 REAL,
             Media_tensaoCBI22_076 REAL,
             Media_correnteCBI22_076 REAL);''')

# Inserir os dados
for i in range(2, 13):
    Media_tensaoCBI22_077 = (p['Voltage'][i] + t['Voltage'][i])/2
    Media_correnteCBI22_077 = (p['Current'][i] + t['Current'][i])/2
    Media_tensaoCBI22_076 = (b['Voltage'][i] + z['Voltage'][i])/2
    Media_correnteCBI22_076 = (b['Current'][i] + z['Current'][i])/2
    conexao.execute("INSERT INTO medias (id, Media_tensaoCBI22_077, Media_correnteCBI22_077, Media_tensaoCBI22_076, Media_correnteCBI22_076) VALUES (?, ?, ?, ?, ?)", (i-2, Media_tensaoCBI22_077, Media_correnteCBI22_077, Media_tensaoCBI22_076, Media_correnteCBI22_076))

# Salvar as alterações
conexao.commit()

# Fechar a conexão
conexao.close()

# Crie um gráfico de dispersão
plt.plot(df['Média-de-Tensão-CBI22-077'], df['Média-de-Corrente-CBI22-077'], 'o', label='CBI22-077')
plt.plot(df['Média-de-Tensão-CBI22-076'], df['Média-de-Corrente-CBI22-076'], 'o', label='CBI22-076')

# Adicione rótulos de eixo e título
plt.xlabel('Tensão (V)')
plt.ylabel('Corrente (A)')
plt.title('POLARIZAÇÃO CV')

# Adicione uma legenda
plt.legend()
plt.grid()

# Exiba o gráfico
plt.show()
