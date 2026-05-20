# 3) Write a program to check Palindrome Number

#  For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.

# Steps for checking Palindrome number


# 1. Find reverse of the given number.
# 2. Compare that number with the reverse number.
# 3. If number and its reverse is equal then it is a Palindrome Number otherwise not.

# Taking input from user
a = int(input("Enter number : "))

# Store original number
x = a

# Variable to store reversed number
r = 0

# Loop to reverse number
while(a > 0):

    # Extract last digit
    k = a % 10

    # Build reversed number
    r = r * 10 + k

    # Remove last digit
    a = a // 10

# Check palindrome
if(x == r):
    print("Number is Palindrome")

else:
    print("Number is not Palindrome")