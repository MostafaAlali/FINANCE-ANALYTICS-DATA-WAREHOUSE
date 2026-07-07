import duckdb, os 
import pandas as pd

data = os.path.join(os.path.dirname(__file__) ,"..","..","account_mapping_light.xlsx" )

df = pd.read_excel(data)


con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.register("df_account_mapping_light" , df)
con.execute(
    """
    CREATE OR REPLACE TABLE bronze_account_mapping_light AS 
    SELECT 
         *
    FROM df_account_mapping_light;
"""
)

print(" Created bronze_account_mapping_light")

con.close()