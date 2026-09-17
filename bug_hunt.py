# BUG: Added missing colon at the end of the while loop statement.
count = 1
total = 0

while count <= 5:
    total = total + count
    # BUG: Fixed the loop condition from '< 5' to '<= 5' to ensure the number 5 is included in the summation.
    count = count + 1

# BUG: Converted the integer total to a string using str() to avoid a TypeError during concatenation.
print("Sum of 1 to 5 is: " + str(total))
