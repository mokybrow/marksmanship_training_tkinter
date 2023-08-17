from tkinter import *
import random

class Rectangle:
    def __init__(self, canvas, coord, fill, outline=None):
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)
        self.canvas = canvas
        self.outline = outline if outline is not None else fill
        self.fill = fill
        self.canvas_id = self.canvas.create_rectangle(coord, outline=self.outline, fill=self.fill)
        
        self.canvas.bind('<Button-1>', self.click)

    def draw(self):
        if (self.canvas.coords(self.canvas_id)[0] < 1 or self.canvas.coords(self.canvas_id)[2] > 700):
            self.x = self.x * (-1)
        elif (self.canvas.coords(self.canvas_id)[1] < 1 or self.canvas.coords(self.canvas_id)[3] > 400):
            self.y = self.y * (-1)
        self.canvas.move(self.canvas_id, self.x, self.y)
        self.canvas.after(35, self.draw)
        

    def click(self, event):
        x = event.x
        y = event.y
        print(self.canvas_id)
        if (x < self.canvas.coords(self.canvas_id)[2] and x > self.canvas.coords(self.canvas_id)[0]) and (
                y < self.canvas.coords(self.canvas_id)[3] and y > self.canvas.coords(self.canvas_id)[1]):
            print('Target')
            #self.canvas.delete(self.canvas_id)



root = Tk()
root.geometry('800x500')
root.title('Курсовая работа')

c = Canvas(width=700, height=400, bg='black')
c.place(x=50, y=10)

rectangle = [Rectangle(c, (10, 20, 40, 50), fill='red') for i in range(8)]
for rec in rectangle:
    rec.draw()

# Кнопки запуска, остановки и выхода из программы
vars = IntVar()
vars.set(0)
r1 = Radiobutton(text='СТАРТ', indicatoron=0, variable=vars, value=1, font='Times 15', bg='green')
r2 = Radiobutton(text='СТОП', indicatoron=0, variable=vars, value=0, font='Times 15',  bg='yellow')
r1.place(x=50, y=430)
r2.place(x=150, y=430)


root.mainloop()
