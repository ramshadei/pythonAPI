from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, jsonify
import os

app = Flask(__name__)
# Define your PostgreSQL connection parameters
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = os.environ['ENDPOINT']  # os.getenv('ENDPOINT')
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
PASSWORD = quote_plus(str(PASSWORD))
PORT = os.environ['PORT']
DATABASE = os.environ['DATABASE']

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
    app.run(host='0.0.0.0', port=5000, debug=True)
