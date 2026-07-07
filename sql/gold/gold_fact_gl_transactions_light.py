import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE gold_fact_gl_transactions_light AS 
    SELECT 
         transaction_id       AS Transaction_ID,
         transaction_date     AS Transaction_Date,
         store_code           AS Store_Code,
         account_number       AS Account_Number,
         amount_local         AS Amount_Local,
         currency             AS Currency,
         document_number      AS Document_Number,   
         description          AS Description
    FROM silve_gl_transactions_light
    ORDER BY Transaction_ID;
"""
)

print(" Created gold_fact_gl_transactions_light")

con.close()