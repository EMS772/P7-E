# src/app.py
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos desde variables de entorno
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "test_db")

@app.route('/')
def hello_world():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hola mundo soy Julio cesar Desde my SQL con docker' ")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0]
    except Exception as e:
        return f"Error connecting to database: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
