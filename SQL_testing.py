query = """SET sql_mode = 'ONLY_FULL_GROUP_BY';"""


import pandas as pd
from sqlalchemy import create_engine, text
import os 
from dotenv import load_dotenv

load_dotenv()

# Example for MySQL
SQL_URL = os.getenv('MYSQL_URL')
engine = create_engine(SQL_URL)
connection = engine.connect()


result = connection.execute(text(query))

#  # Fetch all rows from the result
# rows = result.fetchall()



# print(rows)
