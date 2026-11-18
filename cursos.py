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

    sql = 'INSERT INTO cursos (id_curso, nome_curso, carga_horaria, turno) VALUES (%s, %s, %s, %s)'
    
    valores = [
        (1, 'Administração', 1000, 'noite'), 
        (2, 'Enfermagem', 1200, 'tarde'), 
        (3, 'Informática', 800, 'manhã'), 
    ]

    cursor.executemany(sql, valores)

    conexao.commit()

    cursor.execute('SELECT * FROM cursos')

    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    df = pd.DataFrame(resultados) # traz o banco sem o nome das colunas
    df = pd.read_sql('SELECT * FROM cursos', conexao)
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