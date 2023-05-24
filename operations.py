
import CalculatorOOP 

# class for operations
class operations():
    # defining every variables that we need 
    def calc_operations(self, math, entry_num, first_num, second_number):
        # for addition
        if math == "add":
                entry_num.insert(0, first_num + int(second_number))
        # for subtraction
        if math == "subtract":
                entry_num.insert(0, first_num - int(second_number))
        # for multiplication
        if math == "multiplication":
                entry_num.insert(0, first_num * int(second_number))
        # for division
        if math == "division":
                entry_num.insert(0, first_num / int(second_number))

