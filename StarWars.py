import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap


class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.testBot = Bots(0, 0, 0, 0)
        self.shell_ss = []
        self.BotMas = [[Bots(75, -50, 0, 0), Bots(175, -50, 0, 1),
                        Bots(275, -50, 0, 2),
                        Bots(475, -50, 0, 3), Bots(575, -50, 0, 4),
                        Bots(675, -50, 0, 5), False],
                       [Bots(75, -50, 0, 0), Bots(175, -50, 0, 1),
                        Bots(275, -50, 0, 2),
                        Bots(475, -50, 0, 3), Bots(575, -50, 0, 4),
                        Bots(675, -50, 0, 5), False],
                       [Bots(75, -50, 0, 0), Bots(175, -50, 0, 1),
                        Bots(275, -50, 0, 2),
                        Bots(475, -50, 0, 3), Bots(575, -50, 0, 4),
                        Bots(675, -50, 0, 5), False],
                       [Bots(75, -50, 0, 0), Bots(175, -50, 0, 1),
                        Bots(275, -50, 0, 2),
                        Bots(475, -50, 0, 3), Bots(575, -50, 0, 4),
                        Bots(675, -50, 0, 5), False],
                       [Bots(75, -50, 0, 0), Bots(175, -50, 0, 1),
                        Bots(275, -50, 0, 2),
                        Bots(475, -50, 0, 3), Bots(575, -50, 0, 4),
                        Bots(675, -50, 0, 5), False],
                       [Bots(75, -50, 0, 0), Bots(175, -50, 0, 1),
                        Bots(275, -50, 0, 2),
                        Bots(475, -50, 0, 3), Bots(575, -50, 0, 4),
                        Bots(675, -50, 0, 5), False]
                       ]

        self.shooting_bots = QBasicTimer()  # Таймеры для ботов
        self.moving_bots = QBasicTimer()
        self.move_shell = QBasicTimer()

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

        self.shooting_bots.start(25000, self)
        self.moving_bots.start(50000, self)
        self.creating_bots.start(20000, self)  # Респавн ботов #################################################
        self.move_shell.start(200, self)
        self.respawnBots()
        self.show()

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
        if self.BotMas[idd][1].alive:
            self.BotMas[idd][1].y += 1
        if self.BotMas[idd][2].alive:
            self.BotMas[idd][2].y += 1
        if self.BotMas[idd][3].alive:
            self.BotMas[idd][3].y += 1
        if self.BotMas[idd][4].alive:
            self.BotMas[idd][4].y += 1
        if self.BotMas[idd][5].alive:
            self.BotMas[idd][5].y += 1
        # Изменения координат фреймов ##############################################################################

    def deadBot(self, id1, id2):  # Умертление бота, проверка колва живых ботов
        self.BotMas[id1][id2].alive = False
        self.BotMas[id1][id2].x = self.BotMas[id1][id2].start_x
        self.BotMas[id1][id2].y = -50
        # ОТНОСИМ ФРЕЙМ НАЗАД НА РЕСП БОТОВ ########################################################################
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


class Bots:
    def __init__(self, x, y, id1, id2):
        self.id = (id1, id2)
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
                                # ИЗМЕНЕНИЯ КООРДИНАТ ФРЕЙМОВ ##########################################################################################
                                ex.repaint()
                            print('remove bot')
                        else:
                            ex.BotMas[i][g].move = True
                            for k in range(50):
                                ex.BotMas[i][g].x -= 1
                                # ИЗМЕНЕНИЯ КООРДИНАТ ФРЕЙМОВ ##########################################################################################
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
