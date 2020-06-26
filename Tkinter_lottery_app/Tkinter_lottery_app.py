from tkinter import *
from random import random, sample

window = Tk()
img = PhotoImage(file='1_small.gif')

imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=4, height=4, font=25, fg='red')
label2 = Label(window, relief='groove', width=4, height=4, font=25, fg='red')
label3 = Label(window, relief='groove', width=4, height=4, font=25, fg='red')
label4 = Label(window, relief='groove', width=4, height=4, font=25, fg='red')
label5 = Label(window, relief='groove', width=4, height=4, font=25, fg='red')
label6 = Label(window, relief='groove', width=4, height=4, font=25, fg='red')
getBtn = Button(window)
resBtn = Button(window)

imgLbl.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10, 20))
getBtn.grid(row=2, column=2, columnspan=4)
resBtn.grid(row=2, column=6, columnspan=2)

window.title('Lotto Number Picker')
window.resizable(0, 0)
getBtn.configure(text='Get My Lucky Numbers', fg='red')
resBtn.configure(text='Reset', fg='red')


label1.configure(text='...')
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...')


def pick():
    """Функция генерирует шесть уникальных чисел и присваевает их шести меткам"""
    nums = sample(range(1, 49), 6)
    label1.configure(text=nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[2])
    label4.configure(text=nums[3])
    label5.configure(text=nums[4])
    label6.configure(text=nums[5])
    getBtn.configure(text='Get My Lucky Numbers', state=DISABLED)
    resBtn.configure(text='Reset', state=NORMAL)



def reset():
    """Функция выводит многоточие в метках, а также возвращает значение двух кнопок в их изначальное состояние."""
    label1.configure(text='...')
    label2.configure(text='...')
    label3.configure(text='...')
    label4.configure(text='...')
    label5.configure(text='...')
    label6.configure(text='...')
    getBtn.configure(text='Get My Lucky Numbers', state=NORMAL)
    resBtn.configure(text='Reset', state=DISABLED)


getBtn.configure(command=pick)
resBtn.configure(command=reset)
window.mainloop()