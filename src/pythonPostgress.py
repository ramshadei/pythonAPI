from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function to get environment variables with error handling
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Environment variable {var_name} not set.")
    return value


# Define your PostgreSQL connection parameters
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = get_env_variable('ENDPOINT')
USER = get_env_variable('USER')
PASSWORD = get_env_variable('PASSWORD')
PASSWORD = quote_plus(PASSWORD)  # Ensure PASSWORD is a string before quoting
PORT = get_env_variable('PORT')
DATABASE = get_env_variable('DATABASE')

# Create a SQLAlchemy engine
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')

# Construct the absolute path to the CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, '../data/customers.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Load the DataFrame into PostgreSQL
table_name = 'customer_Muyiwa'  # Replace with the name of the table you want to create or append to
df.to_sql(table_name, engine, if_exists='replace', index=False)  # Use 'append' if you want to add to an existing table

print(f"Data successfully loaded into {table_name} table.")
