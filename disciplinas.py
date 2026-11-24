import pandas as pd
import mysql.connector
from mysql.connector import Error

try:
    
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'escola' 
    ) 

    if conexao.is_connected():
        print('Conectado com sucesso')

    cursor = conexao.cursor()

    sql = 'INSERT INTO disciplinas (nome_disciplina, carga_horaria, id_curso) VALUES (%s, %s, %s)'
    
    valores =  [
    # (nome_disciplina, carga_horaria, id_curso)
    ('Lógica de Programação', 80, 1),  # id 1
    ('Banco de Dados',        60, 1),  # id 2
    ('Gestão Financeira',     60, 2),  # id 3
    ('Marketing',             40, 2),  # id 4
    ('Anatomia',              80, 3),  # id 5
    ('Farmacologia',          60, 3),  # id 6
]

    cursor.executemany(sql, valores)

    conexao.commit()

    cursor.execute('SELECT * FROM disciplinas')

    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    df = pd.DataFrame(resultados) # traz o banco sem o nome das colunas
    df = pd.read_sql('SELECT * FROM disciplinas', conexao)
    df.to_csv("sql.csv", index=False)

    print(df)


except Error as e:
        print(f'Error ao comectar: {e}')

finally:
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass 
   
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexao encerrada.')