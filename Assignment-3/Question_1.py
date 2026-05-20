# 1) Practise
# 	Dictionary
# 	Tuple
# 	Set


# Dictionary Creation
d = {
    1: "Vivek",
    2: "Rahul",
    3: "Aman"
}

# Print dictionary
print("Dictionary :", d)

# Access element
print("Element at key 1 :", d[1])

# Add new element
d[4] = "Rohit"

print("After Adding :", d)

# Update value
d[2] = "Karan"

print("After Updating :", d)

# Delete element
del(d[3])

print("After Deletion :", d)

# Print keys
print("Keys :", d.keys())

# Print values
print("Values :", d.values())

# Print items
print("Items :", d.items())


# Tuple Creation
t = (10, 20, 30, 40, 50)

# Print tuple
print("Tuple :", t)

# Access element
print("First Element :", t[0])

# Slicing
print("Tuple Slicing :", t[1:4])

# Length of tuple
print("Length :", len(t))

# Count occurrence
print("Count of 20 :", t.count(20))

# Find index
print("Index of 40 :", t.index(40))



# Set Creation
s = {10, 20, 30, 40}

# Print set
print("Set :", s)

# Add element
s.add(50)

print("After Adding :", s)

# Remove element
s.remove(20)

print("After Removing :", s)

# Another set
s2 = {40, 50, 60, 70}

# Union
print("Union :", s.union(s2))

# Intersection
print("Intersection :", s.intersection(s2))

# Difference
print("Difference :", s.difference(s2))