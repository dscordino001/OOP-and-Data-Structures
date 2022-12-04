# call Employee Class
from DTASEmployee import Employee
# create ProductionWorker Class
class ProductionWorker(Employee):
    # The init method accepts arguments for the
    # name, number, age, shift, rate, hours attributes.
    def __init__(self, name, number, age, nonepay, shift, rate, hours):
        # Call the superclass __init__ method.
        Employee.__init__(self, name, number, age, nonepay)
        # Initialize the __shift attribute.
        self.__shift = shift
        # Initialize the __rate attribute.
        self.__rate = rate
        # Initialize the __hours attribute.
        self.__hours = hours
    # The mutators for the __shift, 
    # __rate, __hours attributes.
    def set_shift(self, shift):
        self.__shift = shift
    def set_rate(self, rate):
        self.__rate = rate
    def set_hours(self, hours):
        self.__hours = hours
    # The accessors for the __shift, 
    # __rate, __hours attributes.
    def get_shift(self):
        return self.__shift
    def get_rate(self):
        return self.__rate
    def get_hours(self):
        return self.__hours
    # The __str__ method returns a string 
    # indicating the object's state.
    def __str__(self):
        # make default shift value 1
        if self.__shift < 1 or self.__shift > 3:
            self.__shift = 1
        # set pay equal to rate * hours
        pay = self.__rate * self.__hours
        # create temporary function to display 
        # all 8 attributes from Employee Class
        temp = f'Here is the following information about your Production Worker:\n'
        # displays state of name
        temp += f'The Employee Name is: {Employee.get_name(self)}\n'
        # displays state of number
        temp += f'The Employee Number is: {Employee.get_number(self)}\n'
        # displays state of age
        temp += f'The Employee Age is: {Employee.get_age(self)}\n'
        # displays state of nonepay - returns "None"
        temp += f'The Employee None Pay is: {Employee.get_nonepay(self)}\n'
        # displays state of shift
        temp += f'The Employee Shift is : {self.__shift}\n'
        # displays state of rate
        temp += f'The Employee Rate is: ${self.__rate} per hour\n'
        # displays state of hours
        temp += f'The Employee Hours is: {self.__hours}\n'
        # displays pay
        temp += f'The Employee Actual Pay is: ${pay}\n'
        # returns the states in temp
        return temp