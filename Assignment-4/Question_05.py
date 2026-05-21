# 5. Write a Python program to reverse a string.

# Function to reverse string
def reverse_string(s):

    # Reverse using slicing
    rev = s[::-1]

    print("Reverse string is :", rev)


# Taking input from user
s = input("Enter string : ")

print("Actual String is :", s)

# Function calling
reverse_string(s)