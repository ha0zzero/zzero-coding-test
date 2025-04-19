-- book_sales에서 2022년 1월의 도서 판매 데이터 추출, book_id별 sales의 합계 테이블 만들기
-- book 테이블과 join 후 저자별, 카테고리별 매출액 구하기
-- author 테이블과 join 후 데이터 추출
-- book_sales: book_id, sales_date, sales
-- author: author_id, author_name
-- book: book_id, category, author_id, price, published_date

/*
with dm as (select s.book_id, b.category, b.author_id, a.author_name, sum(s.sales) as book_sales, b.price
from book b
join book_sales s on b.book_id = s.book_id
join author a on b.author_id = a.author_id
where left(s.sales_date,7) = '2022-01'
group by s.book_id
order by s.book_id)
select author_id, author_name, category, sum(book_sales)*price as total_sales
from dm
group by author_id, category
order by author_id asc, category desc
*/

SELECT 
    b.author_id,
    a.author_name,
    b.category,
    SUM(s.sales * b.price) AS total_sales
FROM book_sales s
JOIN book b ON s.book_id = b.book_id
JOIN author a ON b.author_id = a.author_id
WHERE s.sales_date BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY b.author_id, a.author_name, b.category
ORDER BY b.author_id ASC, b.category DESC;
