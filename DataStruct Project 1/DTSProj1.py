# Dom Scordino
# CSC145B
# February 11, 2022
# Assignment 1

# Start of Code

class DTSComplex:
    __num_of_complex = 0
    def __init__(self, __real, __imag):
        self.__real = int(__real)
        self.__imag = int(__imag)
        DTSComplex.__num_of_complex += 1
#-------------------------------------------------------------------------------------
    def __repr__(self):
        return f'{self.__real} + {self.__imag}i'
#-------------------------------------------------------------------------------------
    def __del__(self):
        DTSComplex.__num_of_complex -= 1
#-------------------------------------------------------------------------------------
    def __mul__(self, other):
        new_real = self.__real * other.__real
        new_imag = self.__imag * other.__imag
        return DTSComplex(new_real, new_imag)
#-------------------------------------------------------------------------------------
    def __add__(self, other):
        new_real = self.__real + other.__real
        new_imag = self.__imag + other.__imag
        return DTSComplex(new_real, new_imag)
#-------------------------------------------------------------------------------------
    @classmethod
    def num_of_complex(cls):
        return cls.__num_of_complex

a = DTSComplex(1,3)
b = DTSComplex(2,4)
c = a + b
d = a * b

def main():
    print(a)
    print(b)
    print(c)
    print(d)
    print(DTSComplex.num_of_complex())

#call function main()
if __name__ == '__main__':
    main()