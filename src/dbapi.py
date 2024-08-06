from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, jsonify

app = Flask(__name__)
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

# Specify the table name you want to read from
table_name = 'customer_Priya'  # Replace with your table name

@app.route('/data', methods=['GET'])
def get_data():
    # Read data from the PostgreSQL table into a DataFrame
    df = pd.read_sql_table(table_name, engine)

    # Convert the DataFrame to a dictionary and then to JSON
    data = df.to_dict(orient='records')

    # Return the data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)