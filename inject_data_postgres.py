from psycopg2 import connect
from faker import Faker

if __name__ == '__main__':
    print("Inject data into PostgreSQL")

    conn = connect(
        host="localhost",
        port="5432",
        dbname="nba",
        user="admin",
        password="admin"
    )
