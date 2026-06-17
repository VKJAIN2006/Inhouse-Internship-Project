## Build Docker Image

Run the following command inside the project directory:

```bash
docker build -t pyspark-rdd-app .
```

---

## Run Docker Container

```bash
docker run pyspark-rdd-app
```

---

## Expected Console Output

```text
===== Employees Sorted By Salary =====

['4', 'Priya', 'Finance', '70000']
['3', 'Neha', 'IT', '65000']
['7', 'Rohit', 'Finance', '60000']
['1', 'Amit', 'IT', '55000']
['5', 'Karan', 'IT', '50000']
['6', 'Simran', 'HR', '45000']
['2', 'Rahul', 'HR', '40000']

===== Department Salary Totals =====

('IT', 170000)
('HR', 85000)
('Finance', 130000)

Top 3 employees saved successfully.
```

---

## Output Files

### sorted_employees.csv

Contains employees sorted by salary in descending order.

### department_totals.csv

Contains total salary paid in each department.

### top3_employees.csv

Contains the top three highest-paid employees.

---