import mysql.connector
import hashlib
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PORT = os.getenv("MYSQL_PORT")

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )


def initialize_db():
    conn = connect()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        email VARCHAR(255),
        password VARCHAR(256)
    )
    """
    cursor.execute(query)
    conn.close()

def create_user(name, age,email,password):
    conn = connect()
    cursor = conn.cursor()
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hash_password = hash_object.hexdigest()
    query = """
        INSERT INTO users (name, age, email, password) VALUES (
            %s , %s, %s, %s
        )"""
    values = (name,age,email,hash_password)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid
