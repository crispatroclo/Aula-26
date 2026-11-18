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

    sql = 'INSERT INTO notas (nota, data_avaliacao, id_aluno, id_disciplina) VALUES (%s, %s, %s, %s)'
    
    valores = [
        (10, 2026-11-10, 1, 13),
        (10, 2026-11-10, 2, 15),
        (10, 2026-11-10, 3, 14),
    ]

    cursor.executemany(sql, valores)

    conexao.commit()

    cursor.execute('SELECT * FROM notas')

    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    df = pd.DataFrame(resultados) # traz o banco sem o nome das colunas
    df = pd.read_sql('SELECT * FROM notas', conexao)
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