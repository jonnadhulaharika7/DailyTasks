CREATE TABLE customer_orders(
order_id integer,
customer_id integer,
order_date date,
order_amount integer
);
SELECT * FROM customer_orders
INSERT INTO customer_orders values(1,100,cast('2022-01-01' as date),2000),
                                    (2,200,cast('2022-01-01' as date),2500),
									(2,300,cast('2022-01-01' as date),2100),
									(4,100,cast('2022-01-02' as date),2000),
									(5,400,cast('2022-01-02' as date),2200),
									(6,500,cast('2022-01-02' as date),2700),
									(7,100,cast('2022-01-03' as date),3000),
									(8,400,cast('2022-01-03' as date),1000),
									(9,600,cast('2022-01-03' as date),3000);
with first_visit as(
SELECT customer_id, min(order_date) as first_visit_date
FROM customer_orders
GROUP BY customer_id)
SELECT co.order_date
,SUM(CASE WHEN co.order_date=fv.first_visit_date then 1 else 0 end) as first_visit_flag
,SUM(CASE WHEN co.order_date!=fv.first_visit_date then 1 else 0 end) as repeat_visit_flag
FROM customer_orders co
INNER JOIN first_visit fv ON co.customer_id=fv.customer_id
GROUP BY co.order_date
;
