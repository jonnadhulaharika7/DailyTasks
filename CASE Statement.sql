CREATE TABLE employees1 (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(20),
    salary INT
);

INSERT INTO employees1 VALUES
(1,'John','HR',40000),
(2,'Alice','IT',70000),
(3,'Bob','IT',80000),
(4,'David','Sales',50000),
(5,'Eva','HR',60000),
(6,'Grace','IT',90000),
(7,'Sam','Sales',45000);
SELECT * FROM employees1;

1.Display employee names and classify salaries as
High Salary (>70000)
Medium Salary (50000–70000)
Low Salary (<50000)

SELECT 
emp_name,
salary,
CASE
WHEN salary > 70000 THEN 'High salary'
WHEN salary >= 50000 THEN 'Medium salary'
ELSE 'Low salary'
END AS salary_category
FROM employees1;

2.Replace department names

HR
↓
Human Resources

IT
↓
Information Technology

Sales
↓
Sales Department
SELECT emp_name,
CASE
WHEN department = 'HR'
THEN 'Human Resources'
WHEN department = 'IT'
THEN 'Information Technology'
WHEN department = 'Sales'
THEN 'Sales Department'
END AS department_name
FROM employees1;

3.Display Bonus Eligibility
Salary
Greater than or equal to
60000
Eligible
Else
Not Eligible
SELECT emp_name,
       salary,
CASE
WHEN salary >= 60000
THEN 'Eligible'
ELSE 'Not Eligible'
END AS Bonus
FROM employees1;

4.Classify employees
Excellent
Good
Average
Poor
SELECT emp_name,
       salary,
CASE
WHEN salary > 80000
THEN 'Excellent'
WHEN salary >= 70000
THEN 'Good'
WHEN salary >= 50000
THEN 'Average'
ELSE 'Poor'
END AS performance
FROM employees1;

5.Display employee remarks
Salary above
75000
Outstanding
Salary above
60000
Excellent
Salary above
50000
Good
Else
Needs Improvement
SELECT emp_name,
       salary,
CASE
WHEN salary > 75000
THEN 'Outstanding'
WHEN salary > 60000
THEN 'Excellent'
WHEN salary > 50000
THEN 'Good'
ELSE 'Need Improvement'
END AS remarks
FROM employees1;

6.Count employees earning above ₹60,000.
SELECT SUM (
CASE
WHEN salary > 60000
THEN 1
ELSE 0
END ) AS total_high_salary
FROM employees1;

7.Count employees earning below ₹60,000.
SELECT SUM(
CASE
WHEN salary < 60000
THEN 1
ELSE 0
END ) AS total_low_salary
FROM employees1;

8.Department-wise count of employees earning above ₹60,000.
SELECT department,
SUM(
CASE 
WHEN salary > 60000
THEN 1
ELSE 0
END ) AS high_salary
FROM employees1
GROUP BY department;

9.Total salary of employees earning above ₹60,000.
SELECT SUM(
CASE 
WHEN salary > 60000
THEN salary
ELSE 0
END ) AS total_salary
FROM employees1;

10.Average salary of employees earning above ₹50,000.
SELECT AVG(
CASE
WHEN salary > 50000
THEN salary
END ) AS average_salary
FROM employees1;

11.Find the department-wise total salary, but include only employees earning above ₹50,000.
SELECT department,
SUM (
CASE
WHEN salary > 50000
THEN salary
ELSE 0
END ) AS total_salary
FROM employees1
GROUP BY department;

12.Count employees in each salary category.
Categories
High (>70000)
Medium (50000–70000)
Low (<50000)
SELECT
CASE
WHEN salary > 70000
THEN 'High'
WHEN salary >= 50000
THEN 'Medium'
ELSE 'Low'
END AS salary_category,
COUNT(*) AS total
FROM employees1
GROUP BY
CASE
WHEN salary > 70000
THEN 'High'
WHEN salary >= 50000
THEN 'Medium'
ELSE 'Low'
END;

13.Display employees ordered by salary category.
SELECT emp_name,
       salary,
CASE
WHEN salary > 80000
THEN 1
WHEN salary >= 60000
THEN 2
ELSE 3
END AS salary_category
FROM employees1;

14.Display departments in this order:
IT
↓
HR
↓
Sales
instead of alphabetical order.
SELECT *
FROM employees1
ORDER BY
CASE
WHEN department = 'IT' THEN 1
WHEN department = 'HR' THEN 2
WHEN department = 'Sales' THEN 3
END;


15.Display employees with custom priority:
IT
↓
HR
↓
Sales
Within each department, show the highest salary first.
SELECT emp_name,
       salary,
	   department
FROM employees1
ORDER BY
CASE
WHEN department = 'IT'
THEN 1
WHEN department = 'HR'
THEN 2
WHEN department = 'Sales'
THEN 3
END,
salary DESC;

16.Display only High Salary employees using CASE.
SELECT emp_name,
       salary
FROM employees1
WHERE
CASE
WHEN salary > 70000 THEN 'High'
ELSE 'Low'
END = 'High'
