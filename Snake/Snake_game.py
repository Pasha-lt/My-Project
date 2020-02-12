import random
from tkinter import *
from PIL  import Image, ImageTk # Нужно добавить модуль для управления графикой.

'''
Реализована простая игра(Змейка). 
Использовались такие библиотеки как Tkinter, для создания графического интерфейса и прорисовки обьектов. Для более тонкой
работы с графикой была использована библиотека pillow(PIL), она помогла более детально проработать графику.
Также была использована библиотека random для рандомного появления яблук. 

Сама анимация была достигнута с помощью таймера тоесть указания через какое время наш обьект сдвинется с места. 
С повышением уровня задержка таймера уменьшалась и скорость соответственно увеличивалась. 

Отслеживания обьектов в основном реализовалось через использование тегов. И создания квадратной координаты в которой и 
мониторилось попадания обьектов.
'''

WIDTH = 800
HEIGHT = 800
BODYSIZE = 50 # Размер клетки.
STARTDELAY = 300 # Начальный интервал для нашего таймера(что бы создать анимацию).
MINDELAY = 100 # После каждого сьедания яблока будем увеличивать скорость, но ниже 100 не ставим.
STEPDELAY = 20 # Будем увеличивать скорость на 20 единиц после каждого яблока.
LENGTH = 3 # Начальная длина змейки.

countBodyW = WIDTH/BODYSIZE # Определяем сколько у нас будет клеток по ширине.
countBodyH = HEIGHT/BODYSIZE # Определяем сколько у нас будет клеток по высоте.

class Snake(Canvas): # Наследуемся от класса канвас, что бы рисовать.

    x = False
    y = False
    headImage = False # Так как нам прийдется в дальнейшем крутить голову змеи то делаем ее отдельным свойством.
    head = False
    body = False
    apple = False
    delay = 0
    direction = 'Right' # Указываем направление в котором будет двигатся
    directiontemp = 'Right' # Переменая в которой будет хранится указания изминения движения(пользователь уже назал, но к змейке оно еще не применилось).
    loss = False # Переменая которая будет отвечать проиграл пользователь или нет.


    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background='black', highlightthickness=0) # Убераем белую рамку.
        self.focus_get() # Вызываем фокус, что бы введеные команды могли сразу обрабатыватся
        self.bind_all('<Key>', self.onKeyPressed)# Вешаем биндинг указываем что хотим обрабатывать абсолютно все клавиши которые нажимает пользователь.
        self.loadResourse() # Создаем метод для загрузки картинок и ниже прописываем его.
        self.beginplay() # Делаем что бы при запуске програмы сразу запускалась игра.
        self.pack()


    def loadResourse(self):
        self.headImage = Image.open('images/head.png') # Указываем адрес к рисунку Image берем из папки.
        self.head = ImageTk.PhotoImage(self.headImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS)) # Вызываем resize что бы преобразовать картинку в используем что бы изображение было сглаженым Image.ANTIALIAS.
        self.body = ImageTk.PhotoImage(Image.open('images/body.png').resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.apple = ImageTk.PhotoImage(Image.open('images/apple.png').resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))


    def beginplay(self): # Настройки которые у нас будут при начале игры.
        self.delay = STARTDELAY
        self.direction = 'Right'
        self.directiontemp = 'Right'
        self.loss = False
        self.x = [0] * int(countBodyW)  # Координаты кадой из частей змейки.
        self.y = [0] * int(countBodyH)  # Координаты кадой из частей змейки.
        self.delete(ALL) # Очищаем канву независимо, начал пользователь только играть или уже были игры до этого.
        self.spawnActors() # Создаем обьекты в игре. ниже пишем специально для этого функцию.
        self.after(self.delay, self.timer) # Запускаем таймер, что бы создать анимацию. self.delay - задержка через какое время нам нужно запускать.
