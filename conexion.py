import pyodbc

server = 'PAVILON-ADRIAN\SQLSERVER2016'
db = 'appClima'
usuario  = 'jarma'
contraseña = '123456'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+db+';UID='+usuario+'PWD='+contraseña)
    print('yei')

except:
    print('no')