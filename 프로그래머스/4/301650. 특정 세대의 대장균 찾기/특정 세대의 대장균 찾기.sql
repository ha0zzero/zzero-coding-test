with ed as (select id, parent_id
from ecoli_data)
select e1.id
from ed as e1
left join ed as e2 on e1.parent_id = e2.id
left join ed as e3 on e2.parent_id = e3.id
where e2.parent_id is not null and e3.parent_id is null