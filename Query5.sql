CREATE TABLE orders (
    order_id INT,
    product_id INT,
    sales NUMERIC(10,2)
);

INSERT INTO orders (order_id, product_id, sales) VALUES
(1, 101, 500),
(2, 102, 300),
(3, 101, 200),
(4, 103, 150),
(5, 104, 100),
(6, 102, 100),
(7, 105, 50);

--4-80% of yoyr sales comes from 20% of your product or services

--select sum(sales) * 0.8 from orders
--1837760

with product_wise_sales as
 (select product_id, sum(sales) as product_sales
  from orders
  group by product_id)
  ,calc_sales as(
  select product_id, product_sales
  ,sum(product_sales) over (order by product_sales desc rows between unbounded preceding and 0 preceding) as running_sales
  ,0.8 * sum(product_sales) over() as total_sales
  from product_wise_sales)
  select * from calc_sales where running_sales <= total_sales