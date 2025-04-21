-- 코드를 입력하세요
WITH CART_M AS (SELECT *
                FROM CART_PRODUCTS
                WHERE NAME = 'Milk'
                GROUP BY CART_ID),
CART_Y AS (SELECT *
               FROM CART_PRODUCTS
               WHERE NAME ='Yogurt'
               GROUP BY CART_ID)
SELECT M.CART_ID
FROM CART_M AS M
JOIN CART_Y AS Y ON M.CART_ID = Y.CART_ID
