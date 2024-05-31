import pandas as pd
from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv

load_dotenv()

# Load the JSON file into a DataFrame
df = pd.read_json('./preprocessing/data.json')

# Display the first few rows of the DataFrame
print(df.head())

# Define your database connection string
# Replace with your actual database connection string
# Example for SQLite
# engine = create_engine('sqlite:///my_database.db')

# Example for PostgreSQL
# engine = create_engine('postgresql://username:password@localhost:5432/my_database')

# Example for MySQL
SQL_URL = os.getenv('MYSQL_URL')
engine = create_engine(SQL_URL)

# Define the name of the table where you want to insert the data
table_name = 'Projects'

# Insert data into the SQL table
df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("Data inserted successfully")
