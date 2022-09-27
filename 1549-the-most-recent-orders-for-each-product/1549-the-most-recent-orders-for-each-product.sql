# Write your MySQL query statement below
With cte AS
(SELECT p.product_name, o.product_id, o.order_id, o.order_date, 
       RANK() OVER (PARTITION BY o.product_id ORDER BY o.order_date DESC) AS rnk
FROM Orders o
LEFT JOIN Products p
ON o.product_id = p.product_id)

SELECT product_name, product_id, order_id, order_date
FROM cte
WHERE rnk = 1
ORDER BY product_name, product_id, order_id
;