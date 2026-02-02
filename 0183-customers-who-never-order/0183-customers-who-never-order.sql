# Write your MySQL query statement below
select name customers from customers left join orders on customers.id = orders.customerid where orders.id is null;