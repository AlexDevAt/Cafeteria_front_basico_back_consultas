import mysql.connector



def obtenerConexion():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="cafeteria_db"
)
