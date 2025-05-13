import sqlite3
import pandas as pd

def load_all_tables_as_dfs(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    dfs = {}
    for table in tables:
        table_name = table[0]
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        dfs[table_name] = df

    return dfs, conn  # return both the data and the connection
