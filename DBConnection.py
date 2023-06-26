import pyodbc
import config

connection_bd = pyodbc.connect(config.bd_connection_info)
cursor = connection_bd.cursor()