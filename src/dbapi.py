from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, jsonify
import os

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5300, debug=True)