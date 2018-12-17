import time
from multiprocessing import Process
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap


def shoot(typ):  # Функция стрельбы в твоей компетенции
    print('hello', typ)


class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('StarWars')
        self.resize(750, 800)  # Размеры окна
        self.center()  # Центрируем игру
        self.fone()  # Постановка фона

        self.timer = QBasicTimer()
        self.timer.start(1000, self)

        self.x_ss = 350
        self.y_ss = 700
        self.spaceship = QFrame(self)  # Создаём фрейм с кординатами x_ss и y_ss
        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50))  # Накладываем на фрейм картинку корабля
        self.spaceship.setStyleSheet("background-image: url(test_spaceship_v2.png);")
        #self.bot1 = Bots(50, 50, 1)
        #self.bot2 = Bots(150, 50, 2)

        self.show()  # Создаем окно игры

    def fone(self):  # Создали лейбл, наложили как фон
        label = QLabel(self)
        label.resize(750, 800)
        stars = QPixmap('fone.jpg')
        label.setPixmap(stars)

    def timerEvent(self, event):
        print(event.timerld())
        print(self.timer.timerId())

    def center(self):  # Центрируем игру
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            if self.y_ss > 0:
                self.y_ss = self.y_ss - 10
                self.x_ss = self.x_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_S:
            if self.y_ss < 750:
                self.y_ss = self.y_ss + 10
                self.x_ss = self.x_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_A:
            if self.x_ss > 0:
                self.x_ss = self.x_ss - 10
                self.y_ss = self.y_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_D:
            if self.x_ss < 700:
                self.x_ss = self.x_ss + 10
                self.y_ss = self.y_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()


class Bots:
    def __init__(self, x, y, typ):
        self.typ = typ  # тип корабля бота
        self.x = x  # Координаты корабля бота
        self.y = y
        self.alive = True  # Жив ли бот
        self.move = False  # Передвижение бота по оси "x" с целью добавления экшона

    def model(self):
        print('why dont you work?')  # Он до сюда не доходит
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


app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
