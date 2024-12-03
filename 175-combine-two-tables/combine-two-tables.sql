# Write your MySQL query statement below

select p.firstname, p.lastName, a.city, a.state from Person p
LEFT JOIN Address a ON p.personId = a. personId