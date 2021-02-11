#Привет, это фановый кликер
from tkinter import *
from tkinter import messagebox
import pyautogui as p
#Библиотеки
def click():
    while True:
        if int(pereg.get()) == 1:
            p.press('enter')     #Нажатие кнопки 'enter'
        elif int(pereg.get()) == 0:
            p.click()            #Нажатие правой кнопки миши)))
def click1():
    if j.get() != "":
        try:                                    
            for x in range(int(j.get())):
                if int(pereg.get()) == 1:
                    p.press('enter')  #Нажатие кнопки 'enter'
                    #print("gg")      #Debug
                elif int(pereg.get()) == 0:
                    #print("g")       #Debug
                    p.click()         #Нажатие правой кнопки миши)))
        except ValueError:
            messagebox.showerror("","Чел, учись читать, тебе тут рано быть!!))") #Ладно
            r.destroy()#Ouff
    else:
        messagebox.showwarning("","Введите кол-во кликов")
def switch():
    messagebox.showinfo("","Режим выбора кол-ва кликов")
    l.pack()
    j.pack()
    g.config(command = click1)
    ggg.config(command=switch1)
def switch1():
    messagebox.showinfo("","Режим бесконечности кликов")
    l.pack_forget()
    j.pack_forget()
    g.config(command = click)
    ggg.config(command=switch)
#Функции
r = Tk()
r.title("Кликер")
pereg = IntVar()
pere = Checkbutton(text=("Клик миши, или нажатие enter"), variable=pereg)
g = Button(r,font=("gg",15), text=("Начать"), command=click)
l = Label(r,font=("gg",10), text=("Кол-во кликов"))
j = Entry(r)
ggg = Button(r,font=("gg",7), text=("Переключение режимов"), command=switch)
ggg.pack()
g.pack()
pere.pack()
r.mainloop()
#Окно
