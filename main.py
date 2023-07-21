import psycopg2

from config import config


def connect():
    """establishes a connection to the PostgreSQL database using the retrieved parameters."""
    try:
        connection = None
        params = config()
        print("Connecting to the database...")
        connection = psycopg2.connect(**params)
        # Create a connection
        csr = connection.cursor()
        print("PostgreSQL Version")
        csr.execute('SELECT version()')
        db_version = csr.fetchone()
        print(db_version)
        csr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated!")


if __name__ == "__main__":
    connect()
