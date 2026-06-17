from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("EmployeeRDDProcessing") \
    .getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("employee.csv")

header = rdd.first()
data = rdd.filter(lambda x: x != header)

employees = data.map(lambda x: x.split(","))

os.makedirs("output", exist_ok=True)

# 1. Sorted employees by salary
sorted_emp = employees.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

print("\n===== Employees Sorted By Salary =====")

sorted_list = sorted_emp.collect()

for emp in sorted_list:
    print(emp)

with open("output/sorted_employees.csv", "w") as f:
    f.write("id,name,department,salary\n")
    for emp in sorted_list:
        f.write(",".join(emp) + "\n")

# 2. Department salary totals
dept_salary = employees.map(
    lambda x: (x[2], int(x[3]))
)

dept_totals = dept_salary.reduceByKey(
    lambda a, b: a + b
)

dept_list = dept_totals.collect()

print("\n===== Department Salary Totals =====")

for dept in dept_list:
    print(dept)

with open("output/department_totals.csv", "w") as f:
    f.write("department,total_salary\n")
    for dept, total in dept_list:
        f.write(f"{dept},{total}\n")

# 3. Top 3 employees
top3 = sorted_emp.take(3)

with open("output/top3_employees.csv", "w") as f:
    f.write("id,name,department,salary\n")
    for emp in top3:
        f.write(",".join(emp) + "\n")

print("\nAll output files saved successfully!")

spark.stop()