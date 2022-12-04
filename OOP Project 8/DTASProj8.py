#Dom Scordino
#CSC144A
#November 3, 2021
#Assignment 8

#Python Code to display a lottery number

#Start of Script

#set seed value to global so both functions can access the same set of random numbers
import random
global seedvalue
seedvalue = random.randint(1, 100000)

#define DTASLottoGenerator - Creates a random number 7 times, puts them into a sequence and then displays them as one number
def DTASLottoGenerator():
    #set a matrix to add random numbers into
    lottointegers = []
    #import random module
    import random
    #set seedvalue so List of NUmbers and Lotto Numbers are the same
    random.seed(seedvalue)
    for i in range (0,7):
        #Create a random number 7 times
        number = random.randint(0,9)
        #Add that number created to the end of the list
        lottointegers.append(number)

    #Make the list of numbers into one number
    strings = [str(integer) for integer in lottointegers]
    #join the 7 strings together without any spaces in between them
    one_string = "".join(strings)
    #set the lottery number equal to the new string with the 7 numbers connected to each other
    lotterynumber = int(one_string)

    #Display the lottery number on screen:
    print(">>> Today's lottery number is: ") 
    print(lotterynumber)

#define DTASDisplayList - displays the lottery numbers individually into one list
def DTASDisplayList():
    #set a matrix to add random numbers into
    listofnumbers = []
    #import random module
    import random
    #set seedvalue so List of NUmbers and Lotto Numbers are the same
    random.seed(seedvalue)
    for i in range (0,7):
        #Create a random number 7 times
        number = random.randint(0,9)
        #Add that number created to the end of the list
        listofnumbers.append(number)
    print(">>> Today's lottery number in list form is: ") 
    #print the list of numbers in a matrix
    print(listofnumbers)

#define the main function which is the DTASLottoGenerator() and DTASDisplayList() functions
def main():
    DTASLottoGenerator()
    DTASDisplayList()

#call function main()
if __name__ == '__main__':
    main()

#End of Script

#Start of Pseudocode

#1.

#set seed value to global so both functions can access the same set of random numbers

#2.

#define DTASLottoGenerator - Creates a random number 7 times, puts them into a sequence and then displays them as one number
    #set a matrix to add random numbers into
    #import random module
    #set seedvalue so List of NUmbers and Lotto Numbers are the same
        #Create a random number 7 times
        #Add that number created to the end of the list
    #Make the list of numbers into one number
    #join the 7 strings together without any spaces in between them
    #set the lottery number equal to the new string with the 7 numbers connected to each other
    #Display the lottery number on screen:

#3.

#define DTASDisplayList - displays the lottery numbers individually into one list
    #set a matrix to add random numbers into
    #import random module
    #set seedvalue so List of NUmbers and Lotto Numbers are the same
        #Create a random number 7 times
        #Add that number created to the end of the list
    #print the list of numbers in a matrix


#4.

#define the main function which is the DTASLottoGenerator() and DTASDisplayList() functions

#5.

#call function main()

#End of Pseudocode