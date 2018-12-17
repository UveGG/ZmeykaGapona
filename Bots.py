import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap


class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()

        self.bot1 = Bots(75, -50, 1)  # Перворожденные боты ######################################################
        self.bot2 = Bots(175, -50, 1)
        self.bot3 = Bots(275, -50, 1)
        self.bot4 = Bots(475, -50, 1)  # Вместо переменных можно сделать двухмерный массив #######################
        self.bot5 = Bots(575, -50, 1)
        self.bot6 = Bots(675, -50, 1)

        self.shooting_1 = QBasicTimer()  # Таймеры для ботов
        self.moving_1 = QBasicTimer()

        self.shooting_2 = QBasicTimer()
        self.moving_2 = QBasicTimer()

        self.shooting_3 = QBasicTimer()
        self.moving_3 = QBasicTimer()

        self.shooting_4 = QBasicTimer()
        self.moving_4 = QBasicTimer()

        self.shooting_5 = QBasicTimer()
        self.moving_5 = QBasicTimer()

        self.shooting_6 = QBasicTimer()
        self.moving_6 = QBasicTimer()

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

        self.creating_bots.start(15000, self)  # Респавн ботов #################################################

        self.initBots()

        self.show()  # Создаем окно игры

    def shoot(self):  # Функция стрельбы в твоей компетенции ###########################################################
        print('Стреляю')

    def fone(self):  # Создали лейбл, наложили как фон
        label = QLabel(self)
        label.resize(750, 800)
        stars = QPixmap('fone.jpg')
        label.setPixmap(stars)

    def initBots(self):  # Создание ботов
        self.bot1 = Bots(75, -50, 1)
        self.bot2 = Bots(175, -50, 1)
        self.bot3 = Bots(275, -50, 1)
        self.bot4 = Bots(475, -50, 1)
        self.bot5 = Bots(575, -50, 1)
        self.bot6 = Bots(675, -50, 1)

        for i in range(100):
            self.bot1.y += 1
            self.bot2.y += 1
            self.bot3.y += 1
            self.bot4.y += 1
            self.bot5.y += 1
            self.bot6.y += 1  # Можно поэксперементировать с += ###########################################
            self.repaint()

        self.shooting_1.start(1350, self)  # Включаем таймеры для ботов
        self.moving_1.start(2700, self)

        self.shooting_2.start(1350, self)
        self.moving_2.start(2700, self)

        self.shooting_3.start(1350, self)
        self.moving_3.start(2700, self)

        self.shooting_4.start(1350, self)
        self.moving_4.start(2700, self)

        self.shooting_5.start(1350, self)
        self.moving_5.start(2700, self)

        self.shooting_6.start(1350, self)
        self.moving_6.start(2700, self)

    def timerEvent(self, event):
        if event.timerId() == self.shooting_1.timerId():  # Стрельба бота
            if self.bot1.alive:
                self.shoot()  # Стрельба, от середины корабля перпендикулярно вниз летит снаряд. ####################
            else:
                self.shooting_1.end()
        elif event.timerId() == self.moving_1.timerId():  # Маневрирование бота
            if self.bot1.alive:
                if self.bot1.move:
                    self.bot1.move = False
                    for i in range(50):
                        self.bot1.x += 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
                else:
                    self.bot1.move = True
                    for i in range(50):
                        self.bot1.x -= 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
            else:
                self.moving_1.end()
        elif event.timerId() == self.shooting_2.timerId():  # Стрельба бота
            if self.bot2.alive:
                self.shoot()  # Стрельба, от середины корабля перпендикулярно вниз летит снаряд. ####################
            else:
                self.shooting_2.end()
        elif event.timerId() == self.moving_2.timerId():  # Маневрирование бота
            if self.bot2.alive:
                if self.bot2.move:
                    self.bot2.move = False
                    for i in range(50):
                        self.bot2.x += 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
                else:
                    self.bot2.move = True
                    for i in range(50):
                        self.bot2.x -= 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
            else:
                self.moving_2.end()
        elif event.timerId() == self.shooting_3.timerId():  # Стрельба бота
            if self.bot3.alive:
                self.shoot()  # Стрельба, от середины корабля перпендикулярно вниз летит снаряд. ####################
            else:
                self.shooting_3.end()
        elif event.timerId() == self.moving_3.timerId():  # Маневрирование бота
            if self.bot3.alive:
                if self.bot3.move:
                    self.bot3.move = False
                    for i in range(50):
                        self.bot3.x += 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
                else:
                    self.bot3.move = True
                    for i in range(50):
                        self.bot3.x -= 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
            else:
                self.moving_3.end()
        elif event.timerId() == self.shooting_4.timerId():  # Стрельба бота
            if self.bot4.alive:
                self.shoot()  # Стрельба, от середины корабля перпендикулярно вниз летит снаряд. ####################
            else:
                self.shooting_4.end()
        elif event.timerId() == self.moving_4.timerId():  # Маневрирование бота
            if self.bot4.alive:
                if self.bot4.move:
                    self.bot4.move = False
                    for i in range(50):
                        self.bot4.x += 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
                else:
                    self.bot4.move = True
                    for i in range(50):
                        self.bot4.x -= 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
            else:
                self.moving_4.end()
        elif event.timerId() == self.shooting_5.timerId():  # Стрельба бота
            if self.bot5.alive:
                self.shoot()  # Стрельба, от середины корабля перпендикулярно вниз летит снаряд. ####################
            else:
                self.shooting_5.end()
        elif event.timerId() == self.moving_5.timerId():  # Маневрирование бота
            if self.bot5.alive:
                if self.bot5.move:
                    self.bot5.move = False
                    for i in range(50):
                        self.bot5.x += 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
                else:
                    self.bot5.move = True
                    for i in range(50):
                        self.bot5.x -= 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
            else:
                self.moving_5.end()
        elif event.timerId() == self.shooting_6.timerId():  # Стрельба бота
            if self.bot6.alive:
                self.shoot()  # Стрельба, от середины корабля перпендикулярно вниз летит снаряд. ####################
            else:
                self.shooting_6.end()
        elif event.timerId() == self.moving_6.timerId():  # Маневрирование бота
            if self.bot6.alive:
                if self.bot6.move:
                    self.bot6.move = False
                    for i in range(50):
                        self.bot6.x += 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
                else:
                    self.bot6.move = True
                    for i in range(50):
                        self.bot6.x -= 1  # Можно поэксперементировать с += ###########################################
                        self.repaint()
            else:
                self.moving_6.end()

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
        self.typ = typ  # тип корабля бота  ################################################################
        self.x = x  # Координаты корабля бота
        self.y = y
        self.alive = True  # Жив ли бот
        self.move = False  # Передвижение бота по оси "x" с целью добавления экшона


app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
