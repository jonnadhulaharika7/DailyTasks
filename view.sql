CREATE TABLE employees2 (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees2 VALUES
(1,'John','HR',40000),
(2,'Alice','IT',70000),
(3,'Bob','IT',80000),
(4,'David','Sales',50000),
(5,'Eva','HR',60000),
(6,'Grace','IT',90000),
(7,'Sam','Sales',45000);
SELECT * FROM employees2;

1.Create a view to display all employee details.
CREATE VIEW emply_view AS
SELECT * 
FROM employees2;
SELECT *
FROM emply_view;

2.Create a view showing only employee name and salary.
CREATE VIEW employeessalary AS
SELECT emp_name,
       salary
FROM employees2;
SELECT *
FROM employeessalary;

3.Create a view displaying only IT employees.
CREATE VIEW ITEmployees AS
SELECT *
FROM employees2
WHERE department = 'IT';
SELECT *
FROM ITEmployees;

4.Create a view showing employees earning more than ₹60,000.
CREATE VIEW high_salary AS
SELECT *
FROM employees2
WHERE salary > 60000;
SELECT *
FROM high_salary;

5.Create a view displaying HR employees.
CREATE VIEW HRemployees AS
SELECT *
FROM employees2
WHERE department = 'HR';
SELECT *
FROM HRemployees;

6.Create a view with renamed columns.
CREATE VIEW employeedetails AS
SELECT 
emp_name AS employee_name,
salary AS employee_salary
FROM employees2;
SELECT *
FROM employeedetails;

7.Display all records from HighSalaryEmployees view.
CREATE VIEW highsalaryemployees AS
SELECT *
FROM employees2
WHERE salary > 60000;
SELECT *
FROM highsalaryemployees;

8.Drop the HREmployees view.
DROP VIEW HRemployees;

9.Replace an existing view to include the department column.
CREATE OR REPLACE VIEW EmployeeSalary AS
SELECT
emp_name,
department,
salary
FROM employees2;
SELECT *
FROM EmployeeSalary;

10.Create a view showing employees earning more than ₹50,000 and display them in descending salary order.
CREATE VIEW highsalary AS
SELECT
emp_name,
salary,
department
FROM employees2
WHERE salary > 50000
ORDER BY salary DESC;
SELECT *
FROM highsalary;

11.Create a view containing only Sales employees ordered by employee name.
CREATE VIEW salesemployees AS
SELECT emp_name,
       salary
FROM employees2
WHERE department = 'Sales'
ORDER BY emp_name;
SELECT *
FROM salesemployees;

12.Create a view showing employees with salary between ₹50,000 and ₹80,000.
CREATE VIEW empsalary AS
SELECT emp_name,
       salary
FROM employees2
WHERE salary BETWEEN 50000 AND 80000;
SELECT *
FROM empsalary;

13.Create a view showing employees whose names start with 'A'.
CREATE VIEW empnames AS
SELECT emp_name
FROM employees2
WHERE emp_name LIKE 'A%';
SELECT *
FROM empnames;

14.Create a view displaying employees whose department is HR or IT.
CREATE VIEW empdepartment AS
SELECT emp_name,
       salary,
	   department
FROM employees2
WHERE department IN('HR' , 'IT');
SELECT *
FROM empdepartment;

15.Create a view displaying the Top 3 highest-paid employees.
CREATE VIEW top3highestpaid AS
SELECT emp_name,
       salary
FROM employees2
ORDER BY salary DESC
LIMIT 3;
SELECT *
FROM top3highestpaid;

16.Create a view displaying employees earning less than the company average salary.
CREATE VIEW lowsalary AS
SELECT emp_name,
       salary
FROM employees2
WHERE salary < (SELECT AVG(salary) FROM employees2);
SELECT *
FROM lowsalary;

17.Create a view displaying employees earning above the company average salary.
CREATE VIEW aboveaveragesalary AS
SELECT emp_name,
       salary
FROM employees2
WHERE salary > (SELECT AVG(salary) FROM employees2);
SELECT *
FROM aboveaveragesalary;

18.Create a view displaying employees with the highest salary.
CREATE VIEW highestsalary AS
SELECT emp_name,
       salary
FROM employees2
WHERE salary  = (SELECT MAX(salary) FROM employees2);
SELECT *
FROM highestsalary;

19.Create a view displaying employees with the minimum salary.
CREATE VIEW lowestsalary AS
SELECT emp_name,
       salary
FROM employees2
WHERE salary  = (SELECT MIN(salary) FROM employees2);
SELECT *
FROM lowestsalary;
