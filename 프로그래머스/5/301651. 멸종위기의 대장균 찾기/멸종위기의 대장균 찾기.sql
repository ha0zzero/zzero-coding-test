-- 코드를 작성해주세요

WITH RECURSIVE generation_cte AS (
  -- 1) Anchor: 부모가 없는 개체 = 1세대
  SELECT
      ID,
      PARENT_ID,
      1 AS GENERATION
  FROM ECOLI_DATA
  WHERE PARENT_ID IS NULL

  UNION ALL

  -- 2) Recursive step: 직전 단계의 개체를 부모로 가지는 자식들을 찾아 세대 + 1
  SELECT
      e.ID,
      e.PARENT_ID,
      g.GENERATION + 1 AS GENERATION
  FROM ECOLI_DATA e
  JOIN generation_cte g
    ON e.PARENT_ID = g.ID
)

-- 3) Leaf(자식 없음)만 남기고
-- 4) 세대별로 묶어 카운트
SELECT
    COUNT(*) AS COUNT,
    GENERATION
FROM generation_cte g
WHERE NOT EXISTS (
    SELECT 1
    FROM ECOLI_DATA c
    WHERE c.PARENT_ID = g.ID   -- g가 부모인 자식이 하나도 없으면(=리프)
)
GROUP BY GENERATION
ORDER BY GENERATION;
