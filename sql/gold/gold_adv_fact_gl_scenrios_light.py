import duckdb, os 

con = duckdb.connect(os.path.join(os.path.dirname(__file__) ,"..","..","finance_analytics_light_raw.duckdb" ))

con.execute(
    """
    CREATE OR REPLACE TABLE gold_adv_fact_gl_scenrios_light  AS 
    WITH base AS (
         SELECT 
            DATE_TRUNC( 'month' , Transaction_Date) AS Transaction_Month,
            Store_Code,
            Account_Number,
            SUM(Amount_Local)                                                  AS Amount_Local
            FROM gold_fact_gl_transactions_light
            GROUP BY 
                    Transaction_Month,
                    Store_Code,
                    Account_Number
)
SELECT 
    Transaction_Month,
    Store_Code,
    Account_Number,
    'Actual' AS Scenario,
    Amount_Local 

FROM base 

UNION ALL
SELECT 
    Transaction_Month,
    Store_Code,
    Account_Number,
    'BestCase' AS Scenario,
    CASE 
        WHEN Amount_Local >= 0 THEN Amount_Local * 1.10
        ELSE Amount_Local * 0.90
    END AS Amount_Local
FROM base

UNION ALL
SELECT 
    Transaction_Month,
    Store_Code,
    Account_Number,
    'WorstCase' AS Scenario,
    CASE 
        WHEN Amount_Local >= 0 THEN Amount_Local * 0.90
        ELSE Amount_Local * 1.10
    END AS Amount_Local
FROM base

ORDER BY 
    Transaction_Month,
    Store_Code,
    Account_Number,
    Scenario;
"""
)

print(" Created gold_adv_fact_gl_scenrios_light ")

con.close()
