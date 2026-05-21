# 7. Write a Python function to Print Even Numbers from a Given List


# Function to print even numbers from list
def print_even(lst):

    # Traverse list elements
    for x in lst:

        # Check even condition
        if(x % 2 == 0):

            print(x)


# List creation
lst = [25, 10, 22, 14, 59, 75, 89, 100]

# Function calling
print_even(lst)