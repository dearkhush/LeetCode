# Write your MySQL query statement belo
select m.name as employee from employee e inner join employee m on e.id = m.managerId where e.salary < m.salary;
