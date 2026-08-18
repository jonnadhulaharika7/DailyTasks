employees = [
    (1, "Harika", 101, 70000),
    (2, "Rahul", 102, 85000),
    (3, "Priya", 103, 50000),
    (4, "Arjun", 101, 90000),
    (5, "Sneha", 104, 65000),
    (6, "Kiran", 105, 55000)
]

emp_columns = [
    "emp_id",
    "name",
    "dept_id",
    "salary"
]

emp_df = spark.createDataFrame(employees, emp_columns)

emp_df.show()

# COMMAND ----------

departments = [
    (101, "Data Engineering", "Hyderabad"),
    (102, "Data Science", "Bangalore"),
    (103, "HR", "Chennai"),
    (104, "Finance", "Hyderabad"),
    (106, "Marketing", "Mumbai")
]

dept_columns = [
    "dept_id",
    "department",
    "location"
]

dept_df = spark.createDataFrame(departments, dept_columns)

dept_df.show()

# COMMAND ----------

# Perform an inner join between employees and departments using dept_id.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner")
result.show()

# COMMAND ----------

# Display employee name and department name after the inner join.
emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner")
.select(emp_df.name,dept_df.department).show()

# COMMAND ----------

# Display employee name, salary, department and location.
emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").select(emp_df.name,emp_df.salary,dept_df.department,dept_df.location).show()

# COMMAND ----------

# Perform a left join.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"left").result.show()

# COMMAND ----------

# Find employees who don't have a matching department.
result =  emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"left")result.filter(dept_df.dept_id.isNull()).show()

# COMMAND ----------

# Perform a right join.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"right")result.show()

# COMMAND ----------

# Find departments that don't have employees.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"right")result.filter(emp_df.emp_id.isNull()).show()

# COMMAND ----------

# Perform a full outer join.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"full")result.show()

# COMMAND ----------

# Find employees who have a matching department.
result = emp_df.join(dep_df,emp_df.dept_id == dept_df.dept_id,"left_semi")result.show()


# COMMAND ----------

# Find employees whose department exists in the department table and salary > 60000.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"left_semi")result.filter(col("salary") > 60000).show()

# COMMAND ----------

# Find employees whose department doesn't exist.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"left_anti")result.show()

# COMMAND ----------

# Find departments that don't have employees.
result = dept_df.join(emp_df,dept_df.dept_id == dept_id,"left_anti")result.show()

# COMMAND ----------

# Join Using Same Column Name
result = emp_df.join(dept_df,"dept_id","inner")result.show()

# COMMAND ----------

# After joining, select only required columns
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").select(emp_df.emp_id,emp_df.name,emp_df.salary,dept_df.department,dept_df.location)result.show()

# COMMAND ----------

# Join + Filter
#  Find Data Engineering employees.
result = emp_df.join(dept_df,emp_df.dept_df == dept_df.dept_id,"inner").filter(col("department") == "DataEngineering")result.show()

# COMMAND ----------

# Find employees earning more than 70000 and display their department.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").filter(col("salary") > 70000).select("name","salary","department")result.show()

# COMMAND ----------

# Join + GroupBy
#  Find the number of employees in each department.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").groupBy("department").count()result.show()

# COMMAND ----------

# Find the average salary of each department.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").groupBy("department").agg(avg("salary").alias("average_salary"))result.show()

# COMMAND ----------

# Find the maximum salary in each department
result = emp_df.join(dept_df,emp_df.dept_id == dept_id,"inner").groupBy("department").agg(max("salary").alias("max_salary"))result.show()

# COMMAND ----------

# Join + Window Function
# Rank employees based on salary within each department.
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").withcolumn("rank",row_number().over(window_spec))result.show()

# COMMAND ----------

# Find the highest-paid employee in each department.
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").withColumn("rank",row_number().over(window_spec)).filter(col("rank") == 1)result.show()

# COMMAND ----------

# Find employees who don't have a department.
emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"left_anti").show()

# COMMAND ----------

# Find departments that don't have employees.
dept_df.join(emp_df,dept_df.dept_id == emp_df.dept_id,"left_anti").show()

# COMMAND ----------

# Find employees working in Hyderabad.
emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").filter(col("location") == "Hyderabad").show()

# COMMAND ----------

# Find employees in Data Engineering earning more than 75000.
emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").filter(col("department") == "DataEngineering") & (col("salary") > 75000).show()

# COMMAND ----------

# Find the department with the highest average salary.
result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").groupBy("department").agg(avg("salary").alias("avg_salary")).orderBy(col("avg_salary").desc()).limit(1)result.show()

# COMMAND ----------

# Find the top 2 highest-paid employees in each department.
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())result = emp_df.join(dept_df,emp_df.dept_id == dept_df.dept_id,"inner").withColumn("rank",row_number().over(window_spec)).filter(col("rank") <= 2)result.show()

# COMMAND ----------

