import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE silve_gl_transactions_light AS 
    SELECT 
         transaction_id,
         STRFTIME(transaction_date , '%d-%m-%Y') AS transaction_date,
         TRIM(store_code) AS store_code,
         account_number,
         amount_local,
         UPPER(TRIM(currency)) AS currency,
         TRIM(document_number) AS document_number,
         TRIM (description) AS description
    FROM bronze_gl_transactions_light;
"""
)

print(" Created silve_gl_transactions_light")

con.close()