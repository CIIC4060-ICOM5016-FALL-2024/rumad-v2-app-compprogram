import sqlite3
import pandas as pd

conn = sqlite3.connect('requisites.db')

# Query the data you want to convert (change 'your_table' to your actual table name)
query = 'SELECT * FROM requisites'
data = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Convert the DataFrame to CSV (change 'output.csv' to your desired output file)
data.to_csv('requisites.csv', index=False)