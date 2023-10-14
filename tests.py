import pyodbc

SERVER = 'localhost'
DATABASE = 'AdventureWorks12'
USERNAME = 'sa'
PASSWORD = 'reallyStrongPwd123'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)


