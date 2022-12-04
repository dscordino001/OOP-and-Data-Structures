# Dom Scordino
# CSC144A
# October 1, 2021
# Assignment 4

# Python Code to Print a Series of Star Shapes

# Start of Code

# Enter the Number of Rows you would like for your Star Shapes
rows = int(input('How many rows? '))

# Print a line separating the input from the output (for aesthetic)
print()

# Output - Part 1/4 - Print Rows of stars in descending order
for integer in range(rows, -1, -1):
    for column in range(integer):
        print('*', end='')
    for column in range(integer, rows, 1):
        print(' ', end='')
    print()

# Output - Part 2/4 - Print Rows of stars in descending order with first star in each row getting farther from the edge
for integer in range(rows, -1, -1):
    for column in range(integer, rows, 1):
        print(' ', end='')
    for column in range(integer):
        print('*', end='')
    print()

# Output - Part 3/4 - Print Rows of stars in ascending order with first star in each row getting closer to the edge
for integer in range(1, rows + 1, 1):
    for column in range(integer, rows, 1):
        print(' ', end='')
    for column in range(integer):
        print('*', end='')
    print()
print()

# Output Part 4/4 - Print the first 3 shapes all back to back on the same lines with 2 spaces in between each shape

for integer in range(rows, 0, -1):
    for column in range(integer):
        print('*', end='')
    for column in range(integer - 1, rows, 1):
        print(' ', end='')
    for column in range(2, 0, -1):
        print(' ', end='')
    for column in range(integer, rows, 1):
        print(' ', end='')
    for column in range(integer):
        print('*', end='')
    for column in range(2, 0, -1):
        print(' ', end='')
    for column in range(integer - 1):
        print(' ', end='')
    for column in range(integer, rows + 1, 1):
        print('*', end='')
    print()
print()

# End of Code
