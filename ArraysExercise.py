# In this exercise, we want to check through an array, and print two values that equal a predifined sum
# To complete this, we will need to import itertools

# EXAMPLE 1
print("==================== EXAMPLE 1 IS BELOW ====================")


import itertools
arr  = [8, 7, 2, 5, 3, 1]
setUniqueArr= set(arr)
theGivenSum = 10            # Based on the question, this is the given sum
for i in itertools.combinations(setUniqueArr, 2):     # We loop
    if i[0] + i[1] == theGivenSum:      # The aim is to check if they equal 10
        print("The Pair Summing to 10 for the Case are: " + str(i[0]) + " , " + str(i[1]))


# EXAMPLE 2
print("=================== EXAMPLE 2 IS BELOW =====================")

newArray = [2, 4, 6, 8, 10, 12, 14, 15, 16, 18, 18, 19, 20]
uniqueArray = set(newArray)
definedSum = 20
for b in itertools.combinations(uniqueArray, 2):        # We want to pick only two elements that equal 20
    if b[0] + b[1] == definedSum:
        print("The Pair elements Summing to 20 for the Case are: " + str(b[0]) + " , " + str(b[1]))




# EXAMPLE 3

print("=================== EXAMPLE 3 IS BELOW =====================")

# We can do the same for three (3) elements, by making some minor changes to the code as shown below

import itertools

thirdArray = [2, 4, 6, 8, 10, 12, 14, 15, 16, 18, 18, 19, 20]
myuniqueArray = set(thirdArray)
chosenSum = 20
for b in itertools.combinations(myuniqueArray, 3):        # Here, we now want to pick three elements that equal 20, rather than 2 as above
    if b[0] + b[1] + b[2] == chosenSum:
        print("The Pair elements Summing to 20 for the Case are: " + str(b[0]) + " , " + str(b[1]) + " & " + str(b[2]))

"""
==================== EXAMPLE 1 IS BELOW ====================
The Pair Summing to 10 for the Case are: 2 , 8
The Pair Summing to 10 for the Case are: 3 , 7
=================== EXAMPLE 2 IS BELOW =====================
The Pair elements Summing to 20 for the Case are: 2 , 18
The Pair elements Summing to 20 for the Case are: 4 , 16
The Pair elements Summing to 20 for the Case are: 6 , 14
The Pair elements Summing to 20 for the Case are: 8 , 12
=================== EXAMPLE 3 IS BELOW =====================
The Pair elements Summing to 20 for the Case are: 2 , 4 & 14
The Pair elements Summing to 20 for the Case are: 2 , 6 & 12
The Pair elements Summing to 20 for the Case are: 2 , 8 & 10
The Pair elements Summing to 20 for the Case are: 4 , 6 & 10

"""
