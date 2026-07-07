import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE bronze_gl_transactions_light AS 
    SELECT 
         transaction_id,
         transaction_date,
         store_code,
         account_number,
         amount_local,
         currency,
         document_number,
         description
    FROM raw__gl_transactions_light;
"""
)

print(" Created bronze_gl_transactions_light")

con.close()