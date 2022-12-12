# Conexão com o banco de dados.
import pyodbc


server = 'pc-gamer' 
database = 'BancoEstudos' 
username = 'sa' 
password = 'bandal' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()


