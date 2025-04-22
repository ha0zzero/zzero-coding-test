# 리뷰를 가장 많이 작성한 회원 구하기
with t as (
    select r.member_id, m.member_name, count(r.review_text),
            rank() over (order by count(r.review_text) desc) as member_rank
    from rest_review as r
    join member_profile as m
    on r.member_id = m.member_id
    group by r.member_id
    order by 3 desc
)
select t.member_name, rr.review_text, left(rr.review_date, 10)
from t
join rest_review rr
on t.member_id = rr.member_id
where t.member_rank = 1
order by 3, 2