import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="arya2008",
        database="hospital_management"
    )
# print("Database connection established successfully.")