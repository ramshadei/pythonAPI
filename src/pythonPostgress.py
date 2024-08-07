from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine
import os

# Define your PostgreSQL connection parameters
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = os.getenv('DB_ENDPOINT')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
PASSWORD = quote_plus(PASSWORD)
PORT = os.getenv('DB_PORT')
DATABASE = os.getenv('DB_NAME')

# Create a SQLAlchemy engine
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')

# Read the CSV file into a DataFrame
csv_file_path = '../customers.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Load the DataFrame into PostgreSQL
table_name = 'customer_Muyiwa'  # Replace with the name of the table you want to create or append to
df.to_sql(table_name, engine, if_exists='replace', index=False)  # Use 'append' if you want to add to an existing table

print(f"Data successfully loaded into {table_name} table.")
