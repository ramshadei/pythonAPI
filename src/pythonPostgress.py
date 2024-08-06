from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine

# Define your PostgreSQL connection parameters
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = '18.132.73.146'  # Replace with your PostgreSQL server endpoint
USER = 'consultants'  # Replace with your PostgreSQL username
PASSWORD = 'WelcomeItc@2022'  # Replace with your PostgreSQL password
PASSWORD = quote_plus(PASSWORD)
PORT = 5432  # Default PostgreSQL port
DATABASE = 'testdb'  # Replace with your PostgreSQL database name

# Create a SQLAlchemy engine
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')

# Read the CSV file into a DataFrame
csv_file_path = "./customers.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Load the DataFrame into PostgreSQL
table_name = 'customer_Smita'  # Replace with the name of the table you want to create or append to
df.to_sql(table_name, engine, if_exists='replace', index=False)  # Use 'append' if you want to add to an existing table

print(f"Data successfully loaded into {table_name} table.")