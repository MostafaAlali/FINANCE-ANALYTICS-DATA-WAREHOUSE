import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE bronze_geograhpy_light AS 
    SELECT 
         store_code,
         country,
         region
    FROM raw__geography_light;
"""
)

print(" Created bronze_geograhpy_light")

con.close()