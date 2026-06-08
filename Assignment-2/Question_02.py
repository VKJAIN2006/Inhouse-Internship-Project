# Taking first string input from user
string1 = input("Enter First String : ")

# Taking second string input from user
string2 = input("Enter Second String : ")

# String Concatenation
string3 = string1 + " " + string2

# Converts all characters into lowercase
print("Lowercase :", string3.lower())

# Converts all characters into uppercase
print("Uppercase :", string3.upper())

# Converts first letter of every word into uppercase
print("Title Case :", string3.title())

# Converts uppercase to lowercase and lowercase to uppercase
print("Swapcase :", string3.swapcase())

# Converts first character into uppercase
print("Capitalize :", string3.capitalize())

# Converts string into lowercase (stronger version of lower)
print("Casefold :", string3.casefold())

# Places string at center within 30 spaces
print("Centered String :", string3.center(30))

# Checks whether string ends with 'in'
print("Endswith 'in' :", string3.endswith('in'))

# Finds index position of character 'k'
print("Find 'k' :", string3.find('k'))

# Checks whether string contains only digits
print("Is Digit :", string3.isdigit())

# Checks whether string is numeric
print("Is Numeric :", string3.isnumeric())

# Checks whether string contains only spaces
print("Is Space :", string3.isspace())

# Replaces 'jain' with 'sir'
print("Replace :", string3.replace('jain', 'sir'))