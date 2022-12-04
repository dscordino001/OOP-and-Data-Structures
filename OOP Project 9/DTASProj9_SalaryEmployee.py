# call Employee Class
from DTASEmployee import Employee
# create SalaryEmployees Class
class SalaryEmployee(Employee):
    def __init__(self, name, number, age, nonepay, yearsalary):
        # Call the superclass __init__ method.
        Employee.__init__(self, name, number, age, nonepay)
        # Initialize the __yearsalary attribute.
        self.__yearsalary = yearsalary
    # The mutator for the __yearsalary attribute.
    def set_yearsalary(self, yearsalary):
        self.__yearsalary = yearsalary
    # The accessor for the __yearsalary attribute.
    def get_yearsalary(self):
        return self.__yearsalary
    # The __str__ method returns a string 
    # indicating the object's state.
    def __str__(self):
        # create temporary function to display 
        # all 5 attributes

        # Intorduction Line for Salary Employee
        temp = f'Here is the following information about your Salary Employee:\n'
        # displays state of name
        temp += f'The Employee Name is: {Employee.get_name(self)}\n'
        # displays state of number
        temp += f'The Employee Number is: {Employee.get_number(self)}\n'
        # displays state of age
        temp += f'The Employee Age is: {Employee.get_age(self)}\n'
        # displays state of nonepay - returns "None"
        temp += f'The Employee None Pay is: {Employee.get_nonepay(self)}\n'
        # displays state of yearly pay divided by 12 to show monthly pay
        temp += f'The Employee Monthly Salary is: ${((self.__yearsalary)//12)} a month\n'
        # returns the states in temp
        return temp