# Dom Scordino
# CSC144A
# October 8, 2021
# Assignment 5

# Python Code to Estimate Cost of a Paint Job

# Start of Script

#define known variables

hours_per_foot = 8 / 112
gallon_per_foot = 1 / 112
labor_per_hour = 35

#define main function

def main():
    global wall_space                                                                               #define global function for use in main() and DTASTotal Cost
    global cost_per_gallon                                                                          #define global function for use in main() and DTASTotal Cost
    wall_space = int(input('Enter amount of Wall Space about to be painted in square feet: '))      #Have User enter the square footage of wall space
    cost_per_gallon = int(input('Enter cost of paint per gallons: '))                               #Have User enter the cost of paint per gallon

#define total cost function

def DTASTotalCost():
    paint_needed = gallon_per_foot * wall_space                                                     #formula for amount of paint needed
    cost_of_paint = cost_per_gallon * paint_needed                                                  #formula for cost of paint
    hours_of_labor = wall_space * hours_per_foot                                                    #formula for hours of labor
    total_labor = hours_of_labor * labor_per_hour                                                   #formula for total labor charges
    TotalCost = cost_of_paint + total_labor                                                         #formula for total cost
    print(f'The Number of Gallons of Paint required is {paint_needed}.')                            #output for amount of paint needed
    print(f'The Total Cost of the Paint for the Job is {cost_of_paint}.')                           #output for cost of paint
    print(f'The Total Cost of the Labor Charges for the Job is {total_labor}.')                     #output for total labor charges
    print(f'The Total Cost of the Job is {TotalCost}.')                                             #output for total cost

#Output - Use if Statement to ask if User wants estimate

def estimate_Q():    
    estimate_cost = input('Do you want to estimate the cost of a painting job? - y/n: ')            #Input for Estimate
    if estimate_cost.lower() == 'y':                                                                #If the User wants the estimate, run main() and DTASTotalCost()
            main()
            DTASTotalCost()
    elif estimate_cost.lower() == 'n':                                                              #If the user does not want the estimate, return
        return
    else:                                                                                           #If the User does not type y or n, print invalid response and ask the question again
        print('Invalid Response. Answer y to run estimate. Answer n to terminate code.')
        estimate_Q()

#Run Code

estimate_Q()

#End of Script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~