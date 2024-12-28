CREATE DATABASE MH;
CREATE SCHEMA SCH;






-- DimDate
CREATE OR REPLACE  TABLE DimDate (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    day_of_week VARCHAR(10),
    month_name VARCHAR(10),
    quarter VARCHAR(2),
    is_weekend BOOLEAN,
    is_holiday BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- DimCardholder
CREATE OR REPLACE  TABLE DimCardholder (
    cardholder_key INT AUTOINCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    cardholder_type VARCHAR(20) NOT NULL,
    onboarding_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    valid_from TIMESTAMP_NTZ NOT NULL,
    valid_to TIMESTAMP_NTZ DEFAULT TO_TIMESTAMP_NTZ('9999-12-31 00:00:00'),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP
);


-- DimAccount
CREATE OR REPLACE  TABLE DimAccount (
    account_key INT AUTOINCREMENT PRIMARY KEY,
    account_number VARCHAR(16) NOT NULL,
    account_credit_limit DECIMAL(12,2) NOT NULL,
    opening_date DATE NOT NULL,
    account_status VARCHAR(20) NOT NULL,
    primary_cardholder_key INT REFERENCES DimCardholder(cardholder_key),
    is_active BOOLEAN DEFAULT true,
    valid_from TIMESTAMP NOT NULL,
    valid_to TIMESTAMP_NTZ DEFAULT TO_TIMESTAMP_NTZ('9999-12-31 00:00:00'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DimPlasticCard
CREATE OR REPLACE  TABLE DimPlasticCard (
    card_key INT AUTOINCREMENT PRIMARY KEY,
    account_key INT REFERENCES DimAccount(account_key),
    cardholder_key INT REFERENCES DimCardholder(cardholder_key),
    card_number VARCHAR(16) NOT NULL,
    card_credit_limit DECIMAL(12,2) NOT NULL,
    issue_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    card_status VARCHAR(20) NOT NULL,
    is_primary_card BOOLEAN NOT NULL,
    valid_from TIMESTAMP NOT NULL,
    valid_to TIMESTAMP_NTZ DEFAULT TO_TIMESTAMP_NTZ('9999-12-31 00:00:00'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fact Tables

-- FactDailyAccountBalance
CREATE OR REPLACE  TABLE FactDailyAccountBalance (
    balance_id INT AUTOINCREMENT PRIMARY KEY,
    date_key INT REFERENCES DimDate(date_key),
    account_key INT REFERENCES DimAccount(account_key),
    outstanding_balance DECIMAL(12,2) NOT NULL,
    total_payments DECIMAL(12,2) NOT NULL,
    total_purchases DECIMAL(12,2) NOT NULL,
    credit_utilization_pct DECIMAL(5,2) NOT NULL,
    snapshot_timestamp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- FactCardActivity
CREATE OR REPLACE  TABLE FactCardActivity (
    activity_id INT AUTOINCREMENT PRIMARY KEY,
    date_key INT REFERENCES DimDate(date_key),
    card_key INT REFERENCES DimPlasticCard(card_key),
    account_key INT REFERENCES DimAccount(account_key),
    transaction_amount DECIMAL(12,2) NOT NULL,
    activity_type VARCHAR(50) NOT NULL,
    running_balance DECIMAL(12,2) NOT NULL,
    activity_timestamp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data with Indian context

-- DimDate (Sample data for 2024)
INSERT INTO DimDate (date_key, full_date, year, month, day, day_of_week, month_name, quarter, is_weekend, is_holiday)
WITH date_series AS (
    SELECT DATEADD(day, seq4(), '2023-01-01') AS dt
    FROM TABLE(GENERATOR(ROWCOUNT => 365))
)
SELECT 
    TO_NUMBER(TO_CHAR(dt, 'YYYYMMDD')) AS date_key,
    dt AS full_date,
    EXTRACT(YEAR FROM dt) AS year,
    EXTRACT(MONTH FROM dt) AS month,
    EXTRACT(DAY FROM dt) AS day,
    DAYOFWEEK(dt) AS day_of_week,
    TO_CHAR(dt, 'MON') AS month_name,
   'Q'||quarter(dt) AS quarter,
    CASE WHEN EXTRACT(DOW FROM dt) IN (0, 6) THEN true ELSE false END AS is_weekend,
    CASE WHEN TO_CHAR(dt, 'MMDD') IN ('0126', '0815', '0102') THEN true ELSE false END AS is_holiday
FROM date_series;




-- DimCardholder
INSERT INTO DimCardholder (first_name, last_name, cardholder_type, onboarding_date, status, valid_from)
VALUES
    ('Rajesh', 'Kumar', 'PRIMARY', '2023-01-15', 'ACTIVE', '2023-01-15'),
    ('Priya', 'Sharma', 'PRIMARY', '2023-02-01', 'ACTIVE', '2023-02-01'),
    ('Amit', 'Patel', 'ADDITIONAL', '2023-01-20', 'ACTIVE', '2023-01-20'),
    ('Sneha', 'Gupta', 'PRIMARY', '2023-03-10', 'ACTIVE', '2023-03-10'),
    ('Deepak', 'Singh', 'ADDITIONAL', '2023-02-15', 'ACTIVE', '2023-02-15');

-- DimAccount
INSERT INTO DimAccount (account_number, account_credit_limit, opening_date, account_status, primary_cardholder_key, valid_from)
VALUES
    ('4563780123456789', 200000.00, '2023-01-15', 'ACTIVE', 1, '2023-01-15'),
    ('4563780123456790', 150000.00, '2023-02-01', 'ACTIVE', 2, '2023-02-01'),
    ('4563780123456791', 300000.00, '2023-03-10', 'ACTIVE', 4, '2023-03-10');

-- DimPlasticCard
INSERT INTO DimPlasticCard (account_key, cardholder_key, card_number, card_credit_limit, issue_date, expiry_date, card_status, is_primary_card, valid_from)
VALUES
    (1, 1, '4563780123456789', 200000.00, '2023-01-15', '2026-01-31', 'ACTIVE', true, '2023-01-15'),
    (1, 3, '4563780123456792', 50000.00, '2023-01-20', '2026-01-31', 'ACTIVE', false, '2023-01-20'),
    (2, 2, '4563780123456790', 150000.00, '2023-02-01', '2026-02-28', 'ACTIVE', true, '2023-02-01'),
    (2, 5, '4563780123456793', 30000.00, '2023-02-15', '2026-02-28', 'ACTIVE', false, '2023-02-15'),
    (3, 4, '4563780123456791', 300000.00, '2023-03-10', '2026-03-31', 'ACTIVE', true, '2023-03-10');

-- FactCardActivity (Sample transactions)
INSERT INTO FactCardActivity (date_key, card_key, account_key, transaction_amount, activity_type, running_balance, activity_timestamp)
VALUES
    (20240101, 1, 1, 25999.00, 'PURCHASE', 25999.00, '2024-01-01 10:30:00'),
    (20240101, 1, 1, 5499.00, 'PURCHASE', 31498.00, '2024-01-01 14:45:00'),
    (20240102, 2, 1, 1999.00, 'PURCHASE', 33497.00, '2024-01-02 09:15:00'),
    (20240102, 3, 2, 15999.00, 'PURCHASE', 15999.00, '2024-01-02 11:30:00'),
    (20240103, 4, 2, 999.00, 'PURCHASE', 16998.00, '2024-01-03 16:20:00'),
    (20240103, 5, 3, 45999.00, 'PURCHASE', 45999.00, '2024-01-03 18:45:00'),
    (20240104, 1, 1, -10000.00, 'PAYMENT', 23497.00, '2024-01-04 10:00:00'),
    (20240104, 3, 2, -5000.00, 'PAYMENT', 11998.00, '2024-01-04 14:30:00');






select * from DimDate;
select * from DimCardholder;
select * from DimAccount;

select * from DimPlasticCard;

select * from  FactDailyAccountBalance;

select * from  FactCardActivity;

-- 1. Monthly spending pattern by primary cardholders
SELECT 
    dc.first_name || ' ' || dc.last_name as cardholder_name,
    dd.month_name,
    SUM(CASE WHEN fa.activity_type = 'PURCHASE' THEN fa.transaction_amount ELSE 0 END) as total_purchases,
    SUM(CASE WHEN fa.activity_type = 'PAYMENT' THEN ABS(fa.transaction_amount) ELSE 0 END) as total_payments
FROM FactCardActivity fa
JOIN DimPlasticCard dp ON fa.card_key = dp.card_key
JOIN DimCardholder dc ON dp.cardholder_key = dc.cardholder_key
JOIN DimDate dd ON fa.date_key = dd.date_key
WHERE dp.is_primary_card = true
GROUP BY dc.first_name, dc.last_name, dd.month_name
ORDER BY dc.first_name, dc.last_name, dd.month_name;

-- 2. Credit utilization trends
SELECT 
    dd.full_date,
    da.account_number,
    dc.first_name || ' ' || dc.last_name as primary_cardholder,
    fdb.outstanding_balance,
    fdb.credit_utilization_pct
FROM FactDailyAccountBalance fdb
JOIN DimAccount da ON fdb.account_key = da.account_key
JOIN DimCardholder dc ON da.primary_cardholder_key = dc.cardholder_key
JOIN DimDate dd ON fdb.date_key = dd.date_key
ORDER BY dd.full_date, da.account_number;

-- 3. Additional cardholder spending analysis
SELECT 
    dc.first_name || ' ' || dc.last_name as additional_cardholder,
    SUM(CASE WHEN fa.activity_type = 'PURCHASE' THEN fa.transaction_amount ELSE 0 END) as total_spent,
    COUNT(CASE WHEN fa.activity_type = 'PURCHASE' THEN 1 END) as number_of_purchases,
    MAX(fa.transaction_amount) as largest_purchase
FROM FactCardActivity fa
JOIN DimPlasticCard dp ON fa.card_key = dp.card_key
JOIN DimCardholder dc ON dp.cardholder_key = dc.cardholder_key
WHERE dp.is_primary_card = false
GROUP BY dc.first_name, dc.last_name
ORDER BY total_spent DESC;




--4  Calculate Daily Outstanding Balances and Utilization
INSERT INTO FactDailyAccountBalance (account_key, date_key, outstanding_balance, total_payments, total_purchases, credit_utilization_pct, snapshot_timestamp)
WITH DailyBalances AS (
    SELECT
        da.account_key,
        dd.date_key,
        SUM(CASE WHEN fa.activity_type = 'PURCHASE' THEN fa.transaction_amount ELSE 0 END) AS total_purchases,
        SUM(CASE WHEN fa.activity_type = 'PAYMENT' THEN ABS(fa.transaction_amount) ELSE 0 END) AS total_payments,
        COALESCE(
            (
                SELECT SUM(transaction_amount)
                FROM FactCardActivity fa2
                WHERE fa2.account_key = da.account_key
                  AND fa2.activity_timestamp <= dd.full_date
            ), 0
        ) AS outstanding_balance,
        ROUND(
            100 * COALESCE(
                (
                    SELECT SUM(transaction_amount)
                    FROM FactCardActivity fa2
                    WHERE fa2.account_key = da.account_key
                      AND fa2.activity_timestamp <= dd.full_date
                ), 0
            ) / da.account_credit_limit, 2
        ) AS credit_utilization_pct
    FROM DimAccount da
    CROSS JOIN DimDate dd
    LEFT JOIN FactCardActivity fa ON da.account_key = fa.account_key AND fa.date_key = dd.date_key
   WHERE dd.full_date = CURRENT_DATE -- Track only today's snapshot
    GROUP BY da.account_key, dd.date_key, da.account_credit_limit, dd.full_date
)

SELECT
    account_key,
    date_key,
    outstanding_balance,
    total_payments,
    total_purchases,
    credit_utilization_pct,
    CURRENT_TIMESTAMP
FROM DailyBalances;









