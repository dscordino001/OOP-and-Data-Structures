#Dom Scordino
#CSC144A
#October 22, 2021
#Assignment 7

#Python Code to read the numbers in a file and display the sum

#Start of Script

#open the file and read the contents
numbersfile = open('C:\\Users\\dscor\\OneDrive\\Desktop\\Visual Studio\\VSC Assignments\\numbers.txt', 'r')
#read the lines in the file
read = numbersfile.readlines()
#p represents the creation of a string out of the read line in the file
p = str(read)

#define the sum function
def sum():
    #for a line read in numbers.txt
    for line in read:
        #set total to a global variable
        global total
        #set accumulator value for sum of all digits
        #total = 0
        #while loop for when there is a string in a line that is digits
        while p.isdigit():
            #set accumulator value for sum of all digits
            #total = 0
        #for an integer in the line read
        for i in read:    
            #add that integer to the accumulator value
            total = total + int(i)
        #stop the code once you have added all integers in the file
        break
    #display the sum
    print('The sum of the digits is', total)

#define the average of the sum function
def extracredit():
    #import statistics and mean function
    from statistics import mean
    #variable for the average of the sum
    average = mean(range(total))
    #print the average of the sum to 2 decimal places
    print(f'The average of the sum is {average:.2f}')

#define the main function which is the extracredit and sum functions
def main():
    sum()
    extracredit()

#call function main()
if __name__ == '__main__':
    main()

#End of script