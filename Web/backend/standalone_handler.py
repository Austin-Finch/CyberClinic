from app.models import user
import psycopg2
import os
from dotenv import load_dotenv
import socket



if __name__ == '__main__':
    load_dotenv()
    
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port
    )
