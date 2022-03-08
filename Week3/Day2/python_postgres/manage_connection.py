from psycopg import OperationalError, connect
import os


def create_connection():
    try:
        # I am going to create a connection object that will handle all my queries to the database
        conn = connect(
            # host="database-1.cuzywhpjucyb.us-east-1.rds.amazonaws.com",
            # dbname="postgres",
            # user="postgres",
            # password="password goes here",
            # port="5432"
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        print(e)


connection = create_connection()

print(connection)
