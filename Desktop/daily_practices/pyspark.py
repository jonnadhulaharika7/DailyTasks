data = [
    (1, "Harika", "Data Engineering", 70000, "Hyderabad", "Female", 3),
    (2, "Rahul", "Data Engineering", 85000, "Bangalore", "Male", 5),
    (3, "Priya", "HR", 50000, "Hyderabad", "Female", 2),
    (4, "Arjun", "Data Engineering", 90000, "Chennai", "Male", 6),
    (5, "Sneha", "Finance", 65000, "Bangalore", "Female", 4),
    (6, "Kiran", "HR", 55000, "Chennai", "Male", 3),
    (7, "Anjali", "Finance", 75000, "Hyderabad", "Female", 5),
    (8, "Vijay", "Data Engineering", 80000, "Bangalore", "Male", 4),
    (9, "Neha", "HR", 60000, "Hyderabad", "Female", 3),
    (10, "Ravi", "Finance", 70000, "Chennai", "Male", 2)
]

columns = [
    "emp_id",
    "name",
    "department",
    "salary",
    "city",
    "gender",
    "experience"
]

df = spark.createDataFrame(data, columns)

df.show()
%md
MEMBERSHIP OPERATORS
# Find employees who belong to Hyderabad.
from pyspark.sql.functions import col
df.filter(col("city").isin(["Hyderabad"])).show()
# Find employees who belong to Hyderabad or Bangalore
df.filter(col("city").isin(["Hyderabad","Banglore"])).show()
# Find employees who are NOT from Hyderabad
df.filter(~col("city").isin(["Hyderabad"])).show()
# Find employees who work in Data Engineering or Finance
df.filter(col("department").isin(["Data Engineering","Finance"])).show()
# Find employees who are not from HR or Finance.
df.filter(~col("department").isin("HR","Finance")).show()
# Find employees whose city is either Hyderabad, Bangalore, or Chennai
df.filter(col("city").isin(["Hyderabad","Banglore","Chennai"])).show()
%md
LOGICAL OPERATORS
# Find employees with salary greater than 70000 AND experience greater than 4.
df.filter((col("salary") > 70000) & (col("experience") > 4)).show()
# Find employees from Hyderabad OR Chennai.
df.filter((col("city") == "Hyderabad") | (col("city") == "Banglore")).show()
# Find female employees with salary greater than 60000
df.filter((col("gender") == "Female") & (col("salary") > 60000)).show()
# Find Data Engineering employees with experience greater than 4.
df.filter((col("department") == "Data Engineering") & (col("experience") > 4)).show()
# Find employees who are either from Hyderabad with salary > 60000 OR from Bangalore with salary > 70000.
df.filter(((col("city") == "Hyderbad") | (col("salary") > 60000)) | ((col("city") == "Bangalore") & (col("salary") > 70000))).display()
df.filter(((col("city") == "Hyderbad") & (col("salary") > 60000)) | ((col("city") == "Bangalore") & (col("salary") > 70000))).show()
# Find employees who are NOT from Chennai.
df.filter(col("city") != "Chennai").show()
%md
WHERE() IS ANOTHER FORM OF FILTER()
# Find employees whose salary is greater than 70000.
df.where(col("salary") > 70000).show()
# Find employees from HR.
df.where(col("department") == "HR").show()
# Find employees from Hyderabad with salary greater than 60000
df.where((col("city") == "Hyderabad") & (col("salary") > 60000)).show()

# . Find employees whose experience is between 3 and 5.
df.where((col("experience") >= 3) & (col("experience") <= 5)).show()
# Use a SQL-style condition with where().
df.where("salary > 70000 AND experience > 4").show()