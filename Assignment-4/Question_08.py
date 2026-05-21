# 8. Write a Python function that takes a number as a parameter and whether the number is prime or not.

# Function to check prime number
def check_prime(n):

    # 0 and 1 are not prime
    if(n <= 1):

        print("Number is not prime")
        return

    ans = True

    # Check divisibility
    for i in range(2, n):

        if(n % i == 0):

            ans = False
            break

    # Print result
    if(ans):

        print("Number is prime")

    else:

        print("Number is not prime")


# Taking input
n = int(input("Enter Number : "))

# Function calling
check_prime(n)