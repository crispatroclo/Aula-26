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

    sql = 'INSERT INTO notas (id_aluno, id_disciplina, nota, data_avaliacao) VALUES (%s, %s, %s, %s)'
    
    valores = [
    # (id_aluno, id_disciplina, nota, data_avaliacao)
    # Informática (alunos 1, 2, 5, 6, 10 | disciplinas 1 e 2)
    (1, 1, 8.5, '2026-06-30'), (1, 2, 9.0, '2026-06-30'),
    (2, 1, 7.0, '2026-06-30'), (2, 2, 6.5, '2026-06-30'),
    (5, 1, 9.5, '2026-06-30'), (5, 2, 8.0, '2026-06-30'),
    (6, 1, 6.0, '2026-06-30'), (6, 2, 7.5, '2026-06-30'),
    (10, 1, 8.0, '2026-06-30'), (10, 2, 8.5, '2026-06-30'),
    # Administração (alunos 3, 8 | disciplinas 3 e 4)
    (3, 3, 7.5, '2026-06-30'), (3, 4, 8.0, '2026-06-30'),
    (8, 3, 6.5, '2026-06-30'), (8, 4, 9.0, '2026-06-30'),
    # Enfermagem (alunos 4, 7, 9 | disciplinas 5 e 6)
    (4, 5, 9.0, '2026-06-30'), (4, 6, 8.5, '2026-06-30'),
    (7, 5, 7.0, '2026-06-30'), (7, 6, 6.0, '2026-06-30'),
    (9, 5, 8.5, '2026-06-30'), (9, 6, 9.5, '2026-06-30'),
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