# Write your MySQL query statement below
select product_name, year , price from product,sales where sales.product_id = product.product_id;