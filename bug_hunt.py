
count = 1
total = 0

# BUG: Missing colon (:) at the end of the while header line.
# BUG: The condition 'count < 5' only ran up to 4; changed to 'count <= 5' so it includes 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate string and int directly using +; updated to use an f-string (or str(total)).
print(f"Sum of 1 to 5 is: {total}")