-- 자동차 종류 '트럭'
-- 기록별 대여금액
-- 대여 기록 ID, 대여금액 리스트
/*
with h as (SELECT history_id, car_id, date(end_date) - date(start_date) + 1 as duration,
case when date(end_date) - date(start_date) +1 >= 90 then '90일 이상'
when date(end_date) - date(start_date) +1 >= 30 then '30일 이상'
when date(end_date) - date(start_date) +1 >= 7 then '7일 이상'
else null end as duration_type
from car_rental_company_rental_history)
select 
    
    h.history_id, 
    case when discount_rate is null then c.daily_fee * h.duration
    else FLOOR(c.daily_fee * (100 - d.discount_rate) / 100 * h.duration) end as fee
    
from h
left join car_rental_company_car as c on h.car_id = c.car_id
left join car_rental_company_discount_plan as d on h.duration_type = d.duration_type AND c.car_type = d.car_type
where c.car_type = '트럭'
order by fee desc, history_id desc
*/

WITH h AS (
    SELECT 
        history_id, 
        car_id, 
        DATEDIFF(end_date, start_date) + 1 AS duration,
        CASE 
            WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
            ELSE NULL 
        END AS duration_type
    FROM car_rental_company_rental_history
)
SELECT 
    h.history_id, 
    CASE 
        WHEN d.discount_rate IS NULL THEN c.daily_fee * h.duration
        ELSE c.daily_fee * h.duration * (100 - d.discount_rate) DIV 100
    END AS fee
FROM h
JOIN car_rental_company_car AS c 
    ON h.car_id = c.car_id
LEFT JOIN car_rental_company_discount_plan AS d 
    ON c.car_type = d.car_type 
    AND h.duration_type = d.duration_type
WHERE c.car_type = '트럭'
ORDER BY fee DESC, history_id DESC;

