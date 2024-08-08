from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

app = Flask(__name__)

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

# Specify the table name you want to read from
table_name = 'customer_Muyiwa'  # Replace with your table name


@app.route('/data', methods=['GET'])
def get_data():
    # Read data from the PostgreSQL table into a DataFrame
    df = pd.read_sql_table(table_name, engine)

    # Convert the DataFrame to a dictionary and then to JSON
    data = df.to_dict(orient='records')

    # Return the data as JSON
    return jsonify(data)


@app.route('/data', methods=['POST'])
def add_data():
    try:
        # Get the JSON data from the request
        new_data = request.get_json()

        # Convert the JSON data to a DataFrame
        df = pd.DataFrame([new_data])

        # Insert the DataFrame into the PostgreSQL table
        df.to_sql(table_name, engine, if_exists='append', index=False)

        return jsonify({"message": "Data added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5310, debug=True)
