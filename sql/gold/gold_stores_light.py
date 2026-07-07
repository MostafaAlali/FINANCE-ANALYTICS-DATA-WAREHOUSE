import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE gold_stores_light AS 
    SELECT 
         store_code     AS Store_Code,
         store_name     AS Store_Name,
         store_type     AS Store_Type,
         country        AS Country,
         region         AS Region
    FROM silver_stores_light
    ORDER BY store_code;
"""
)

print(" Created gold_stores_light")

con.close()