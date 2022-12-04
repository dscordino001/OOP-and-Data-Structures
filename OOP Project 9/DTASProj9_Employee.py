# create Employee class
class Employee:
    # The __init__ method accepts arguments for the
    # name, number, age. It initializes
    # the data attributes with these values.
    def __init__(self, name, number, age, nonepay):
        # Initialize the __name attribute.
        self.__name = name
        # Initialize the __number attribute.
        self.__number = number
        # Initialize the __age attribute.
        self.__age = age
        # Initialize the __nonepay attribute.
        self.__nonepay = None
    # The following methods are mutators for the
    # class's data attributes.
    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number
    def set_age(self, age):
        self.__age = age
    def set_nonepay(self, nonepay):
        self.__nonepay = nonepay
    # The following methods are the accessors
    # for the class's data attributes.
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    def get_age(self):
        return self.__age
    def get_nonepay(self):
        return self.__nonepay
    # The __str__ method returns a string
    # indicating the object's state.
    def __str__(self):
        # create temporary function to display 
        # all 4 attributes
        
        # displays state of name
        temp = f'The Employee Name is : {self.__name}\n'
        # displays state of number
        temp += f'The Employee Number is: {self.__number}\n'
        # displays state of age
        temp += f'The Employee Age is: {self.__age}\n'
        # displays state of nonepay - returns "None"
        temp += f'The Employee None Pay is: {self.__nonepay}\n'
        # returns the states in temp
        return temp