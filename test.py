import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap


class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_menue()  # Создаем меню (Рабочее)
        self.testBot = Bots(0, -50, -200, -200, QFrame(self), self)
        self.shell_ss = []
        self.BotMas = [[Bots(75, -50, 0, 0, QFrame(self), self),
                        Bots(175, -50, 0, 1, QFrame(self), self),
                        Bots(275, -50, 0, 2, QFrame(self), self),
                        Bots(475, -50, 0, 3, QFrame(self), self),
                        Bots(575, -50, 0, 4, QFrame(self), self),
                        Bots(675, -50, 0, 5, QFrame(self), self), False],
                       [Bots(75, -50, 0, 0, QFrame(self), self),
                        Bots(175, -50, 0, 1, QFrame(self), self),
                        Bots(275, -50, 0, 2, QFrame(self), self),
                        Bots(475, -50, 0, 3, QFrame(self), self),
                        Bots(575, -50, 0, 4, QFrame(self), self),
                        Bots(675, -50, 0, 5, QFrame(self), self), False],
                       [Bots(75, -50, 0, 0, QFrame(self), self),
                        Bots(175, -50, 0, 1, QFrame(self), self),
                        Bots(275, -50, 0, 2, QFrame(self), self),
                        Bots(475, -50, 0, 3, QFrame(self), self),
                        Bots(575, -50, 0, 4, QFrame(self), self),
                        Bots(675, -50, 0, 5, QFrame(self), self), False],
                       [Bots(75, -50, 0, 0, QFrame(self), self),
                        Bots(175, -50, 0, 1, QFrame(self), self),
                        Bots(275, -50, 0, 2, QFrame(self), self),
                        Bots(475, -50, 0, 3, QFrame(self), self),
                        Bots(575, -50, 0, 4, QFrame(self), self),
                        Bots(675, -50, 0, 5, QFrame(self), self), False],
                       [Bots(75, -50, 0, 0, QFrame(self), self),
                        Bots(175, -50, 0, 1, QFrame(self), self),
                        Bots(275, -50, 0, 2, QFrame(self), self),
                        Bots(475, -50, 0, 3, QFrame(self), self),
                        Bots(575, -50, 0, 4, QFrame(self), self),
                        Bots(675, -50, 0, 5, QFrame(self), self), False],
                       [Bots(75, -50, 0, 0, QFrame(self), self),
                        Bots(175, -50, 0, 1, QFrame(self), self),
                        Bots(275, -50, 0, 2, QFrame(self), self),
                        Bots(475, -50, 0, 3, QFrame(self), self),
                        Bots(575, -50, 0, 4, QFrame(self), self),
                        Bots(675, -50, 0, 5, QFrame(self), self), False]
                       ]

        self.shooting_bots = QBasicTimer()  # Таймеры для ботов
        self.moving_bots = QBasicTimer()
        self.move_shell = QBasicTimer()

        self.creating_bots = QBasicTimer()  # Респавн ботов

        self.ss_typ = 'spaceship_1.png'  # Типы кораблей


        self.start.clicked.connect(self.menue_start())
        self.reset.clicked.connect(self.menue_reset())
        self.game_started = False
        while not self.game_started:
            a = 1

        self.initUI()

    def initUI(self):
        self.setWindowTitle('StarWars')
        self.resize(750, 800)  # Размеры окна
        self.center()  # Центрируем игру

        for id1 in range(6):
            for id2 in range(6):
                self.BotMas[id1][id2].frame.show()

        self.spaceship = QFrame(self)  # Создаём фрейм с кординатами x_ss и y_ss
        self.x_ss = 350
        self.y_ss = 700

        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50))  # Накладываем на фрейм картинку корабля
        self.spaceship.setStyleSheet("background-image: url(" + self.ss_typ + ");")

        self.shooting_bots.start(2500, self)
        self.moving_bots.start(7500, self)
        self.creating_bots.start(20000, self)  # Респавн ботов
        self.move_shell.start(200, self)
        self.respawnBots()
        self.show()

    def shoot_ss(self):
        print('fire ss!')

    def shoot_bots(self, x, y):
        print('fire bot!')

    def main_menue(self):
        self.fone(2)  # Постановка фона меню

        self.start = QLabel(self)
        self.ship = QLabel(self)
        self.reset = QLabel(self)

        self.start.resize(200, 50)
        self.ship.resize(200, 50)
        self.reset.resize(200, 50)

        self.start.move(275, 475)
        self.ship.move(525, 475)
        self.reset.move(25, 475)

        self.start.setPixmap(QPixmap('start.jpg'))
        self.ship.setPixmap(QPixmap('ship.jpg'))
        self.reset.setPixmap(QPixmap('reset.jpg'))

    def menue_start(self):
        self.game_started = True  # Когда кораблик умрет не забудь поменять #################################################

    def menue_ship(self):  # Создать менюшку выбора корабля
        pass

    def menue_reset(self):  # Сбросить очки
        pass

    def fone(self, typ):  # Создали лейбл, наложили как фон
        label = QLabel(self)
        label.resize(750, 800)
        if typ == 1:
            background = QPixmap('stars.jpg')
        else:
            background = QPixmap('veider.jpg')
        label.setPixmap(background)

    def respawnBots(self):  # Респавн ботов, вызывается когда боты умирают
        respawned = False
        for i in range(6):
            if not self.BotMas[i][6]:
                self.BotMas[i][6] = True  # Added = True
                respawned = True
                break
        if respawned:
            for i in range(100):  # Увеличивает "y" всех живых ботов на 100
                for g in range(6):
                    if self.BotMas[g][6]:
                        self.respawnHelp(g)
                    self.repaint()

    def respawnHelp(self, idd):
        if self.BotMas[idd][0].alive:
            self.BotMas[idd][0].y += 1
            self.BotMas[idd][0].frame.move(self.BotMas[idd][0].x, self.BotMas[idd][0].y)
        if self.BotMas[idd][1].alive:
            self.BotMas[idd][1].y += 1
            self.BotMas[idd][1].frame.move(self.BotMas[idd][1].x, self.BotMas[idd][1].y)
        if self.BotMas[idd][2].alive:
            self.BotMas[idd][2].y += 1
            self.BotMas[idd][2].frame.move(self.BotMas[idd][2].x, self.BotMas[idd][2].y)
        if self.BotMas[idd][3].alive:
            self.BotMas[idd][3].y += 1
            self.BotMas[idd][3].frame.move(self.BotMas[idd][3].x, self.BotMas[idd][3].y)
        if self.BotMas[idd][4].alive:
            self.BotMas[idd][4].y += 1
            self.BotMas[idd][4].frame.move(self.BotMas[idd][4].x, self.BotMas[idd][4].y)
        if self.BotMas[idd][5].alive:
            self.BotMas[idd][5].y += 1
            self.BotMas[idd][5].frame.move(self.BotMas[idd][5].x, self.BotMas[idd][5].y)
        # Изменения координат фреймов ##############################################################################

    def deadBot(self, id1, id2):  # Умертление бота, проверка колва живых ботов
        self.BotMas[id1][id2].alive = False
        self.BotMas[id1][id2].x = self.BotMas[id1][id2].start_x
        self.BotMas[id1][id2].y = -50
        self.BotMas[id1][id2].frame.move(ex.BotMas[id1][id2].x, -50)
        self.repaint()
        add = False
        for i in range(6):
            if self.BotMas[id1][i].alive:
                add = True
                break
        self.BotMas[id1][6] = add
        if not add:  # Формально возвращаем их к жизни на их респавне
            for i in self.BotMas[id1]:
                i.alive = True

    def timerEvent(self, event):
        if event.timerId() == self.shooting_bots.timerId():  # Стрельба бота
            self.testBot.shoot()
        elif event.timerId() == self.moving_bots.timerId():  # Маневрирование бота
            self.testBot.moving()
        elif event.timerId() == self.creating_bots.timerId():
            self.respawnBots()
        elif event.timerId == self.move_shell.timerId():
            for u in len(self.shell_ss):
                self.shell_ss[u].mover()
                self.repaint()

    def center(self):  # Центрируем игру
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

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

        if event.key() == Qt.Key_Space:
            self.snaryad = Shell_ss(self, self.x_ss, self.y_ss, 1)
            self.snaryad.show()
            self.shell_ss.append(self.snaryad)
            print("draw")


class Bots(QFrame):
    def __init__(self, x, y, id1, id2, frame, form):
        super().__init__(form)
        self.id = (id1, id2)
        self.frame = frame
        self.frame.setGeometry(QtCore.QRect(x, y, 50, 50))
        self.frame.setStyleSheet("background-image: url(bot_spaceship.png);")
        self.frame.show()
        self.start_x = x
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
                                ex.BotMas[i][g].frame.move(ex.BotMas[i][g].x, ex.BotMas[i][g].y)
                                ex.repaint()
                            print('remove bot')
                        else:
                            ex.BotMas[i][g].move = True
                            for k in range(50):
                                ex.BotMas[i][g].x -= 1
                                ex.BotMas[i][g].frame.move(ex.BotMas[i][g].x, ex.BotMas[i][g].y)
                                ex.repaint()
                            print('move bot')


class Shell_ss(QFrame):
    def __init__(self, form, x, y, type_shell):
        super().__init__(form)
        self.x = x + 25
        self.y = y + 1
        self.type_shell = type_shell

        self.setGeometry(QtCore.QRect(self.x, self.y, 2, 2))
        self.setStyleSheet("background-color: red")

    def mover(self):
        self.x += 5
        self.move(self.x, self.y)
        print(228)


app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
