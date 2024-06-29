import pandas as pd
import numpy as np
import psycopg2

# Defining connection parameters
dbname = "nexa-crm-ai-dev"
user = "avnadmin"
password = "Digital!23"
host = "nagarjuna-crm-dbs.postgres.database.azure.com"  # defaults to localhost if not provided
port = "5432"  # defaults to 5432 if not provided

# Establish connection to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()
print("Connection is created")

# Defining the SQL query
sql_query = f'SELECT "leadStatus","name" FROM public.leads'

# Executing the query
cur.execute(sql_query)

# Fetching all rows from the executed query
rows = cur.fetchall()
print("rows: ",rows)

# Getting the column names
col_names = [col[0] for col in cur.description]
print(col_names)

# Creating a DataFrame from the fetched data
df = pd.DataFrame(rows, columns=col_names)

# Closing the cursor and connection
cur.close()
conn.close()

# Displaying the Main dataFrame
df.head()
