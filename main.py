# -*- coding: utf-8 -*-
from tkinter import *
import random
from tkinter.messagebox import showinfo

global count 

count = 0

class Rectangle:
    global count
    def __init__(self, canvas, coord, fill, outline=None):
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)
        self.canvas = canvas
        self.outline = outline if outline is not None else fill
        self.fill = fill
        self.canvas_id = self.canvas.create_rectangle(coord, outline=self.outline, fill=self.fill)


    def draw(self):
        if (self.canvas.coords(self.canvas_id)[0] < 1 or self.canvas.coords(self.canvas_id)[2] > 700):
            self.x = self.x * (-1)
        elif (self.canvas.coords(self.canvas_id)[1] < 1 or self.canvas.coords(self.canvas_id)[3] > 400):
            self.y = self.y * (-1)
        if vars.get() == 1:
            self.canvas.move(self.canvas_id, self.x, self.y)
            self.canvas.after(35, self.draw)

    def stop(self):
        self.canvas.move(self.canvas_id, self.x, self.y)
        self.canvas.after(40000, self.stop)

    def delete_rec(self):
        global rectangle
        global count
        self.canvas.itemconfig(self.canvas_id, fill="white", outline="black")
        self.canvas.coords(self.canvas_id, 0,0,0,0)
        count+=1
        
        if count%10==0:
            rectangle = [Rectangle(c, (10, 20, 40, 50), fill='red') for i in range(10)]
            vars.set(0)
            count = 0
            showinfo(title='Игрок', message='Ты набрал 10 очков')
            
        l2.config(text=count)

root = Tk()
root.geometry('800x500')
root.title('Curses')

c = Canvas(width=700, height=400, bg='black')
c.place(x=50, y=10)

rectangle = [Rectangle(c, (10, 20, 40, 50), fill='red') for i in range(10)]


def start():
    if vars.get() == 1:
        for rec in rectangle:
            rec.draw()

for rec in rectangle:                
    def stop():
        vars.set(0)
        for rec in rectangle:
            rec.stop()

def click(event):
    x = event.x
    y = event.y
    if count == 10:
        print('check')
    for rec in rectangle:
        x1, y1, x2, y2 = rec.canvas.coords(rec.canvas_id)
        if (x1 < x < x2) and (y1 < y < y2):
            rec.delete_rec()


rec.canvas.bind('<Button-1>', click) 
# Кнопки запуска, остановки и выхода из программы
vars = IntVar()
vars.set(0)
r1 = Radiobutton(text='start', indicatoron=0, variable=vars, value=1, command=start, font='Times 15', bg='green')
r2 = Radiobutton(text='stop', indicatoron=0, variable=vars, value=0, command=stop, font='Times 15',  bg='yellow')
r1.place(x=50, y=430)
r2.place(x=150, y=430)

# Счёт игры
l1 = Label(text='Счёт:', font='Times 15')
l1.place(x=500, y=430)
l2 = Label(text='0', font='Times 15')
l2.place(x=550, y=430)

# Функция вызывающая дополнительное окно с информацие об авторе
def surname_info():
    w = Toplevel()
    w.title('Об авторе')
    surname = Label(w, text="Панин Михаил Сергеевич, группа 20-ИЭ", bg='gold')
    surname.pack()
    w.mainloop()
mainmenu = Menu(root)
root.config(menu=mainmenu)

helpmenu = Menu(mainmenu, tearoff=0)
mainmenu.add_command(label="Об авторе", command=surname_info)

root.mainloop()
