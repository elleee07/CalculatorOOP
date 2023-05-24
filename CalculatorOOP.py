# ELLA MARIE A. MALLARI
# BSCPE 1-4

# OOP CALCULATOR

from calcOperations import Operations
import calculator_gui

# creating class for main calculator
try:
    class Calculator():
        def __init__(self):
            self.result= 0

# class for operations 
    class Operations():
        def calc_calculation():
            
            # class for whole use of GUI
            class calculatorGUI():
                def __init__(self, root, Calculator, Entry, Tk):
                    self.calculator = Calculator
                    self.root = Tk()
                    root.title("Elle.Calculator")
                    root.configure(bg="gray")
except:
    print("Error found")

finally: 
    print("No error found.")
