class calculatorGUI():
    def __init__(self, root, Calculator, Entry, Tk):
        self.calculator = Calculator
        self.root = Tk()
        root.title("Elle.Calculator")
        root.configure(bg="gray")
        
        entry_num = Entry(root, width=50, borderwidth=25)
        root.resizable(0,0)
        entry_num.grid(row=0, column=0, columnspan=80, padx=30)

        entry_num = Entry(root, width=50, borderwidth=25)
        
        root.resizable(0,0)
        entry_num.grid(row=0, column=0, columnspan=80, padx=30)


    # defining buttons 
class buttons():
    def __init__(self, entry_num, END, Button, root):

        def button_click(number):
            current = entry_num.get()
            entry_num.delete(0, END)
            entry_num.insert(0, str(current) + str(number))

    # define clear button 
        def button_clear():
            entry_num.delete(0, END)

    # define clear entry button
        def button_clearEntry():
            entry_num.delete(0, END)

    # define percentage button
        def button_percentage():
            entry_num.delete(0, END)

    # define decimal button
        def button_decimal():
            entry_num.delete(0, END)

    # define add button
        def button_add():
            first_number = entry_num.get()
            global first_num
            global math 
            math = "add"
            first_num = int(first_number)
            entry_num.delete(0, END)

    # define subtract button 
        def button_subtract():
            first_number = entry_num.get()
            global first_num
            global math 
            math = "subtract"
            first_num = int(first_number)
            entry_num.delete(0, END)
    
    # define multiplication button 
        def button_multiplication():
            first_number = entry_num.get()
            global first_num
            global math 
            math = "multiplication"
            first_num = int(first_number)
            entry_num.delete(0, END)

    # define division button 
        def button_division():
            first_number = entry_num.get()
            global first_num
            global math 
            math = "division"
            first_num = int(first_number)
            entry_num.delete(0, END)

    # define equal button
        def button_equal():
            second_number = entry_num.get()
            entry_num.delete(0, END)

        button_1 = Button(root, text="1", padx=45, pady=20, command=lambda: button_click(1))
        button_2 = Button(root, text="2", padx=50, pady=20, command=lambda: button_click(2))
        button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
        button_4 = Button(root, text="4", padx=45, pady=20, command=lambda: button_click(4))
        button_5 = Button(root, text="5", padx=50, pady=20, command=lambda: button_click(5))
        button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
        button_7 = Button(root, text="7", padx=45, pady=20, command=lambda: button_click(7))
        button_8 = Button(root, text="8", padx=50, pady=20, command=lambda: button_click(8))
        button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
        button_0 = Button(root, text="0", padx=45, pady=20, command=lambda: button_click(0))