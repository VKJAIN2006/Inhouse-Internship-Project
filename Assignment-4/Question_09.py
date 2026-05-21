# 9. Write a Python function that accepts a string and counts the number of upper and lower case letters.

# Function to count uppercase and lowercase letters
def count_letters(s):

    # Counter for uppercase letters
    count_upper = 0

    # Counter for lowercase letters
    count_lower = 0

    # Traverse string characters
    for x in s:

        # Check uppercase letter
        if(x >= 'A' and x <= 'Z'):

            count_upper += 1

        # Check lowercase letter
        elif(x >= 'a' and x <= 'z'):

            count_lower += 1

    # Print results
    print("Total Uppercase letters are :", count_upper)

    print("Total Lowercase letters are :", count_lower)


# Taking input from user
s = input("Enter String : ")

# Function calling
count_letters(s)