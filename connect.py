import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='cliente',user='root',password='123456')
    consulta_sql = "SELECT * FROM cliente"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Numero de registros: ", cursor.rowcount)
    print('\n')
    for linha in linhas:
        print("Id = ",linha[0])
        print("Nome = ", linha[1])
        print("CPF = ",linha[2])
        print('\n')
except:
    Print("Um erro ocorreu")
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")
