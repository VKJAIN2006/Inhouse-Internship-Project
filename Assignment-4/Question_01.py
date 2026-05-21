# 1. Write a Python function to find the maximum of three numbers.

# Function to find maximum among three numbers
def find_max(n1, n2, n3):

    # Check if first number is greatest
    if(n1 >= n2 and n1 >= n3):
        print(n1, "is the maximum number")

    # Check if second number is greatest
    elif(n2 >= n1 and n2 >= n3):
        print(n2, "is the maximum number")

    # Otherwise third number is greatest
    else:
        print(n3, "is the maximum number")


# Taking input from user
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

# Function calling
find_max(n1, n2, n3)