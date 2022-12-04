#Dom Scordino
#CSC144A
#October 15, 2021
#Assignment 6

#Python Code to Determine if an Integer is a Prime Number

#Start of Script

#Program to check if a number is prime or not

def initial_input():                                #define input function for two numbers
    global num1                                     #make num1 variable used to all functions in script
    global num2                                     #make num2 variable used to all functions in script
    num1 = int(input('Enter A Number: '))           #Input num1
    num2 = int(input('Enter Another Number: '))     #Input num2

#define DTAS_is_prime function that calculates whether an integer is prime
def DTAS_is_prime():
    
    if num1 > 1:
        for integers in range(2,num1):              #checking for factors that num1 has
            if (num1 % integers) == 0:              #if an integer can be divided and has no remainder,
                print(num1, 'is False')             #then it is not prime
                break                               #end section of for loop
        else:
            print('True')                           #if an integer has remainders when divided by integers, then it is prime
    
    if num2 > 1:
        for integers in range(2,num2):              #checking for factors that num2 has
            if (num2 % integers) == 0:              #if an integer can be divided and has no remainder,
                print(num2, 'is False')             #then it is not prime
                break                               #end section of for loop
        else:
            print('True')                           #if an integer has remainders when divided by integers, then it is prime
    
    if num1 <= 1:                                   #if num1 is less than or equal to 1, print None
        print('None')
    if num2 <= 1:                                   #if num2 is less than or equal to 1, print None
        print('None')

#print prime numbers between 1 and 100    
    for numbers in range (1, 101):                  #for numbers between 1 and 100
        count = 0                                   #set accumulator value to count up prime numbers to zero
        for i in range(2, (numbers//2 + 1)):        #for integers in the range of 2 to a range of numbers
            if(numbers % i == 0):                   #if a number in that range does not have a remainder after inputted into the previous lines function (numbers//2+1)
                count = count + 1                   #add that integer represented in numbers to accumulator
                break                               #exit the loop

        if (count == 0 and numbers != 1):           #if the integers represented in the numbers variable is not in the count accumulator and does not equal one
            print(" %d" %numbers, end = ' ')        #prine the number


#define main function to be ran
def main():                                         #main() function combines the input function and prime determination function
    initial_input()
    DTAS_is_prime()

#run code
if __name__ == '__main__':
    main()

#end of script