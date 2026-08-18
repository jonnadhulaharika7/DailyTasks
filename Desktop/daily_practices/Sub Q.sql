CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    salary INT,
    manager_id INT
);

SELECT * FROM employees;

INSERT INTO employees VALUES
(101,'Alice','HR',50000,NULL),
(102,'Bob','IT',70000,101),
(103,'Charlie','Finance',60000,101),
(104,'David','IT',80000,102),
(105,'Eva','HR',55000,101),
(106,'Frank','Finance',75000,103),
(107,'Grace','IT',90000,102),
(108,'Helen','Marketing',65000,101);


LEVEL 1 (Single Row Subqueries)
Question 1
Find the employee who earns the highest salary.
SELECT * 
FROM employees
WHERE salary = (
             SELECT MAX(salary)
			 FROM employees
);

Question 2
Find the employee who earns the lowest salary.
SELECT * 
FROM employees
WHERE salary = (
        SELECT MIN(salary)
        FROM employees
);

Question 3
Find employees earning more than the average salary.
SELECT *
FROM employees
WHERE salary > (
              SELECT AVG(salary)
              FROM employees
);

Question 4
Find employees earning less than the average salary.
SELECT *
FROM employees
WHERE salary < (
            SELECT AVG(salary)
			FROM employees
);

LEVEL 2 (Multiple Row Subqueries)
Question 5
Find employees who work in departments where salary is greater than 80000.
SELECT * 
FROM employees
WHERE department IN (
                    SELECT department
				   FROM employees
				   WHERE salary > 80000
);

Question 6
Find employees whose manager is Alice
SELECT * 
FROM employees
WHERE manager_id = (
                  SELECT emp_id
                  FROM employees
				  WHERE emp_name = 'Alice'
);

Question 7
Find employees whose salary is equal to any HR employee's salary.
SELECT *
FROM employees
WHERE salary IN(
                 SELECT salary
                 FROM employees
                 WHERE department = 'HR'
);

Question 8
Find employees who are not in the HR department.
SELECT * 
FROM employees
WHERE emp_id NOT IN(
               SELECT emp_id
               FROM employees
               WHERE department = 'HR'
);

Question 9
Find employees earning more than ANY HR employee.
SELECT * 
FROM employees
WHERE salary > ANY(
               SELECT salary 
               FROM employees
               WHERE department = 'HR'
);

Question 10
Find employees earning more than ALL HR employees.
SELECT * 
FROM employees
WHERE salary > ALL(
               SELECT salary
               FROM employees
               WHERE department = 'HR'
);

Question 11
Find departments that have at least one employee earning more than 80,000.
SELECT DISTINCT department
FROM employees e1
WHERE EXISTS (
           SELECT *
		   FROM employees e2
		   WHERE e1.department = e2.department
		   AND salary > 80000
);

Question 12
Find employees earning more than the average salary of their department.
SELECT *
FROM employees e1
WHERE salary > (
            SELECT AVG(salary)
            FROM employees e2
            WHERE e1.department = e2.department
);

Question 13
Find employees having the highest salary in their department.
SELECT *
FROM employees e1
WHERE salary = (
         SELECT max(salary)
		 FROM employees e2
		 WHERE e1.department = e2.department
);

Question 14
Find employees having the minimum salary in their department.
SELECT *
FROM employees e1
WHERE salary = (
             SELECT MIN(salary)
			 FROM employees e2
			 WHERE e1.department = e2.department
);

Question 15
Find employees who manage at least one employee.
SELECT *
FROM employees e1
WHERE EXISTS (
            SELECT *
			FROM employees e2
			WHERE e1.emp_id = e2.manager_id
);


Question 16
Find employees earning more than their manager.
SELECT * 
FROM employees e1
WHERE salary > (
             SELECT salary 
			 FROM employees e2
			 WHERE e1.manager_id = e2.emp_id
);

Question 17
Find employees who work in the department of the highest-paid employee.
SELECT *
FROM employees
WHERE department = 
(
              SELECT department
              FROM employees
              WHERE salary = 
			  (
                    SELECT MAX(salary)
                    FROM employees
			  )
);

Question 18
Find employees who earn the second-highest salary.
SELECT *
FROM employees
WHERE salary = 
( 
              SELECT MAX(salary)
			  FROM employees
			  WHERE salary <
			  ( 
			        SELECT MAX(salary)
					FROM employees
			  )
);

Question 19
Find employees who work in the same department as the lowest-paid employee.
SELECT *
FROM employees
WHERE department =
(
              SELECT department
              FROM employees
              WHERE salary = 
              (
                    SELECT MIN(salary)
                    FROM employees
			   )
);

Question 20
Find employees whose salary is greater than the salary of the lowest-paid IT employee.
SELECT *
FROM employees
WHERE salary >
(
             SELECT MIN(salary)
             FROM employees
             WHERE department = 'IT'
);

Question 21
Find employees who earn more than the minimum salary in the department of Grace.
SELECT *
FROM employees
WHERE salary <
(
              SELECT MIN(salary)
              FROM employees
              WHERE department = 
			  (
                      SELECT department
                      FROM employees
                      WHERE emp_name = 'Grace'
			   )
);