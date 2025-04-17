# import mysql.connector
# from mysql.connector import Error

# def connect_db():
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             port=3306,
#             user="root",
#             password="",
#             database="trisun"
#         )
#         if connection.is_connected():
#             return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None
import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect( host="localhost", username="root", password="Joti@@1705", database="trisun")
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Connection Error: {e}")
        return None


