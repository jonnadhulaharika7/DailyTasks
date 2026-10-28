CREATE TABLE Employee(
emp_id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(30),
salary DECIMAL(10,2)
);

ALTER TABLE employee
ADD email VARCHAR(100);

ALTER TABLE employee
DROP COLUMN email;

RENAME TABLE Employee TO staff;

RENAME TABLE staff to Employee;

INSERT INTO Employee(emp_id, 
					 name, 
                     department, 
                     salary)
VALUES(101, "Haru", "IT", 80000),
	  (102, "Hanu", "HR", 90000);
SELECT * FROM Employee;

UPDATE Employee
SET salary = 70000
WHERE emp_id = 101;

UPDATE Employee
SET name = "Tara"
WHERE emp_id = 101;

DELETE FROM Employee
WHERE emp_id = 102;

INSERT INTO Employee(emp_id, name, department, salary)
VALUES(102, "Hanu", "HR", 50000);

SELECT * FROM Employee;
SELECT name, salary FROM Employee;
SELECT * FROM Employee WHERE salary > 50000;

GRANT SELECT
ON company_db.Employee
TO 'analyst'@'localhost';

GRANT SELECT, INSERT
ON company_db.Employee
TO 'analyst'@'localhost';

REVOKE INSERT 
ON company_db.Employee
FROM 'analyst'@'localhost';

START TRANSACTION;
UPDATE Employee
SET salary = 70000
WHERE emp_id = 101;
COMMIT;

START TRANSACTION;
UPDATE Employee
SET salary = 80000
WHERE emp_id = 101;
ROLLBACK;

START TRANSACTION;
UPDATE Employee
SET salary = 70000
WHERE emp_id = 101;
SAVEPOINT sp1;
UPDATE Employee
SET salary = 90000
WHERE emp_id = 102;
ROLLBACK TO SAVEPOINT sp1;
COMMIT;