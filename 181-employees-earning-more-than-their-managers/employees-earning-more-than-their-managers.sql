# Write your MySQL query statement below


select e.name as Employee from employee e
where e.salary > (select e2.salary from employee e2
                    where e.managerID = e2.id


 )