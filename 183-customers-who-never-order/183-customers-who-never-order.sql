# Write your MySQL query statement below
SELECT 
    customers.name 
AS
    'Customers'
FROM 
    customers 
WHERE  
    customers.id NOT IN
    (SELECT customerId FROM orders)
;