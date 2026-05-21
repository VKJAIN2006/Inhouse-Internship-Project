# 6. Write a Python function to check whether a number falls within a given range.

# Function to check whether number lies within range
def check_num(start, end, n):

    # Check range condition
    if(n >= start and n <= end):

        print(n, "lies in the given range")

    else:

        print(n, "does not lie in the given range")


# Taking range input
start = int(input("Enter starting number of range : "))
end = int(input("Enter ending number of range : "))

# Taking number to check
n = int(input("Enter number to check : "))

# Function calling
check_num(start, end, n)