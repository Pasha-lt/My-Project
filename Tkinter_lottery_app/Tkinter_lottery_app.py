from tkinter import *
from random import random, sample

window = Tk()

img = PhotoImage(file='1.gif')

imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
resBtn = Button(window)

imgLbl.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
resBtn.grid()

window.mainloop()
exit()


num = random()
print('Random Float 0.0-1.0: ', num)
num = int(num * 10)
print('Random Integer 0-9 :', num)
nums = []
i = 0
while i < 6:
    nums.append(int(random() * 10) + 1)
    i += 1
    print('Random Multiple Integers 1-10 :', nums)

nums = sample(range(1, 49), 6)
print('Random Integer Sample 1-49 :', nums)
