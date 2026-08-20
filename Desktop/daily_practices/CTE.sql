CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(20),
    salary INT
);

INSERT INTO employees VALUES
(1,'John','HR',40000),
(2,'Alice','IT',70000),
(3,'Bob','IT',80000),
(4,'David','Sales',50000),
(5,'Eva','HR',60000),
(6,'Grace','IT',90000),
(7,'Sam','Sales',45000);
SELECT * FROM employees;

1.Create a CTE that displays all employee details.
WITH employeedata AS
(
     SELECT *
	 FROM employees
)  
     SELECT *
	 FROM employeedata;

2.Display only IT employees using a CTE.
WITH ITemployees AS
(
     SELECT *
	 FROM employees
	 WHERE department = 'IT'
)
     SELECT *
	 FROM ITemployees;

3.Display employees whose salary is greater than 50,000.
WITH highsalary AS
( 
     SELECT *
	 FROM employees
	 WHERE salary > 50000
) 
     SELECT *
	 FROM highsalary;

4.Display only employee name and salary using a CTE.
WITH employeessalary AS
(
      SELECT emp_name,
	         salary
	  FROM employees
)
      SELECT *
	  FROM employeessalary;

5.Display employees from the HR department.
WITH HRemployees AS
( 
     SELECT *
	 FROM employees
	 WHERE department = 'HR'
)
     SELECT *
	 FROM HRemployees;

6.Display employees whose salary is less than 60,000 using a CTE.
WITH lowsalary AS
(
     SELECT * 
	 FROM employees
	 WHERE salary < 60000
)
     SELECT * 
	 FROM lowsalary;

7.Display employees whose names start with 'A'.
WITH namestart AS
(
     SELECT *
	 FROM employees
	 WHERE emp_name LIKE 'A%'
)
     SELECT *
	 FROM namestart;

8.Display all Sales employees using a CTE.
WITH salesemployees AS
(
     SELECT *
	 FROM employees
	 WHERE department = 'Sales'
)
     SELECT *
	 FROM salesemployees;

9.Display employee names and salaries of employees earning between 50,000 and 80,000.
WITH employeesearning AS
( 
       SELECT emp_name,
	          salary
	   FROM employees
	   WHERE salary BETWEEN 50000 AND 80000
) 
       SELECT * 
	   FROM employeesearning;

10.Display employees whose department is either HR or IT using a CTE.
WITH employeesdepartment AS
( 
      SELECT *
	  FROM employees
	  WHERE department IN ('HR','IT')
)
      SELECT *
	  FROM employeesdepartment;

11.Find the average salary of all employees using a CTE.
WITH avgsalary AS
( 
     SELECT AVG(salary)
	 FROM employees
)
     SELECT *
	 FROM avgsalary;

12.Find the maximum salary using a CTE.
WITH highsalary AS
( 
      SELECT MAX(salary)
	  FROM employees
)
      SELECT * 
      FROM highsalary;

13.Find the minimum salary using a CTE.
WITH lowsalary AS
( 
      SELECT MIN(salary)
	  FROM employees
)
      SELECT * 
      FROM lowsalary;

14,Find the total salary paid to all employees.
WITH totalsalary AS
( 
      SELECT SUM(salary)
	  FROM employees
)
      SELECT *
	  FROM totalsalary;

15.Find the total number of employees using a CTE.
WITH employeecount AS
( 
     SELECT COUNT(*) AS total_employees
	 FROM employees
)
     SELECT *
	 FROM employeecount;

16.Find the average salary of only IT employees.
WITH averagesalary AS
(
     SELECT AVG(salary)
	 FROM employees
	 WHERE department = 'IT'
)
     SELECT *
	 FROM averagesalary;

17.Find the maximum salary in the HR department.
WITH highsalary AS
(
     SELECT MAX(salary)
	 FROM employees
	 WHERE department = 'HR'
)
     SELECT *
	 FROM highsalary

18.Display employees earning more than the company average salary.
WITH avgsalary AS
( 
     SELECT AVG(salary) AS avg_salary
	 FROM employees
)
     SELECT e.emp_name,
	        e.salary
	 FROM employees e
	 JOIN avgsalary a
	 ON e.salary > a.avg_salary;

WITH avgsalary AS
( 
     SELECT AVG(salary) AS avg_salary
	 FROM employees
)
     SELECT emp_name, 
	        salary
	 FROM employees
	 JOIN avgsalary
	 ON salary > avg_salary;

19.Display employees earning more than the company average salary.
WITH lowsalary AS
(
     SELECT AVG (salary) AS min_salary
	 FROM employees
)
     SELECT emp_name,
	        salary
	 FROM employees
	 JOIN lowsalary
	 ON salary < min_salary;

