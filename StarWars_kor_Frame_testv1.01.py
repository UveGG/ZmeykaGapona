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


        self.x_ss = 350
        self.y_ss = 700
        self.spaceship = QFrame(self) #Создаём фрейм с кординатами x_ss и y_ss


        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50)) #Накладываем на фрейм картинку корабля
        self.spaceship.setStyleSheet("background-image: url(test_spaceship_v2.png);")


        self.show() # Обновляем экран



    def fone(self):  # Создали лейбл, наложили как фон
        label = QLabel(self)
        label.resize(750, 800)
        stars = QPixmap('fone.jpg')
        label.setPixmap(stars)

    def center(self):  # Центрируем игру
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
