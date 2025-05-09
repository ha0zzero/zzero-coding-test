with em as(select case when e.salary > m.salary then e.name end as Employee
from employee as e
join employee as m on e.managerId = m.id)
select *
from em
where Employee is not null
