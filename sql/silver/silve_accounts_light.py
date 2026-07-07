import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE silver_accounts_light AS 
    SELECT 
         CAST(account_number AS INTEGER)    AS account_number,
         TRIM(account_name)                 AS account_name,
         UPPER(TRIM(account_type))          AS account_type,
         UPPER(TRIM(currency))              AS currency
    FROM bronze_accounts_light;
"""
)

print(" Created silver_accounts_light")

con.close()