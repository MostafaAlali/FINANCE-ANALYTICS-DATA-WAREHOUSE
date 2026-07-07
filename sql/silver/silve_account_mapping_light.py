import duckdb, os 
import pandas as pd



con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE silver_account_mapping_light AS 
    SELECT 
         CAST(AccountNumber AS INTEGER )  AS account_number,
         TRIM(AccountName)                AS account_name,
         TRIM(PLLine)                     AS pl_line,
         UPPER(TRIM(StatementType))       AS statement_type,
         CAST(SortOrder AS INTEGER)       AS sort_order,
         TRIM(Notes)                      AS notes
    FROM bronze_account_mapping_light;
"""
)

print(" Created silver_account_mapping_light")

con.close()