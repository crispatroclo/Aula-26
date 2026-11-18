import pandas as pd
import mysql.connector
from mysql.connector import Error

try:
    # Estabelece a conexão
    
    conexao = mysql.connector.connect(
        host = 'localhost', # ou o IP do servidor
        user = 'root',
        password = '',
        database = 'escola' 
    ) 

    if conexao.is_connected():
        print('Conectado com sucesso')

    # cria um cursor (objeto que permite executar comandos SQL)
    cursor = conexao.cursor()

    # Define a query de INSERT usando placeholders (%s)
    #sql = 'INSERT INTO alunos (cpf, matricula, id_curso, nascimento, nome) VALUES (%s, %s, %s, %s, %s)'
    
    # Valores qye serão substituidos nos placeholders, na mesm aordem
    #valores = [
       #('00000000000', 000, 1, '10/10/2000', 'Ana'), 
        #('11111111111', 111, 1, '01/01/2000', 'Bia'), 
        #('22222222222', 222, 2, '02/02/2000', 'Ceu'), 
        #('33333333333', 333, 2, '03/03/2000', 'Dea'), 
        #('44444444444', 444, 3, '04/04/2000', 'Eni'), 
        #('55555555555', 555, 1, '05/05/2000', 'Fia'), 
        #('66666666666', 666, 1, '06/06/2000', 'Gio'), 
        #('77777777777', 777, 2, '07/07/2000', 'Hui'), 
        #('88888888888', 888, 3, '08/08/2000', 'Ina'), 
        #('99999999999', 999, 1, '10/10/2000', 'Jil')
    #]

    # Executa insert no banco, substituindo os %s pelos valores em 'valores'
    # o conector trata automaticamente aspas, datas e acentos
    #cursor.executemany(sql, valores)

    # confirma (grava) as alterações da transação no banco
    # sem commit(), o INSERT ficaria só na memoria e seria descartado
    #conexao.commit()

# confirma (grava) as alterações da transação no banco
    # sem commit(), o INSERT ficaria só na memoria e seria descartado
    # conexao.commit()

    # Mostra o ID (AUTO_INCREMENR) gerado na ultima inserção
    # print(f'Linha inserida. ID gerado: {cursor.lastrowid}')

    # executa uma consulta
    cursor.execute('SELECT * FROM alunos')

    # busca os resultados
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    #df = pd.DataFrame(resultados) # traz o banco sem o nome das colunas
    #df = pd.read_sql('SELECT * FROM alunos LIMIT 5', conexao)
    #df.to_csv("sql.csv", index=False)

    #print(df)


except Error as e:
        print(f'Error ao comectar: {e}')

finally:
    # fecha o cursos (se foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass # se já estiver fechado ou ocorrer erro, ignore

    # fecha conexão (se foi criada e ainda está conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexao encerrada.')