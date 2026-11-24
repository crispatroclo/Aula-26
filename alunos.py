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

    sql = 'INSERT INTO alunos (nome, cpf, data_nascimento, email, telefone, data_matricula, id_curso) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    
    valores = [
    ('Ana Souza',      '11122233344', '2005-03-14', 'ana@email.com',     '21999990001', '2026-02-01', 1),  # id 1
    ('Bruno Lima',     '22233344455', '2004-07-22', 'bruno@email.com',   '21999990002', '2026-02-01', 1),  # id 2
    ('Carla Mendes',   '33344455566', '2003-11-05', 'carla@email.com',   '21999990003', '2026-02-03', 2),  # id 3
    ('Diego Ferreira', '44455566677', '2006-01-30', 'diego@email.com',   '21999990004', '2026-02-05', 3),  # id 4
    ('Joana Ribeiro',  '55566677788', '2005-04-21', 'joana@email.com',   '21999990005', '2026-02-07', 1),  # id 5
    ('Lucas Martins',  '66677788899', '2004-09-10', 'lucas@email.com',   '21999990006', '2026-02-07', 1),  # id 6
    ('Mariana Costa',  '77788899900', '2003-12-02', 'mariana@email.com', '21999990007', '2026-02-10', 3),  # id 7
    ('Pedro Alves',    '88899900011', '2006-06-18', 'pedro@email.com',   '21999990008', '2026-02-10', 2),  # id 8
    ('Rafaela Nunes',  '99900011122', '2005-08-25', 'rafaela@email.com', '21999990009', '2026-02-12', 3),  # id 9
    ('Thiago Rocha',   '10120230344', '2004-02-14', 'thiago@email.com',  '21999990010', '2026-02-12', 1),  # id 10
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