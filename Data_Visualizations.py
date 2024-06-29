import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Replace with your actual database connection details
engine = create_engine('postgresql://avnadmin:Digital!23@nagarjuna-crm-dbs.postgres.database.azure.com:5432/nexa-crm-prod')

# Query to retrieve data
query = f'SELECT "leadSource","techStack","classMode","feeQuoted","nextFollowUp","createdAt","updatedAt","leadStatus" FROM public.leads'  # Replace 'your_table_name' with your actual table name
df = pd.read_sql(query, engine)

# Separate the datetime into date and time
columns = ['nextFollowUp', 'createdAt', 'updatedAt']
for col in columns:
    df[f'{col}_date'] = df[col].dt.date
    df[f'{col}_time'] = df[col].dt.time
    df[f'{col}_day'] = df[col].dt.day_name()
df

# Unique values collection 
unique_values = {column: df[column].unique().tolist() for column in df.columns}
for column, values in unique_values.items():
    print(f"Unique values in column '{column}': {values}\n")

# Group by Category and sum the Sales
sales_by_category = df.groupby('techStack')['feeQuoted'].sum().reset_index()

# Sort the data to ensure the line plot is drawn in the order of categories
sales_by_category = sales_by_category.sort_values('techStack')

print(sales_by_category.columns)
print(sales_by_category.head())
# Ensure 'feeQuoted' is numeric
sales_by_category['feeQuoted'] = pd.to_numeric(sales_by_category['feeQuoted'], errors='coerce')
print(sales_by_category['feeQuoted'])
sales_by_category['log_feeQuoted'] = np.log10(sales_by_category['feeQuoted'] + 1)
import plotly.express as px


# Label encoding using pd.Categorical
df['nextFollowUp_day_encoded'] = pd.Categorical(df['nextFollowUp_day']).codes
df['createdAt_day_encoded'] = pd.Categorical(df['createdAt_day']).codes

print(df)
# Plot the 2D density plot
plt.figure(figsize=(10, 6))
sns.kdeplot(x='nextFollowUp_day_encoded', y='', data=df, fill=True, cmap='viridis')
plt.title('2D Density Plot using Seaborn')
plt.xlabel('')
plt.show()
# Extract colors from the plot
colors = plt.collections[0].get_facecolors()

# Plot the 2D density plot with a colorbar
plt.figure(figsize=(10, 6))
sns.kdeplot(x='nextFollowUp_day_encoded', y='createdAt_day_encoded', data=df, fill=True, cmap='viridis')
plt.colorbar(label='Density')
plt.title('2D Density Plot using Seaborn with Colorbar')
plt.xlabel('nextFollowUp_day')
plt.ylabel('createdAt_day')
plt.show()