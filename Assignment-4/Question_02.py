# 2. Write a Python function that takes a list and returns a new list with distinct elements from the first list.


# Function to remove duplicate elements from list
def remove_duplicates(lst):

    # Empty list to store distinct elements
    new_list = []

    # Traverse original list
    for x in lst:

        # Check element already exists or not
        if x not in new_list:

            # Add unique element
            new_list.append(x)

    # Print new list
    print("List with distinct elements is :", new_list)


# Original list
lst = [10, 20, 10, 30, 40, 20, 60, 30, 30]

# Function calling
remove_duplicates(lst)