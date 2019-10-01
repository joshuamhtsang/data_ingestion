from psycopg2 import connect
from faker import Faker


def create_person_table_query():
    query = """
    CREATE TABLE public.person
    (
        id uuid NOT NULL,
        role text,
        first_name text,
        middle_name text,
        last_name text,
        nationality text,
        PRIMARY KEY (id)
    )
    WITH (
        OIDS = FALSE
    )
    TABLESPACE pg_default;
    
    ALTER TABLE public.person
        OWNER to admin;
    """

    return query


if __name__ == '__main__':
    print("Inject data into PostgreSQL")

    conn = connect(
        host="localhost",
        port="5432",
        dbname="nba",
        user="admin",
        password="admin"
    )
    cur = conn.cursor()

    cur.execute(create_person_table_query())

    conn.commit()

    cur.close()
    conn.close()
