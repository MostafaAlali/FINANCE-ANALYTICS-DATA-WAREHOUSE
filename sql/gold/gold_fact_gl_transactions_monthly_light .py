import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE gold_fact_gl_transactions_monthly_light AS 
    WITH base AS (
         SELECT 
            CAST(Transaction_Date AS DATE) AS Transaction_Date,
            Store_Code,
            Account_Number,
            Amount_Local
            FROM gold_fact_gl_transactions_light
        )
    SELECT 
        DATE_TRUNC('month', Transaction_Date) AS Transaction_Month,
        Store_Code,
        Account_Number,
        SUM(Amount_Local) AS Total_Amount_Local
    FROM base 
    GROUP BY  
        DATE_TRUNC('month', Transaction_Date),
        Store_Code,
        Account_Number
    ORDER BY 
        Transaction_Month,
        Store_Code,
        Account_Number;
"""
)

print("Created gold_fact_gl_transactions_monthly_light")

con.close()
