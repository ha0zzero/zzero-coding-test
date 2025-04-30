-- 자동차 종류: 세단, SUV -> o
-- 기간: 2022.11.1 ~ 2022.11.30 과 안겹치게
-- 대여금액: 50만원 이상 ~ 200만원 미만
-- 출력: 자동차ID, 자동차 종류, 대여 금액
-- 정렬: 대여 금액 desc, 자동차 종류 asc

-- car_id, car_type, daily_fee

/*
select c.car_id, c.car_type, c.daily_fee, h.history_id, h.start_date, h.end_date
from CAR_RENTAL_COMPANY_CAR as c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h on c.car_id = h.car_id
where c.car_type in ('세단', 'suv')
    and (
        h.start_date between '2022-11-01' and '2022-11-30'
    or h.end_date between '2022-11-01' and '2022-11-30'
    or h.start_date < '2022-11-01' and h.end_date > '2022-11-30')
order by c.car_id
-- 26, 16, 29, 22, 28, 5, 11, 2, 7, 1, 4, 6, 8
*/
/*
with h as (
select *
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where
    start_date between '2022-11-01' and '2022-11-30'
    or end_date between '2022-11-01' and '2022-11-30'
    or start_date < '2022-11-01' and end_date > '2022-11-30'
)
select *
from h
full outer join CAR_RENTAL_COMPANY_CAR as c 
on h.car_id = c.car_id
where h.car_id is null or c.car_id is null;
*/

SELECT 
    c.car_id,
    c.car_type,
    FLOOR(c.daily_fee * (100 - d.discount_rate) / 100 * 30) AS fee
FROM 
    CAR_RENTAL_COMPANY_CAR c
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
    ON c.car_type = d.car_type AND d.duration_type = '30일 이상'
WHERE 
    c.car_type IN ('세단', 'SUV')
    AND NOT EXISTS (
        SELECT 1
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        WHERE h.car_id = c.car_id
          AND (
              h.start_date <= '2022-11-30' AND h.end_date >= '2022-11-01'
          )
    )
HAVING 
    fee BETWEEN 500000 AND 1999999
ORDER BY 
    fee DESC,
    c.car_type ASC,
    c.car_id DESC;
