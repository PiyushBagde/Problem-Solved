# Write your MySQL query statement below
select customer_number from Orders
GROUP BY customer_number order by Count(customer_number) desc limit 1