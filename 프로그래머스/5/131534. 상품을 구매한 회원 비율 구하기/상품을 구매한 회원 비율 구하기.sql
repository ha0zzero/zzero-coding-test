-- 코드를 입력하세요
WITH joined_2021 AS (
    SELECT user_id
    FROM user_info
    WHERE YEAR(joined) = 2021
),
purchased AS (
    SELECT DISTINCT 
        YEAR(s.sales_date) AS year,
        MONTH(s.sales_date) AS month,
        s.user_id
    FROM online_sale s
    JOIN joined_2021 u ON s.user_id = u.user_id
),
summary AS (
    SELECT 
        year,
        month,
        COUNT(DISTINCT user_id) AS purchased_users
    FROM purchased
    GROUP BY year, month
)

SELECT 
    s.year,
    s.month,
    s.purchased_users,
    ROUND(s.purchased_users / (SELECT COUNT(*) FROM joined_2021), 1) AS purchased_ratio
FROM summary s
ORDER BY s.year, s.month;