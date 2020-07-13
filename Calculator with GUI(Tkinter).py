#9139136@gmail.com
from tkinter import *

start = True  # The variable 'start' is needed to understand what the user entered.
lastcommand = '='
result = 0


def click(text):  # Processing function, everything could be done through 'bind', but we will add to the 'button (comand =)'.
    global start
    global lastcommand
    global display
    if text.isdigit() or text == '.':  # Create application logic.
        if start:
            display.configure(text='')  # If the user has entered a number, then we display it on the scoreboard
            start = False
        if text != '.' or display.cget('text').find(
                '.') == -1:  #If our text is not equal to a point or it already was then we do not add it.
            display.configure(text=(display.cget(
                'text') + text))  # Enter the value specified by the user.
    else:  # If the user did not enter a number, then he entered the arithmetic sign.
        if start:
            lastcommand = text  # If the user immediately clicked the operation sign (to zero),
            # then we print him the same number. We also save the number if we have the 2nd arithmetic operation.
        else:
            calculate(float(display.cget('text')))
            lastcommand = text  # If the user clicks on '=' several times, the operation will be repeated (+5 +5 +5).
            start = True


def calculate(x):  # Operations on numbers.
    global lastcommand
    global result
    global display
    if lastcommand == '+':
        result += x
    elif lastcommand == '-':
        result -= x
    elif lastcommand == '*':
        result *= x
    elif lastcommand == '/':
        try:
            result /= x
        except ZeroDivisionError:
            result = "Impossible to divide by zero"
    elif lastcommand == '=':
        result = x

    display.configure(text=result)


root = Tk()
root.title('Calculator')  # Make a headline and center it.

buttons = (('7', '8', '9', '/'),  # Make buttons
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           ('0', '.', '=', '+'))

display = Label(root, text='0', font="Tahoma 20", bd=10)  # Make output(display)
display.grid(row=0, column=0, columnspan=4)  # We place on all width.

for row in range(4):  # We display the buttons in a two-dimensional cycle for our tuple "buttons".
    for column in range(4):
        button = Button(root, text=buttons[row][column], font='Tahoma 20',
                        command=lambda text=buttons[row][column]: click(text))

        button.grid(row=row + 1, column=column, padx=5, pady=5, ipadx=20, ipady=20, sticky='nsew')

w = root.winfo_reqwidth()  # The width of this window.
h = root.winfo_reqheight()  # The height of this window.

ws = root.winfo_screenwidth()  # The width of the window for the user.
hs = root.winfo_screenheight()  # User window height.

x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)

root.geometry(f'+{x}+{y}')
root.mainloop()
