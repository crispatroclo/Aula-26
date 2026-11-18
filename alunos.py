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

    sql = 'INSERT INTO alunos (cpf, matricula, id_curso, data_nascimento, nome) VALUES (%s, %s, %s, %s, %s)'
    
    valores = [
        ('00000000000', 000, 1, '10/10/2000', 'Ana'), 
        ('11111111111', 111, 1, '01/01/2000', 'Bia'), 
        ('22222222222', 222, 2, '02/02/2000', 'Ceu'), 
        ('33333333333', 333, 2, '03/03/2000', 'Dea'), 
        ('44444444444', 444, 3, '04/04/2000', 'Eni'), 
        ('55555555555', 555, 1, '05/05/2000', 'Fia'), 
        ('66666666666', 666, 1, '06/06/2000', 'Gio'), 
        ('77777777777', 777, 2, '07/07/2000', 'Hui'), 
        ('88888888888', 888, 3, '08/08/2000', 'Ina'), 
        ('99999999999', 999, 1, '10/10/2000', 'Jil')
    ]

    cursor.executemany(sql, valores)

    conexao.commit()

    cursor.execute('SELECT * FROM alunos')

    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    df = pd.DataFrame(resultados) # traz o banco sem o nome das colunas
    df = pd.read_sql('SELECT * FROM alunos', conexao)
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