import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap


class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.testBot = Bots(0, 0)

        self.BotMas = [[Bots(75, -50), Bots(175, -50), Bots(275, -50),
                        Bots(475, -50), Bots(575, -50),
                        Bots(675, -50), True],
                       [Bots(75, -50), Bots(175, -50), Bots(275, -50),
                        Bots(475, -50), Bots(575, -50),
                        Bots(675, -50), False],
                       [Bots(75, -50), Bots(175, -50), Bots(275, -50),
                        Bots(475, -50), Bots(575, -50),
                        Bots(675, -50), False],
                       [Bots(75, -50), Bots(175, -50), Bots(275, -50),
                        Bots(475, -50), Bots(575, -50),
                        Bots(675, -50), False],
                       [Bots(75, -50), Bots(175, -50), Bots(275, -50),
                        Bots(475, -50), Bots(575, -50),
                        Bots(675, -50), False],
                       [Bots(75, -50), Bots(175, -50), Bots(275, -50),
                        Bots(475, -50), Bots(575, -50),
                        Bots(675, -50), False]]

        self.shooting_bots = QBasicTimer()  # Таймеры для ботов
        self.moving_bots = QBasicTimer()

        self.creating_bots = QBasicTimer()  # Респавн ботов  #######################################################

        self.initUI()

    def initUI(self):
        self.setWindowTitle('StarWars')
        self.resize(750, 800)  # Размеры окна
        self.center()  # Центрируем игру
        self.fone()  # Постановка фона

        self.spaceship = QFrame(self)  # Создаём фрейм с кординатами x_ss и y_ss
        self.x_ss = 350
        self.y_ss = 700

        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50))  # Накладываем на фрейм картинку корабля
        self.spaceship.setStyleSheet("background-image: url(test_spaceship_v2.png);")

        self.shooting_bots.start(2000, self)
        self.moving_bots.start(5000, self)
        self.creating_bots.start(15000, self)  # Респавн ботов #################################################

        self.show()  # Создаем окно игры

    def shoot_ss(self):
        print('fire ss!')

    def shoot_bots(self, x, y):
        print('fire bot!')

    def fone(self):  # Создали лейбл, наложили как фон
        label = QLabel(self)
        label.resize(750, 800)
        stars = QPixmap('fone.jpg')
        label.setPixmap(stars)

    def respawnBots(self):  # Респавн ботов, вызывается когда боты умирают
        pass

    def timerEvent(self, event):
        if event.timerId() == self.shooting_bots.timerId():  # Стрельба бота
            self.testBot.shoot()
        elif event.timerId() == self.moving_bots.timerId():  # Маневрирование бота
            self.testBot.moving()

    def center(self):  # Центрируем игру
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            if self.y_ss > 0:
                for i in range(6):
                    self.y_ss = self.y_ss - 1
                self.x_ss = self.x_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_S:
            if self.y_ss < 750:
                for i in range(6):
                    self.y_ss = self.y_ss + 1
                self.x_ss = self.x_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_A:
            if self.x_ss > 0:
                for i in range(6):
                    self.x_ss = self.x_ss - 1

                self.y_ss = self.y_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_D:
            if self.x_ss < 700:
                for i in range(6):
                    self.x_ss = self.x_ss + 1
                self.y_ss = self.y_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()


class Bots:
    def __init__(self, x, y):
        self.x = x  # Координаты корабля бота
        self.y = y
        self.alive = True  # Жив ли бот
        self.move = False  # Передвижение бота по оси "x" с целью добавления экшона

    def shoot(self):
        for i in range(6):
            if ex.BotMas[i][6]:
                for g in range(6):
                    if ex.BotMas[i][g].alive:
                        ex.shoot_bots(ex.BotMas[i][g].x, ex.BotMas[i][g].y)

    def moving(self):
        for i in range(6):
            if ex.BotMas[i][6]:
                for g in range(6):
                    if ex.BotMas[i][g].alive:
                        if ex.BotMas[i][g].move:
                            ex.BotMas[i][g].move = False
                            for k in range(50):
                                ex.BotMas[i][g].x += 1
                                # ИЗМЕНЕНИЯ КООРДИНАТ ФРЕЙМОВ ##########################################################################################
                                #ex.repaint()
                            print('remove bot')
                        else:
                            ex.BotMas[i][g].move = True
                            for k in range(50):
                                ex.BotMas[i][g].x -= 1
                                # ИЗМЕНЕНИЯ КООРДИНАТ ФРЕЙМОВ ##########################################################################################
                                #ex.repaint()
                            print('move bot')


app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
