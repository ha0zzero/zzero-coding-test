-- 코드를 입력하세요
SELECT MCDP_CD as 진료과코드, count(PT_NO) as 5월예약건수
FROM APPOINTMENT
WHERE left(apnt_ymd,7) = '2022-05'
GROUP BY MCDP_CD
# HAVING 
ORDER BY 5월예약건수 ASC, 진료과코드 ASC