20.Display employee having the highest salary.
WITH highsalary AS
(
     SELECT MAX(salary) highest_salary
	 FROM employees
)
     SELECT emp_name,
	        salary
	 FROM employees
	 JOIN highsalary
	 ON salary = highest_salary

21.Display employee having minimum salary.
WITH lowsalary AS
(
     SELECT MIN(salary) AS lowest_salary
	 FROM employees
)
     SELECT e.emp_name,
	        e.salary
	 FROM employees e
	 JOIN lowsalary l
	 ON e.salary = l.lowest_salary;

***22.Display employees earning more than their department average salary.--- MOST ASKED INTERVIEW Q
WITH deptaverage AS
(
      SELECT department,
	  AVG(salary)AS avg_salary 
	  FROM employees
	  GROUP BY department
)
      SELECT e.emp_name,
	         e.salary,
			 e.department,
			 d.avg_salary
	  FROM employees e
	  JOIN deptaverage d
	  ON e.department = d.department
	  WHERE e.salary > d.avg_salary
	  
23.Display employees earning below their department average salary.
WITH deptavgsalary AS
(
     SELECT department,
	 AVG(salary) AS average_salary
	 FROM employees
	 GROUP BY department
)
     SELECT e.emp_name,
	        e.salary,
			e.department,
			d.average_salary
	 FROM employees e
	 JOIN deptavgsalary d
	 ON e.department = d.department
	 WHERE e.salary < d.average_salary;
	 
24.Display the highest-paid employee from every department.
WITH highestpaidemployee AS
( 
     SELECT department,
	 MAX(salary) high_salary
	 FROM employees
	 GROUP BY department
)
     SELECT e.emp_name,
	        e.salary,
			e.department,
			d.high_salary
	FROM employees e
	JOIN highestpaidemployee d
	ON e.department = d.department
	WHERE e.salary = d.high_salary;
	
25.Display lowest-paid employee from every department.
WITH lowsalary AS
(
     SELECT department,
	 MIN(salary) AS lowest_salary
	 FROM employees
	 GROUP BY department
)
     SELECT e.emp_name,
	        e.salary,
			d.lowest_salary,
			e.department
	FROM employees e
	JOIN lowsalary d
	ON e.department = d.department
	WHERE e.salary  = d.lowest_salary;
			
26.Create one CTE for IT employees.
Create another CTE for employees earning more than 70,000.
Display employees common to both.
WITH ITemployees AS
(
     SELECT *
	 FROM employees
	 WHERE department = 'IT'
),
highsalary AS
(
     SELECT *
	 FROM ITemployees
	 WHERE salary > 70000
)
     SELECT *
	 FROM highsalary;
    
27.Create One CTE HR Employees
Second CTE  Salary below 50000
Display common employees.
WITH HRemployees AS
(
     SELECT *
	 FROM employees
	 WHERE department = 'HR'
),
lowsalary AS
(
     SELECT *
	 FROM HRemployees
	 WHERE salary < 50000
)
     SELECT *
	 FROM lowsalary;

28.Find the second highest salary.
WITH secondhighsalary AS
(
    SELECT  emp_name,
	        salary,
	        ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
	FROM employees
)
    SELECT *
	FROM secondhighsalary
	WHERE rn = 2;

29.Find the third highest salary.
WITH thirdhighestsalary AS
(
     SELECT emp_name,
	        salary,
			ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
	 FROM employees
)
     SELECT *
	 FROM thirdhighestsalary
	 WHERE rn = 3;

30.Display Top 3 highest-paid employees.
WITH thirdpaid AS
(
     SELECT emp_name,
	        salary,
			ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
	 FROM employees
)
     SELECT *
	 FROM thirdpaid
	 WHERE rn <= 3;

31.Display employees ranked by salary.
WITH ranksalary AS
(
     SELECT emp_name,
	        salary,
			ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
	 FROM employees
)
     SELECT *
	 FROM ranksalary;

32.Rank employees within each department.
WITH departmentemp AS
(
    SELECT department,
	       emp_name,
		   salary,
	       ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS rn
	FROM employees
)
    SELECT *
	FROM departmentemp;
	
33.Display the highest-paid employee from each department using ROW_NUMBER().
WITH highestpaid AS
(
     SELECT emp_name,
	        salary,
			department,
			ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS  rn
	 FROM employees
)
     SELECT *
	 FROM highestpaid
	 WHERE rn = 1;

34.Find the 4th highest salary using a CTE.
WITH highestsalary AS
(
     SELECT emp_name,
	        salary,
			department,
			ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS  rn
	 FROM employees
)
     SELECT *
	 FROM highestsalary
	 WHERE rn = 4;

35.Find the 5th highest salary.
WITH highestsalary AS
(
     SELECT emp_name,
	        salary,
			department,
			ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS  rn
	 FROM employees
)
     SELECT *
	 FROM highestsalary
	 WHERE rn = 5;
