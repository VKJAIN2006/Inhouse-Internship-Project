# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Function to calculate factorial using recursion
def factorial(n):

    # Base condition
    if(n == 0 or n == 1):
        return 1

    # Recursive call
    return n * factorial(n - 1)


# Taking input from user
n = int(input("Enter number : "))

# Printing factorial
print("Factorial is :", factorial(n))