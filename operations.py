
import calculator_gui

class operations():
    def calc_operations(self, math, first_num, second_number):
        if math == "add":
                entry_num.insert(0, first_num + int(second_number))
        if math == "subtract":
                entry_num.insert(0, first_num - int(second_number))
        if math == "multiplication":
                entry_num.insert(0, first_num * int(second_number))
        if math == "division":
                entry_num.insert(0, first_num / int(second_number))