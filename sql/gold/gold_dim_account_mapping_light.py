import duckdb, os 



con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE gold_dim_account_mapping_light AS 
    SELECT 
         account_number             AS Account_Number,
         account_name               AS account_Name,
         pl_line                    AS pl_Line,
         statement_type             AS Statement_Type,
         sort_order                 AS Sort_Order,
         notes                      AS Notes
    FROM  silver_account_mapping_light
    ORDER BY sort_Order , Account_Number;
"""
)

print(" Created gold_dim_account_mapping_light")

con.close()