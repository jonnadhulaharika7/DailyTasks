CREATE TABLE Employee2(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
dept_id INT,
salary DECIMAL(10,2),
manager_id INT
);

CREATE TABLE Department4(
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50),
location VARCHAR(50)
);

INSERT INTO Employee2
    (emp_id, emp_name, dept_id, salary, manager_id)
VALUES
    (101, 'Ravi', 10, 60000, NULL),
    (102, 'Priya', 20, 45000, 101),
    (103, 'Arjun', 10, 75000, 101),
    (104, 'Sneha', 30, 55000, 102),
    (105, 'Kiran', NULL, 40000, 101),
    (106, 'Divya', 20, 90000, 102),
    (107, 'Manoj', 40, 50000, NULL);
    
INSERT INTO Department4
    (dept_id, dept_name, location)
VALUES
    (10, 'IT', 'Hyderabad'),
    (20, 'HR', 'Chennai'),
    (30, 'Finance', 'Bengaluru'),
    (50, 'Marketing', 'Hyderabad');    
SELECT * FROM Employee2;
SELECT * FROM Department4;

SELECT e.emp_name,
       e.salary,
	   d.dept_name
FROM Employee2 e
INNER JOIN Department4 d
ON e.dept_id = d.dept_id;

SELECT e.emp_name,
	   e.salary,
       d.dept_name
FROM Employee2 e 
LEFT JOIN Department4 d
ON e.dept_id = d.dept_id;

SELECT e.emp_name,
	   e.salary,
	   d.dept_name
FROM Employee2 e
RIGHT JOIN Department4 d
ON e.dept_id = d.dept_id;

SELECT e.emp_name,
       d.dept_name
FROM Employee2 e
LEFT JOIN Department4 d
ON e.dept_id = d.dept_id
UNION
SELECT e.emp_name,
       d.dept_name
FROM Employee2 e
RIGHT JOIN Department4 d
ON e.dept_id = d.dept_id;

SELECT e.emp_name,
       d.dept_name
FROM Employee2 e
CROSS JOIN Department4 d;

SELECT e.emp_name,
       e.emp_id,
	   d.dept_name
FROM Employee2 e
LEFT JOIN Department4 d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

SELECT d.dept_id,
        d.dept_name
FROM Department4 d
LEFT JOIN Employee2 e
ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

SELECT e.emp_name,
       e.salary,
       d.dept_name
FROM Employee2 e
INNER JOIN Department4 d
ON e.dept_id = d.dept_id
WHERE d.dept_name = "IT";

SELECT e.emp_name,
       e.salary,
       d.dept_name
FROM Employee2 e
INNER JOIN Department4 d
ON e.dept_id = d.dept_id
WHERE e.salary > 50000
ORDER BY e.salary DESC;

SELECT e.emp_name,
       e.salary,
       d.dept_name
FROM Employee2 e
INNER JOIN Department4 d
ON e.dept_id = d.dept_id
WHERE e.salary BETWEEN 50000 AND 80000;

SELECT d.dept_name,
       COUNT(e.emp_id) AS employee_count
FROM Department4 d
LEFT JOIN Employee2 e
ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY d.dept_id;

SELECT d.dept_name,
       COUNT(e.emp_id) AS employee_count
FROM Department4 d
INNER JOIN Employee2 e
ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) > 1;