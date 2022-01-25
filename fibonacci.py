import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
# список со значениями a и b
sp = [1, 2]

# Функция завершения приложения


def quit():
    win.quit()

# Вызов окна подтверждения продолжения игры


def msb():
    msbox = mb.askyesno(title='Вы проиграли!',
                        message='Начать снова?')  # Вызов самого окна
    if msbox:  # Если да
        sp.clear()  # Чистим список со значениями a и b
        sp.append(1)  # И вставляем изначальные
        sp.append(2)
        a = sp[-2]  # Задаем значения a и b
        b = sp[-1]
        lbl['text'] = (a, '+', b)
    else:  # Если нет
        quit()

# Функция кнопки NEXT


def next():
    otvet = etr.get()  # Считываем entry
    etr.delete(0, tk.END)  # Очищаем entry
    otvet = int(otvet)
    resh = sp[-1]+sp[-2]  # Считаем верный ответ
    if resh == otvet:  # если ответ верный
        a = sp[-1]  # Задаём новые значения a и b
        b = sp[-2]
        a = resh
        b = resh+1
        sp.append(a)  # Добавляем их в список значений
        sp.append(b)
        # Создаём пример с новыми значениями и добавляем в label
        lbl['text'] = (a, '+', b)
    else:  # если ответ неверный
        msb()

# Функция кнопки del


def delet():
    dan0 = etr.get()
    dan01 = dan0[0:-1]
    etr.delete(0, tk.END)
    etr.insert(0, dan01)

#Функция ввода значений
def vvod(num):
    dan1 = etr.get()
    etr.delete(0, tk.END)
    etr.insert(-1, dan1+num)


def but(num):
    return tk.Button(text=num, fg='#000000', font=('Comic CAT', 18), bg='#d0d0d0', bd=0, command=lambda: vvod(num))


win = tk.Tk()
win.geometry('300x490')
win['bg'] = '#202020'
win.title('Fibonacci 3.1.1')
win.resizable(width=False, height=False)

lbl = tk.Label(win, text='1 + 2',
               fg='#ffffff', font=('Comic CAT', 18), bg='#202020')
lbl.grid(row=0, column=0, stick='wens', padx=5, pady=5, columnspan=3)

etr = tk.Entry(win, bg='#d0d0d0', font=('Comic CAT', 18))
etr.grid(row=1, column=0, columnspan=3, stick='wens', padx=5, pady=5)
etr.bind('<Key>', lambda e: 'break')


but('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
but('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
but('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
but('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
but('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
but('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
but('7').grid(row=4, column=0, stick='wens', padx=5, pady=5)
but('8').grid(row=4, column=1, stick='wens', padx=5, pady=5)
but('9').grid(row=4, column=2, stick='wens', padx=5, pady=5)
but('0').grid(row=5, column=0, stick='wens', padx=5, pady=5)

tk.Button(text='del', bg='#00b092', fg='#000000', font=('Comic CAT', 18), bd=0, command=lambda: delet()).grid(
    row=5, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='Next', bg='#00b092', fg='#000000', font=('Comic CAT', 18), bd=0, command=lambda: next()).grid(
    row=5, column=2, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_rowconfigure(0, minsize=45)
win.grid_rowconfigure(1, minsize=45)
win.grid_rowconfigure(2, minsize=100)
win.grid_rowconfigure(3, minsize=100)
win.grid_rowconfigure(4, minsize=100)
win.grid_rowconfigure(5, minsize=100)

win.mainloop()
