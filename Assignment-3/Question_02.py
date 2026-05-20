# 2) Write a function for basic math operations like add multiply substract divide and 
#    use this in your program, take 2 number input from user.


# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):

    if b == 0:
        return "Division is not possible!"

    return a / b


# Taking input from user
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
print("First number is : ",a)
print("Second number is :",b)

# Menu driven program
while True:

    print("""
1. Add Numbers
2. Subtract Numbers
3. Multiply Numbers
4. Divide Numbers
5. Exit

""")

    ch = int(input("Enter your choice : "))

    # Addition
    if ch == 1:

        print("Addition of Numbers :", add(a, b))

    # Subtraction
    elif ch == 2:

        print("Subtraction of Numbers :", subtract(a, b))

    # Multiplication
    elif ch == 3:

        print("Multiplication of Numbers :", multiply(a, b))

    # Division
    elif ch == 4:

        print("Division of Numbers :", divide(a, b))

    # Exit
    elif ch == 5:

        print("Program exited successfully")
        break

    # Invalid choice
    else:

        print("Please select a valid choice!")

    