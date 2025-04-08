-- 2022.04.13 / 흉부외과(CS)/ 취소되지 않은 진료 예약 내역 조회
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 출력
-- APPOINTMENT: 진료예약번호, 환자번호, 진료과코드, 의사ID
-- 진료예약일시 기준 오름차순

-- 일단 APPOINTMENT에서 필터링을 다 거친 후 마지막에 환자와 닥터를 조인하면 될듯!

SELECT 
    A.APNT_NO AS APNT_NO,
    P.PT_NAME AS PT_NAME,
    A.PT_NO AS PT_NO,
    A.MCDP_CD AS MCDP_CD,
    D.DR_NAME AS DR_NAME,
    A.APNT_YMD AS APNT_YMD
FROM APPOINTMENT A
JOIN PATIENT P ON A.PT_NO = P.PT_NO
JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE DATE(A.APNT_YMD) = '2022-04-13'
  AND A.MCDP_CD = 'CS'
  AND A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD ASC;


