# 3. Write a Python function to multiply all the numbers in a list.

# Function to multiply all numbers in a list
def update_list(lst):

    # Variable to store multiplication result
    multi = 1

    # Traverse list elements
    for i in range(len(lst)):

        # Multiply elements one by one
        multi = multi * lst[i]

    # Print final multiplication result
    print("Multiplication of all elements is :", multi)


# List creation
lst = [25, 45, 10, 20, 21]

# Function calling
update_list(lst)