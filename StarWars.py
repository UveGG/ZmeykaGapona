import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPixmap, QFont


class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()

        self.snaryad_b = 1
        self.snaryad_ss = 1
        self.snaryad = 1  # Для pep8
        self.now_score = 10

        with open('info.txt') as f:
            info = f.read()
            mas = info.split()
            self.record = mas[0]
            self.score = 0
            self.ss_typ = mas[1]

        self.fone = QLabel(self)
        self.fone.resize(750, 800)
        self.fone.setPixmap(QPixmap('veider.jpg'))

        self.start = QPushButton(self)
        self.ship = QPushButton(self)  # Менюшка
        self.reset = QPushButton(self)

        self.tab = QLabel(self)  # Тоже для меню

        self.main_menue()  # Создаем меню

        self.testBot = Bots(0, -50, -200, -200, QFrame(self), self)  # Боты
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

        self.spaceship = QFrame(self)  # Создаём фрейм с кординатами x_ss и y_ss
        self.x_ss = 350
        self.y_ss = 700

        self.shell_ss = []
        self.shell_bots = []  # Главный кораблик
        self.hp_ss = 100

        self.shooting_bots = QBasicTimer()  # Таймеры для ботов
        self.moving_bots = QBasicTimer()
        self.move_shell = QBasicTimer()
        self.shell_registr = QBasicTimer()
        self.creating_bots = QBasicTimer()  # Респавн ботов

        self.ship1 = QPushButton(self)
        self.ship2 = QPushButton(self)  # Для меню
        self.ship3 = QPushButton(self)

        self.ship1.hide()
        self.ship2.hide()
        self.ship3.hide()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('StarWars')
        self.resize(750, 800)  # Размеры окна
        self.center()  # Центрируем игру

    def main_menue(self):
        self.tab.move(30, 10)
        self.tab.resize(720, 100)
        self.tab.setText(self.record)
        self.tab.setFont(QFont('SansSerif', 45))
        self.tab.setStyleSheet("color: rgb(255, 255, 0);")

        self.start.resize(200, 50)
        self.ship.resize(200, 50)
        self.reset.resize(200, 50)

        self.start.move(275, 475)
        self.ship.move(525, 475)
        self.reset.move(25, 475)

        self.start.setStyleSheet("background-image: url(start.jpg);")
        self.ship.setStyleSheet("background-image: url(ship.jpg);")
        self.reset.setStyleSheet("background-image: url(reset.jpg);")

        self.start.clicked.connect(self.menue_start)
        self.reset.clicked.connect(self.menue_reset)
        self.ship.clicked.connect(self.menue_ship)

    def menue_start(self):
        self.tab.setText(str(self.now_score))
        self.fone.setPixmap(QPixmap('stars.jpg'))
        self.reset.hide()
        self.start.hide()
        self.ship.hide()

        for id1 in range(6):
            for id2 in range(6):
                self.BotMas[id1][id2].frame.show()

        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50))
        self.spaceship.setStyleSheet("background-image: url(" + self.ss_typ + ");")
        self.repaint()

        self.shooting_bots.start(6000, self)
        self.moving_bots.start(12000, self)
        self.creating_bots.start(30000, self)  # Респавн ботов
        self.move_shell.start(10, self)
        self.shell_registr.start(15, self)
        self.respawnBots()

    def menue_reset(self):
        with open('info.txt', mode='w') as f:
            f.write('0 \n' + self.ss_typ)
        self.tab.setText('0')

    def menue_ship(self):
        self.reset.hide()
        self.start.hide()
        self.ship.hide()

        self.ship1.resize(50, 50)
        self.ship2.resize(50, 50)
        self.ship3.resize(50, 50)

        self.ship1.move(100, 475)
        self.ship2.move(345, 475)
        self.ship3.move(575, 475)

        self.ship1.setStyleSheet("background-image: url(spaceship_1.png);")
        self.ship2.setStyleSheet("background-image: url(spaceship_2.png);")
        self.ship3.setStyleSheet("background-image: url(spaceship_3.png);")

        self.ship1.clicked.connect(self.choose1)
        self.ship2.clicked.connect(self.choose2)
        self.ship3.clicked.connect(self.choose3)

        self.ship1.show()
        self.ship2.show()
        self.ship3.show()

    def choose1(self):
        self.ss_typ = "spaceship_1.png"

        with open('info.txt', mode='w') as f:
            f.write(self.record + '\n' + self.ss_typ)

        self.ship1.hide()
        self.ship2.hide()
        self.ship3.hide()

        self.reset.show()
        self.start.show()
        self.ship.show()

    def choose2(self):
        self.ss_typ = 'spaceship_2.png'

        with open('info.txt', mode='w') as f:
            f.write(self.record + '\n' + self.ss_typ)

        self.ship1.hide()
        self.ship2.hide()
        self.ship3.hide()

        self.reset.show()
        self.start.show()
        self.ship.show()

    def choose3(self):
        self.ss_typ = 'spaceship_3.png'

        with open('info.txt', mode='w') as f:
            f.write(self.record + '\n' + self.ss_typ)

        self.ship1.hide()
        self.ship2.hide()
        self.ship3.hide()

        self.reset.show()
        self.start.show()
        self.ship.show()

    def repaint_score(self):
        self.now_score += 10
        self.tab.setText(str(self.now_score))
        self.repaint()
        if self.now_score > int(self.record):
            with open('info.txt', mode='w') as f:
                f.write(str(self.now_score) + '\n' + self.ss_typ)

    def shoot_bots(self, x, y):
        self.snaryad_b = Shell_bots(self, x, y, 1)
        self.shell_bots.append(self.snaryad_b)
        self.snaryad_b.show()

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
                        for j in range(6):
                            if self.BotMas[g][j].alive:
                                self.BotMas[g][j].y += 1
                                self.BotMas[g][j].frame.move(self.BotMas[g][j].x, self.BotMas[g][j].y)

                    self.repaint()

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

        elif event.timerId() == self.move_shell.timerId():

            if len(self.shell_ss) > 0:
                for u in range(len(self.shell_ss)):
                    self.shell_ss[u].mover()
                    self.repaint()

                for j in range(len(self.shell_ss)):
                    if self.shell_ss[j].stats_y() <= 10:
                        self.shell_ss[j].d_f()
                        self.repaint()

            if len(self.shell_bots) > 0:
                for u in range(len(self.shell_bots)):
                    self.shell_bots[u].mover()
                    self.repaint()

                for j in range(len(self.shell_bots)):
                    if self.shell_bots[j].stats_y() >= 800:
                        self.shell_bots[j].d_f()
                        self.repaint()

        elif event.timerId() == self.shell_registr.timerId():

            if len(self.shell_bots) > 0:

                for j in range(len(self.shell_bots)):

                    self.A1_bots = (int(self.y_ss + 25) - int(self.shell_bots[j].stats_y())) ** 2

                    self.A2_bots = (int(self.x_ss + 25) - int(self.shell_bots[j].stats_x())) ** 2
                    self.d_bots = (self.A1_bots + self.A2_bots) ** 0.5
                    self.R_bots = 25 + 8 + 3
                    #print(self.R_bots, self.d_bots)
                    if self.d_bots <= self.R_bots:
                        if self.shell_bots[j].hit() == 0:
                            self.hp_ss -= 10
                            print('Sergii pidor', self.hp_ss)
                            self.shell_bots[j].d_f()


            #if len(self.shell_ss) > 0:

            #    for j in range(len(self.shell_ss)):

            #        self.A1_ss = (int(self.y_ss + 25) - int(self.shell_bots[j].stats_y())) ** 2
            #
            #        self.A2_ss = (int(self.x_ss + 25) - int(self.shell_bots[j].stats_x())) ** 2
            #        self.d_ss = (self.A1_bots + self.A2_bots) ** 0.5
            #        self.R_ss = 25 + 8 + 3
            #        #print(self.R_bots, self.d_bots)
            #        if self.d_bots <= self.R_bots:
            #            if self.shell_bots[j].hit() == 0:
            #                self.hp_ss -= 10
            #                print('Sergii pidor', self.hp_ss)
            #                self.shell_ss[j].d_f()


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

        if event.key() == Qt.Key_F:
            self.snaryad_ss = Shell_ss(self, self.x_ss, self.y_ss, 1)
            self.snaryad_ss.show()
            self.shell_ss.append(self.snaryad_ss)


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
                        else:
                            ex.BotMas[i][g].move = True
                            for k in range(50):
                                ex.BotMas[i][g].x -= 1
                                ex.BotMas[i][g].frame.move(ex.BotMas[i][g].x, ex.BotMas[i][g].y)
                                ex.repaint()


