import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE bronze_stores_light AS 
    SELECT 
         store_code,
         store_name,
         store_type
    FROM raw__stores_light;
"""
)

print(" Created bronze_stores_light")

con.close()