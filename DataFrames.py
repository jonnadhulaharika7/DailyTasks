# COMMAND ----------

# Find the maximum salary in each department.
from pyspark.sql import functions as F
df.groupBy("department").agg(F.max("salary")).show()

# COMMAND ----------

# Find the minimum salary in each department.
from pyspark.sql import functions as F
df.groupBy("department").agg(F.min("salary").alias("min_salary")).display()

# COMMAND ----------

# Find the total salary paid to each department.
from pyspark.sql import functions as F
df.groupBy("department").agg(F.sum("salary").alias("sum_salary")).show()

# COMMAND ----------

# Find employee count and average salary department-wise.
from pyspark.sql import functions as F
df.groupBy("department").agg(F.count("emp_id").alias("employee_count"),F.avg("salary").alias("average_salary")).show()

# COMMAND ----------

# Find the average salary for each city.
from pyspark.sql import functions as F
df.groupBy("city").agg(F.avg("salary").alias("average_salary")).show()

# COMMAND ----------

# Find the maximum salary for each city.
from pyspark.sql import functions as F
df.groupBy("city").agg(F.max("salary").alias("maximum_salary")).show()

# COMMAND ----------

# Find departments having more than 2 employees.
from pyspark.sql import functions as F
df.groupBy("department").agg(F.count("emp_id").alias("employee_count")).filter(F.col("employee_count") > 2).show()

# COMMAND ----------

# Find departments where the average salary is greater than 70000.
from pyspark.sql import functions as F
df.groupBy("department").agg(F.avg("salary").alias("average_salary")).filter(F.col("average_salary") > 70000).show()

# COMMAND ----------

# MAGIC %md
# MAGIC STRING METHODS

# COMMAND ----------

# Convert employee names to uppercase.
from pyspark.sql import functions as F
df.select("name",F.upper("name").alias("upper_name")).show()

# COMMAND ----------

# Convert employee names to lowercase.
from pyspark.sql import functions as F
df.select("name",F.lower("name").alias("lower_name")).show()

# COMMAND ----------

# Find the length of each employee's name.
from pyspark.sql import functions as F
df.select("name",F.length("name").alias("name_length")).show()

# COMMAND ----------

# Find employees whose name starts with A.
from pyspark.sql import functions as F
df.filter(F.col("name").startswith("A")).show()

# COMMAND ----------

# Find employees whose name ends with a.
from pyspark.sql import functions as F
df.filter(F.col("name").endswith("a")).show()

# COMMAND ----------

# Find employees whose name contains i.
from pyspark.sql import functions as F
df.filter(F.col("name").contains("i")).show()

# COMMAND ----------

# Extract the first 3 characters of each name.
from pyspark.sql.functions import substring
df.select("name",substring("name",1,3).alias("first_3_characters")).show()

# COMMAND ----------

# Combine name and city.
from pyspark.sql import functions as F
df.select(F.concat_ws("-","name","city").alias("employee_details")).show()

# COMMAND ----------

# Combine name, department and city.
from pyspark.sql import functions as F
df.select(F.concat_ws("|","name","department","city").alias("employee_details")).show()

# COMMAND ----------

# Replace Data Engineering with DE.
from pyspark.sql import functions as F
df.select(F.regexp_replace("department","Data Engineering","DE").alias("department")).show()


# COMMAND ----------

# DBTITLE 1,Cell 44
# Give a row number to all employees based on salary
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number

window_spec = Window.orderBy(col("salary").desc())
df.withColumn("row_number", row_number().over(window_spec)).show()

# COMMAND ----------

# Give a row number separately for each department.
from pyspark.sql.window import Window
from pyspark.sql.functions import col,row_number
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("row_number",row_number().over(window_spec)).show()

# COMMAND ----------

# Rank employees according to salary.
from pyspark.sql.window import Window
from pyspark.sql.functions import col,rank
window_spec = Window.orderBy(col("salary").desc())
df.withColumn("rank",rank().over(window_spec)).show()

# COMMAND ----------

#  Rank employees separately within each department.
from pyspark.sql.window import Window
from pyspark.sql.functions import col,rank
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("rank",rank().over(window_spec)).show()

# COMMAND ----------

# Find the highest-paid employee in each department
from pyspark.sql.window import Window
from pyspark.sql.functions import col,rank
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
result = df.withColumn("rank",row_number().over(window_spec))
result.filter(col("rank") == 1).show()


# COMMAND ----------

# Find the top 2 employees from each department.
from pyspark.sql.window import Window
from pyspark.sql.functions import col,rank
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
result = df.withColumn("rank",row_number().over(window_spec))
result.filter(col("rank") <= 2).show()

# COMMAND ----------

# Find department average salary beside every employee.
from pyspark.sql.window import Window
from pyspark.sql.functions import col, rank, avg
window_spec = Window.partitionBy("department")
df.withColumn("department_avg_salary",avg("salary").over(window_spec)).show()

# COMMAND ----------

# Find the previous employee's salary within each department.
from pyspark.sql.window import Window
from pyspark.sql.functions import col, lag
window_spec = Window.partitionBy("department").orderBy(col("salary"))
df.withColumn("previous_salary",lag("salary").over(window_spec)).show()

# COMMAND ----------

# Find the next employee's salary within each department.
from pyspark.sql.window import Window
from pyspark.sql.functions import col, lead
window_spec = Window.partitionBy("department").orderBy(col("salary"))
df.withColumn("next_salary",lead("salary").over(window_spec)).show()