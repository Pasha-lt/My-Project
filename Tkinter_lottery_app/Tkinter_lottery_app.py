from tkinter import *
from random import random, sample

window = Tk()
window.title('Lotto Number Picker')
window.resizable(0, 0)

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

getBtn.configure(text='Get My Lucky Numbers')
resBtn.configure(text='Reset', state=DISABLED)  # Деактивируем кнопку ресет

label1.configure(text='...')
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...')

imgLbl.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10, 20))
getBtn.grid(row=2, column=2, columnspan=4)
resBtn.grid(row=2, column=6, columnspan=2)




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
