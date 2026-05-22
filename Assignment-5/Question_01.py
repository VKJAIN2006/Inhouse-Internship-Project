# 1) Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data entered by user.

import csv


import csv

# Empty list to store data
d = []

# Header row
d.append(["Name", "Address", "Mobile", "Email"])

# Taking input for 3 users
for i in range(3):

    print(f"\nEnter Details of Person {i+1}")

    name = input("Enter Name : ")
    address = input("Enter Address : ")
    mobile = input("Enter Mobile : ")
    email = input("Enter Email : ")

    # Add row into list
    d.append([name, address, mobile, email])

# Writing data into CSV file
with open("address_book.csv", "w", newline='') as file:

    writer = csv.writer(file)

    writer.writerows(d)

print("\nCSV File Created Successfully")