# simple gui calculator using python:::

from tkinter import *
# globally declare the expression variable
expression = ""

# function to update expression
# in the text entry box

def press (num):
    # point out the global expression vaiable
    global expression
    # concatenation of string
    expression = expression + str(num)
    # update the expression by using set method
    equation.set(expression)
    
# function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
    
if __name__ ==  "_main_":
    gui = Tk()
    gui.configure(background="blue")
    gui.title("Simple Calculator")
    gui.geometry("270*150")
    equation = StringVar()
    expression_field= Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    button1 = Button(gui, text=' 1 ', fg='black', bg = 'red', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ', fg='black', bg = 'red', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text=' 3 ', fg='black', bg = 'red', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ', fg='black', bg = 'red', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', fg='black', bg = 'red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', fg='black', bg = 'red', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', fg='black', bg = 'red', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text=' 8 ', fg='black', bg = 'red', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text=' 9 ', fg='black', bg = 'red', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
    button0 = Button(gui, text='0', fg='black', bg='blue',command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
    plus = Button(gui, text= ' + ', fg= 'black', bg='red', command=lambda: press("+"), height =1,weidth=7)
    plus = Button(row=2, column=3)
    minus = Button(gui, text= ' - ', fg= 'black', bg='red', command=lambda: press("-"), height =1,weidth=7)
    minus = Button(row=3, column=3)

    multiply = Button(gui, text= ' * ', fg= 'black', bg='red', command=lambda: press("*"), height =1,weidth=7)
    multiply = Button(row=4, column=3)
    divide = Button(gui, text= ' / ', fg= 'black', bg='red', command=lambda: press("/"), height =1,weidth=7)
    divide = Button(row=5, column=3)
    equal = Button(gui, text= ' = ', fg= 'black', bg='red', command=lambda: press("="), height =1,weidth=7)
    equal = Button(row=5, column=2)
    clear = Button(gui, text= ' clear ', fg= 'black', bg='red', command=lambda: press("clear"), height =1,weidth=7)
    clear = Button(row=5, column=1)
    Decimal = Button(gui, text= ' . ', fg= 'black', bg='red', command=lambda: press("."), height =1,weidth=7)
    Decimal = Button(row=6, column=0)
# Start the GUI

    gui.mainloop()