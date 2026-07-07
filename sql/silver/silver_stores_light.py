import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE silver_stores_light AS 
    SELECT 
         s.store_code,
         TRIM(s.store_name) AS store_name,
         TRIM(s.store_type) AS store_type,
         TRIM (g.country) AS  country,
         g.region
    FROM bronze_stores_light s
    LEFT JOIN bronze_geograhpy_light g
    ON s.store_code = g.store_code;
"""
)

print(" Created silver_stores_light")

con.close()