# Dom Scordino
# CSC144A
# September 17, 2021
# Assignment 2

# Python program to determine number of hot dogs and buns needed for a cookout

# Step 1: Create Inputs for User to Enter
people = int(input('Enter the Number of People Attending the Cookout: '))
hotdogsperperson = int(input('Enter the Number of Hot Dogs expected to be Eaten by each Person: '))

# Step 2: Create Formulas for the 4 requested pieces of information
# Formula for Minimum Packs of Hot Dogs Needed (Come in 10's)
packshotdogs = round((people * hotdogsperperson) / 10)

# Formula for Minimum Packs of Hot Dog Buns Needed (Come in 8's)
packsbuns = round((people * hotdogsperperson) / 8)

# Formula for Packs of Hot Dogs Left Over (Come in 10's)
hotdogsleftover = (people * hotdogsperperson) % 10

# Formula for Packs of Hot Dog Buns Left Over (Come in 8's)
bunsleftover = (people * hotdogsperperson) % 8

# Step 3: Create Output of Information
# Output
print('The Minimum Number of Packages of Hot Dogs is', packshotdogs)
print('The Minimum Number of Packages of Hot Dog Buns is', packsbuns)
print('The Number of Hot Dogs that will be left over is', hotdogsleftover)
print('The Number of Hot Dog Buns that will be left over', bunsleftover)