class Shell_ss(QFrame):
    def __init__(self, form, x, y, type_shell):
        super().__init__(form)
        self.x = x + 25
        self.y = y + 1
        self.type_shell = type_shell
        self.dont_move = 0
        self.hitt = 0
        self.setGeometry(QtCore.QRect(self.x, self.y, 3, 3))
        self.setStyleSheet("background-color: red")

    def stats_y(self):
        return self.y

    def stats_x(self):
        return self.x

    def hit(self):
        return self.hitt

    def d_f(self):
        self.move(1, 1)
        self.hide()
        self.dont_move = 1
        self.hitt = 1

    def mover(self):
        if self.dont_move == 0:
            self.y -= 5
            self.move(self.x, self.y)


class Shell_bots(QFrame):
    def __init__(self, form, x, y, type_shell):
        super().__init__(form)
        self.x = x + 25
        self.y = y + 51
        self.type_shell = type_shell
        self.dont_move = 0
        self.hitt = 0
        self.setGeometry(QtCore.QRect(self.x, self.y, 3, 3))
        self.setStyleSheet("background-color: red")

    def stats_y(self):
        return self.y

    def stats_x(self):
        return self.x

    def hit(self):
        return self.hitt

    def d_f(self):
        self.move(1, 1)
        self.hide()
        self.hitt = 1
        self.dont_move = 1

    def mover(self):
        if self.dont_move == 0:
            self.y += 5
            self.move(self.x, self.y)


app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
