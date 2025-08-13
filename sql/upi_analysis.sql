-- SQL script for creating, loading, and analyzing UPI transaction data.


-- Drop the table if it already exists to start fresh.
DROP TABLE IF EXISTS upi_transactions;

-- Create the table structure.
CREATE TABLE upi_transactions (
    transaction_date DATE PRIMARY KEY,
    transaction_year INT,
    transaction_month INT,
    volume_in_crores REAL,
    value_in_rs_crores REAL,
    avg_transaction_value_rs REAL,
    yoy_volume_growth_percent REAL
);

-- Load data from the processed CSV file.
-- Note: This command is for MySQL. The path must be correct and security permissions (local_infile=1) may be required.
LOAD DATA LOCAL INFILE 'C:\Users\hp\OneDrive\Desktop\UPI_Analysis\upi_processed_data.CSV'
INTO TABLE upi_transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; -- This skips the header row


-- =================================================================================
-- Basic Sanity Checks and Queries
-- =================================================================================

-- Query 1: Confirm the data has been loaded by counting the rows.
SELECT COUNT(*) AS total_months_loaded FROM upi_transactions;

-- Query 2: Retrieve the total transaction volume for the year 2023.
SELECT SUM(volume_in_crores) AS total_volume_2023
FROM upi_transactions
WHERE transaction_year = 2023;

-- Query 3: Find the month with the highest transaction value in the entire dataset.
SELECT transaction_year, transaction_month, value_in_rs_crores
FROM upi_transactions
ORDER BY value_in_rs_crores DESC
LIMIT 1;


-- =================================================================================
-- Advanced Analysis Queries
-- =================================================================================

-- Query 4: Calculate Month-over-Month (MoM) percentage growth in transaction volume.
-- This helps identify periods of rapid acceleration or deceleration.
SELECT
    transaction_date,
    volume_in_crores,
    LAG(volume_in_crores, 1, 0) OVER (ORDER BY transaction_date) AS previous_month_volume,
    ROUND(((volume_in_crores - LAG(volume_in_crores, 1, 0) OVER (ORDER BY transaction_date)) / LAG(volume_in_crores, 1, 0) OVER (ORDER BY transaction_date)) * 100, 2) AS mom_growth_percent
FROM
    upi_transactions;


-- Query 5: Find the largest percentage drop in transaction volume month-over-month.
-- This is useful for identifying the impact of external events, like the COVID-19 lockdown.
SELECT
    transaction_date,
    ROUND(((volume_in_crores - LAG(volume_in_crores, 1) OVER (ORDER BY transaction_date)) / LAG(volume_in_crores, 1) OVER (ORDER BY transaction_date)) * 100, 2) AS mom_growth_percent
FROM
    upi_transactions
ORDER BY
    mom_growth_percent ASC
LIMIT 1;


-- Query 6: Calculate total transaction volume by quarter for each year.
-- This helps in identifying seasonal trends (e.g., higher spending in Q4 due to festivals).
SELECT
    transaction_year,
    (transaction_month - 1) / 3 + 1 AS quarter,
    SUM(volume_in_crores) AS total_quarterly_volume
FROM
    upi_transactions
GROUP BY
    transaction_year, quarter
ORDER BY
    transaction_year, quarter;


-- Query 7: Calculate a 3-month moving average for transaction volume.
-- This smooths out short-term fluctuations and highlights the longer-term trend more clearly.
SELECT
    transaction_date,
    volume_in_crores,
    AVG(volume_in_crores) OVER (ORDER BY transaction_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS three_month_moving_avg
FROM
    upi_transactions;

