import pandas as pd
from sqlalchemy import create_engine

# Database connection details
db_config = {
    'dbname': 'nexa-crm-prod',
    'user': 'avnadmin',
    'password': 'Digital!23',
    'host': 'nagarjuna-crm-dbs.postgres.database.azure.com',
    'port': '5432'  # Default PostgreSQL port is 5432
}

# Create a connection string
connection_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

# Create a database engine
engine = create_engine(connection_string)

# Query the data into a DataFrame
query = "SELECT * FROM public.leads"  # Replace 'your_table_name' with your actual table name
df = pd.read_sql(query, engine)

# Get unique values for each column
unique_values = {}
for column in df.columns:
    if df[column].apply(lambda x: isinstance(x, list)).any():
        # Flatten the list and get unique values
        unique_values[column] = pd.Series([item for sublist in df[column] for item in sublist]).unique().tolist()
    else:
        unique_values[column] = df[column].unique().tolist()

# Print the unique values
for column, values in unique_values.items():
    print(f"Unique values in column '{column}': {values}\n")
