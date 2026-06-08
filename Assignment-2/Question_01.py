# Taking student details
Name = input("Enter Student Name : ")
Student_class = int(input("Enter Class : "))

# Variable to store total marks
Total_marks = 0

# Loop for entering marks of 5 subjects
for i in range(1, 6):
    marks = int(input(f"Enter Subject {i} Marks : "))
    Total_marks += marks

# Calculating percentage
Percentage = (Total_marks / 500) * 100

# Displaying student details
print("\n----- RESULT -----")
print("Name of Student :", Name)
print("Class :", Student_class)
print("Total Marks :", Total_marks)
print("Percentage :", round(Percentage, 2))