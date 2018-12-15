import time


def shoot(typ):  # Функция стрельбы в твоей компетенции
    print('hello', typ)


class Bots:
    def __init__(self, x, y, typ):
        self.typ = typ  # тип корабля бота
        self.x = x  # Координаты корабля бота
        self.y = y
        self.alive = True  # Жив ли бот
        self.move = False  # Передвижение бота по оси "x" с целью добавления экшона
        self.model()  # Модель действий бота

    def model(self):
        while self.alive:
            for i in range(2):  # Стрельба каждые 1,35 секунды ( Спорно )
                time.sleep(1.35)
                shoot(1)
            if self.move:  # Движение бота: Влево-вправо на 50 пикселей каждые 2.7 секунды (Увеличим или уменьшим позже)
                for i in range(50):
                    time.sleep(0.015)
                    self.x += 1
                self.move = False
            else:
                self.move = True
                for i in range(50):
                    time.sleep(0.015)
                    self.x -= 1

    def get_x(self):  # Возврат координат бота
        return self.x

    def get_y(self):
        return self.y


bot = Bots(80, 80, 1)
while True:
    print(1)
