import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE gold_dim_accounts_light AS 
    SELECT 
         account_number           AS Account_Number,
         account_name             AS Account_Name,
         account_type             AS Account_Type,
         currency                 AS Currency
    FROM silver_accounts_light
    ORDER BY Account_Number;
"""
)

print(" Created gold_dim_accounts_light")

con.close()