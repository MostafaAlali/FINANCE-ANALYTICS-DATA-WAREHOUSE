import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE bronze_accounts_light AS 
    SELECT 
         account_number,
         account_name,
         account_type,
         currency
    FROM raw__accounts_light;
"""
)

print(" Created bronze_accounts_light")

con.close()