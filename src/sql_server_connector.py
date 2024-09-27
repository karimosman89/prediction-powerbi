import pyodbc
import pandas as pd

def connect_sql_server(server, database, username, password):
    """Connect to SQL Server or Azure SQL Database."""
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    return conn

def run_sql_query(conn, query):
    """Run an SQL query on the database."""
    df = pd.read_sql(query, conn)
    return df

def load_data_to_sql(conn, table_name, data):
    """Load a DataFrame into SQL Server table."""
    cursor = conn.cursor()

    for index, row in data.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name} VALUES ({','.join(['?' for _ in row])})", tuple(row))

    conn.commit()
    cursor.close()
    print(f"Loaded {len(data)} rows into {table_name}")
