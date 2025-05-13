import sys
from db_utils import load_all_tables_as_dfs
import sqlite3

if len(sys.argv) != 2:
    print("Usage: python3 main_practice_may11.py <path_to_database>")
    sys.exit(1)

db_path = sys.argv[1]
dfs, conn = load_all_tables_as_dfs(db_path)
cursor = conn.cursor()

with open("table_summary.txt", "w") as f:
    # Loop through each table and print schema + summary
    for table_name, df in dfs.items():
        print("=" * 50, file=f)
        print(f"Schema for table: {table_name}", file=f)

        # Print schema using PRAGMA
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for column in columns:
            print(f"Column: {column[1]}, Type: {column[2]}, Not NULL: {column[3]}, Primary Key: {column[5]}", file=f)
        print("-" * 50, file=f)

        # Pandas summary
        print(f"Number of rows: {len(df)}", file=f)
        print(f"Number of columns: {df.shape[1]}", file=f)
        print(f"Duplicate rows: {df.duplicated().sum()}", file=f)

        print("Column-wise summary:", file=f)
        for col in df.columns:
            print(f"  - {col}:", file=f)
            print(f"      Type: {df[col].dtype}", file=f)
            print(f"      Unique values: {df[col].nunique()}", file=f)
            print(f"      Missing values: {df[col].isna().sum()}", file=f)
            sample_values = df[col].dropna().unique()[:3]
            print(f"      Sample values: {sample_values}", file=f)
        print("=" * 50, file=f)

conn.close()