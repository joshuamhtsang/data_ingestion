import psycopg2 as pg2
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


def insert_person_table_query(id, role, first_name, middle_name, last_name,
                              nationality):
    query = """
    INSERT INTO public.person(
        id, role, first_name, middle_name, last_name, nationality)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
    """ % (id, role, first_name, middle_name, last_name, nationality)
    print(query)
    return query


def get_data_person_table_query():
    query = """
    SELECT ps.first_name, ps.middle_name, ps.last_name, ps.role
    FROM public.person as ps
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

    try:
        cur.execute(create_person_table_query())
    except pg2.errors.DuplicateTable as e:
        print(e)
        print("Table already exists! Executing rollback...")
        cur.execute("ROLLBACK")

    try:
        cur.execute(
            insert_person_table_query(
                'fc909512-499e-428d-8fc1-09330b26f4c5',
                'player',
                'Stephen',
                'Assassin',
                'Curry',
                'US'
            )
        )
    except pg2.errors.UniqueViolation as e:
        print(e)
        cur.execute("ROLLBACK")

    try:
        cur.execute(get_data_person_table_query())
        persons = cur.fetchmany(2)
        print(persons)
    except Exception as e:
        print(e)
        cur.execute("ROLLBACK")

    conn.commit()

    cur.close()
    conn.close()
