import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap



class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('StarWars')
        self.resize(750, 800)  # Размеры окна
        self.center()  # Центрируем игру
        self.fone()  # Постановка фона

        self.spaceship()



        self.show() # Обновляем экран

    def spaceship(self):
        self.x_ss = 350
        self.y_ss = 700
        self.spaceship = QFrame(self)  # Создаём фрейм с кординатами x_ss и y_ss

        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50))  # Накладываем на фрейм картинку корабля
        self.spaceship.setStyleSheet("background-image: url(test_spaceship_v2.png);")

    def fone(self):  # Создали лейбл, наложили как фон
        label = QLabel(self)
        label.resize(750, 800)
        stars = QPixmap('fone.jpg')
        label.setPixmap(stars)

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

app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
