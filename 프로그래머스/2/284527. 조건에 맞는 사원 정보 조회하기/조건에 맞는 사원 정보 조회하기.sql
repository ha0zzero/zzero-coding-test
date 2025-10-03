-- 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회
-- 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회
-- 2022년도의 평가 점수는 상,하반기 점수의 합을 의미하고, 평가 점수를 나타내는 컬럼의 이름은 SCORE

-- HR_EMPLOYEES 부서 정보 (사번, 성명, 직책, 이메일)
-- HR_GRADE (점수)

SELECT SCORE22.SCORE, H.EMP_NO, H.EMP_NAME, H.POSITION, H.EMAIL
FROM HR_EMPLOYEES AS H
JOIN (SELECT EMP_NO, SUM(SCORE) AS SCORE
FROM HR_GRADE
GROUP BY EMP_NO
ORDER BY 2 DESC
LIMIT 1) AS SCORE22
ON H.EMP_NO = SCORE22.EMP_NO