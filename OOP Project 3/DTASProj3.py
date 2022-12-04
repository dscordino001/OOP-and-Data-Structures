# Dom Scordino
# CSC144A
# September 24, 2021
# Assignment 3

# Python program to Display the Sum of Positive Numbers Entered

# Make a Cumulative Total
total = 0.0
x = int(input('Enter a Positive Integer: '))

# Add Positive Integers to Total
while x > 0:
    total = total + x
    x = int(input('Enter Another Positive Integer or Enter 0 to Display Sum: '))
    
# Display Error Message to Invalid Numbers Entered
    while x < 0:
        print('Error: Negative Number')
        x = int(input('Enter Positive Integers: '))

# Function to Have Zero Used to Discontinue Loop 
if x == 0:
    print('The Sum of the Positive Integers Inputted is', total)