# Вторым аргументом указываем функцию которую нам нужно вызывать через заданый промежуток времени (self.timer) создаем позже.
# timer отработает один раз, так что в самом методе таймера его тоже нужно запускать.


    def spawnActors(self):
        self.spawnApple()
        self.x[0] = int(countBodyW / 2) * BODYSIZE # Пишем координаты головы, умножаем чтобы получилось в центре экрана.
        self.y[0] = int(countBodyH / 2) * BODYSIZE
        for i in range(1, LENGTH): # Так как мы указали движении змейки в право, то нам будет удобней рисовать змейку в левую сторону. так как голова считается одним блоком то мы делаем от 1.
            self.x[i] = self.x[0] - BODYSIZE * i # Каждый следующий раз мы от головы отступаем на BODYSIZE * i(на существующие блоки).
            self.y[i] = self.y[0] # Координаты по 'y' одинаковые.
        self.create_image(self.x[0], self.y[0], image = self.head, anchor='nw', tag = 'head') # Теперь собственно рисуем всю змейку. x[0], y[0] - координаты,
            # Дальше что мы выводим. с помощью anchor='nw' делаем наше изображение строго левый верхний угол.и добавляем tag что бы потом легкго найти.
        for i in range(LENGTH - 1, 0, -1): # Выводим хвост. тут важно делать расчет с конца.
            self.create_image(self.x[i], self.y[i], image=self.body, anchor='nw', tag='body')


    def spawnApple(self): # Метод по появлению яблок. метод будет вызыватся на протяжении всей игры.
        apple = self.find_withtag('apple') # Для того что бы создать новое яблуко нужно удалить предведущее ищем его через tag.
        if apple:
            self.delete(apple[0]) # Так как у нас тут массив то нам нужно удалить первый элемент.
        rx = random.randint(0, countBodyW -1) # Спамним рамдомно целое число в нашей области.
        ry = random.randint(0, countBodyH -1) # Эти координаты у нас идут от 0 до 20 к примеру, а нам нужно сделать как для канвы.
        self.create_image(rx*BODYSIZE, ry*BODYSIZE, anchor='nw',image=self.apple, tag='apple')


    def checkApple(self): # Поедания яблока.
        apple = self.find_withtag('apple')[0]
        head = self.find_withtag('head')
        body = self.find_withtag('body')[-1] # Делаем что бы змейка увеличивалась сразу после того как сьела яблоко.
        # Нужно проверить пересиклись ли колизии головы и яблока.
        x1, y1, x2, y2 = self.bbox(head) # Находим координаты головы.
        overlaps = self.find_overlapping(x1, y1, x2, y2) # Получаем прямоугольник в нем и будем искать обьект.
        for actor in overlaps:
            if actor == apple: # Если яблоко попало в колизию головы.
                tempx, tempy = self.coords(body) # Сохраняем координаты что бы на этом месте создать хвост.
                self.spawnApple() # Удаляем яблоко.
                self.create_image(tempx, tempy, image=self.body, anchor='nw', tag='body') # Спалмим новый хвост змеи. Указываем координаты затем изображение и выравнивание и тег.
                if self.delay > MINDELAY:
                    self.delay -= STEPDELAY


    def checkCollisions(self):
        head = self.find_withtag('head') # Координаты головы.
        body = self.find_withtag('body') # Координаты головы.
        x1, y1, x2, y2 = self.bbox(head) # Берем колизионный прямоугольник у головы.
        overlaps = self.find_overlapping(x1, y1, x2, y2) # Смотрим с чем голова пересекается.
        for b in body:
            for actor in overlaps:
                if actor == b: # Если голова столкнулась с телом.
                    self.loss = True # Пользователь столкнулся сам с собой. Ставим переменную проиграша в True.

        if x1 < 0: # Если голова вышла за левый край экрана.
            self.loss = True  # Пользователь столкнулся сам с собой. Ставим переменную проиграша в True.
        if x2 > WIDTH: # Ушел в правую область.
            self.loss = True  # Пользователь столкнулся сам с собой. Ставим переменную проиграша в True.
        if y1 < 0: # Значит что пользователь ушел в верх экрана.
            self.loss = True  # Пользователь столкнулся сам с собой. Ставим переменную проиграша в True.
        if y2 > HEIGHT: # Значит ушел вниз экрана.
            self.loss = True  # Пользователь столкнулся сам с собой. Ставим переменную проиграша в True.


    def onKeyPressed(self, event):
        key = event.keysym # Выводим клавиши.
        if key == 'Left' and self.direction != 'Right': # Если пользователь нажал влево то змейка должна поворачивать в лево. При условии что перед этим она не двигалась вправо.
            self.directiontemp = key
        elif key == 'Right' and self.direction != 'Left':
            self.directiontemp = key
        elif key == 'Up' and self.direction != 'Down':
            self.directiontemp = key
        elif key == 'Down' and self.direction != 'Up':
            self.directiontemp = key
        elif key == 'space' and self.loss: # Обратываем пробел только в том случае если игра закончилась.
            self.beginplay()


    def updateDirection(self):
        self.direction = self.directiontemp
        head = self.find_withtag('head') # Ищем голову через тег.
        headx, heady = self.coords(head) # Вытаскиваем координаты 'x','y' из головы.
        self.delete(head) # Удаляем голову. нам ее нужно перерисовать что бы голова смотрела в направлении движения.
        if self.direction == 'Left':
            self.head = ImageTk.PhotoImage(self.headImage.transpose(Image.FLIP_LEFT_RIGHT).resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
# Используем функцию transpose() что бы развернуть изображение. FLIP_LEFT_RIGHT - отзеркаливаем, Image.ANTIALIAS - сглажываем
        else:
            rotates={'Right': 0, 'Up': 90, 'Down': -90} # Указываем на сколько градусов нужно развернуть в зависимости от поворота.
            self.head = ImageTk.PhotoImage(self.headImage.rotate(rotates[self.direction]).resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.create_image(headx, heady, image=self.head, anchor='nw', tag='head')


    def timer(self):
        self.checkCollisions() # Проверяем колизию на столкновения.
        if not self.loss: # Проверяем не проиграл ли пользователь.
            self.checkApple()
            self.updateDirection() # Так же вызовем обновление движения змейки если пользователь что-то нажал.
            self.moveSnake() # Если он не проиграл то сдвигаем змейку на одну позицию. метод moveSnake создадим ниже.
            self.after(self.delay, self.timer) # Делаем что бы таймер вызывался постоянно.
        else:
            self.gameOver() # Иначе вызываем метод gameOver().


    def moveSnake(self):        
        head = self.find_withtag('head') # Грузим наше изображение.
        body = self.find_withtag('body') # Грузим наше изображение.
        items = body + head # Массив состоящий вначале из элементов body потом из элементов head.
        for i in range(len(items)-1): # Перебераем все элементы за исключением последнего. управляем мы только головой все предведущие обьекты стают на место впереди(n-1 на n).
            currentxy = self.coords(items[i]) # Смотрим текущие координаты спомощю метода coords() и передаем индентификатор обьекта который в.
            nextxy = self.coords(items[i+1]) # Координаты элемента который находится впереди.
            self.move(items[i], nextxy[0] - currentxy[0], nextxy[1] - currentxy[1]) # Указываем первым аргументом какой элемент мы двигаем, вторым на сколько двигаем.
        if self.direction == 'Left': # Голову смещаем в направлении указаным пользователем.
            self.move(head, -BODYSIZE,0) # Смещаем голову на '-BODYSIZE' так как у нас движение влево а по 'y' Не двигаем.
        elif self.direction == 'Right':
            self.move(head, BODYSIZE,0) # Смещаем голову на 1 'BODYSIZE' по 'x'.
        elif self.direction == 'Up':
            self.move(head, 0, -BODYSIZE) # Тут у нас по 'x' ничего не меняется 'y' смещаемся на квадрат вниз так как движемся в верх
        elif self.direction == 'Down':
            self.move(head, 0, BODYSIZE)


    def gameOver(self):
        body = self.find_withtag('body') # Пишем пользователю его длину змейки.
        self.delete(ALL) # Удаляем все что содержится на нашей канве.
        self.create_text(self.winfo_width()/2 , self.winfo_height()/2 - 60, text = 'Вы проиграли!', fill='white', font = 'Tahoma 30', tag='text')
        # Пишем текст в случаем проиграша пишем по центру.
        self.create_text(self.winfo_width()/2, self.winfo_height()/2, text = 'Длина змейки: ' + str(len(body) + 1), fill='white', font = 'Tahoma 30', tag='text')
        self.create_text(self.winfo_width()/2 , self.winfo_height()/2 + 60, text = 'Нажмите пробел для новой игры!', fill='white', font = 'Tahoma 30', tag='text')
        self.create_text(self.winfo_width()/2 , self.winfo_height()/2 - 260, text = 'Моя почта 9139136@gmail.com', fill='white', font = 'Tahoma 25', tag='text')
        self.create_text(self.winfo_width()/2 , self.winfo_height()/2 - 300, text = 'Данная игра была сделанна как проэкт на \'Tkinter\' для резюме.', fill='white', font = 'Tahoma 15', tag='text')


root = Tk()
root.title('Snake')
root.board = Snake() # Помещаем в рут нашу канву.
root.resizable(False, False) # Запретим расширение по высоте и ширине.
ws = root.winfo_screenwidth() # Ширина окна у пользователя.
hs = root.winfo_screenheight() # Высота окна у пользователя.
x = int(ws / 2 - WIDTH / 2) # Определяем координаты верхнего левого угла.
y = int(hs / 2 - HEIGHT / 2)
root.geometry(f'+{x}+{y}')
root.mainloop()