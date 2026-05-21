# > Practise reading, writting, appending data in a file

# 1. -------Writing Data in File-------

# Open file in write mode
file = open("student.txt", "w")

# Write data into file
file.write("My name is Vivek\n")
file.write("I am learning Python")

# Close file
file.close()


# ------2. Reading Data from File-------

# Open file in read mode
file = open("student.txt", "r")

# Read complete file
data = file.read()

# Print data
print(data)

# Close file
file.close()

# 3. --------Appending Data in File-------

# Open file in append mode
file = open("student.txt", "a")

# Add new data
file.write("\nI am practicing file handling")

# Close file
file.close()