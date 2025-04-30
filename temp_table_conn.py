import snowflake.connector
import os

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("DESMONDTIONGQUICO"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse="YOUR_WAREHOUSE",
    database="YOUR_DATABASE",
    schema="YOUR_SCHEMA"
)

# Create a temp table
query = """
CREATE OR REPLACE TEMPORARY TABLE temp_sales_data AS
SELECT * FROM raw_sales_data
WHERE created_date >= CURRENT_DATE - INTERVAL '7 DAY'
"""

with conn.cursor() as cur:
    cur.execute(query)

print("Temporary table created.")
