class operations():

entry_num = Entry

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

    def calc_operations(self, math, entry_num, first_num, second_number): 
    if math == "add":
            entry_num.insert(0, first_num + int(second_number))
    if math == "subtract":
            entry_num.insert(0, first_num - int(second_number))
    if math == "multiplication":
            entry_num.insert(0, first_num * int(second_number))
    if math == "division":
            entry_num.insert(0, first_num / int(second_number))