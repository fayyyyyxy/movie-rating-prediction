import warnings
warnings.filterwarnings(
    "ignore",
    message="pandas only supports SQLAlchemy connectable",
    category=UserWarning,
)

import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

# load variables from .env into environment
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# connect to Postgres
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
)

# query to get all movies
query = """
    SELECT *
    FROM public.movies;  
"""

print("Running query...")
df = pd.read_sql_query(query, conn) 
conn.close()

# show basic info about the data
print("First 5 rows:")
print(df.head())
print("\nShape:", df.shape)

# save to csv
df.to_csv("data/movies_data.csv", index=False)
print("\nData saved to movies_data.csv")