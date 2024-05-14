import psycopg2
import json
from lib.sql_helper import readsqlfile
def insert_data(conn, data: list, table: str):
    try:
        cursor = conn.cursor()
        
        # Iterate over each item in the list
        for item in data:
            columns = ', '.join(item.keys())
            placeholders = ', '.join(['%s'] * len(item))
            values = tuple(item.values())
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, values)

        conn.commit()
        print(f"{table}Data inserted successfully")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()


def create_table(conn, sql_file_name: str,table_name:str):

    cur = conn.cursor()

    # Check if the table exists
    cur.execute(f"SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename = '{table_name}');")
    exists = cur.fetchone()[0]

    if not exists:
        # Table does not exist, create new table
        sqltxt = readsqlfile(sql_file_name)
        cur.execute(sqltxt)
        conn.commit()
        print(f"{table_name} table created successfully.")
    else:
        # Table exists
        print(f"{table_name} table already exists.")
        
def update_table(conn,connection_params, table, data, update_column, condition_column):
    """Update a table based on the provided data and column specifications."""
    cursor = conn.cursor()
    try:
        # Generate the SQL statement dynamically based on the input
        sql = f"UPDATE {table} SET {update_column} = %s WHERE {condition_column} = %s;"
        # Values to be updated
        update_value = data[update_column.split('=')[0].strip()]
        condition_value = data[condition_column]
        # Execute the update statement
        cursor.execute(sql, (update_value, condition_value))
        conn.commit()
        print("Database has been updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()