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
        #self.fone()  # Постановка фона

        #решение вопроса с фреймом
        #-self.kor = QtWidgets.QFrame(self.centralwidget)
        self.x_ss = 350
        self.y_ss = 350
        self.spaceship = QFrame(self)
        #self.spaceship.setGeometry(self.x_ss, self.y_ss, 50, 50)

        self.spaceship.setGeometry(QtCore.QRect(self.x_ss, self.y_ss, 50, 50))

        #self.spaceship.setStyleSheet("background-color: red")

        #self.spaceship.setStyleSheet("background-image: url(:/truck/test_spaceship_v2.png);background-repeat: no-repeat; ")

        #self.spaceship.setFrameStyle(QFrame::StyledPanel)

        #self.spaceship.setStyleSheet("background-image: url(C:\Yandex_L\ZmeykaGapona\test_spaceship_v2.png)")
        #self.spaceship.setStyleSheet("background:black;background-position: center; background-image: url(:/truck/test_spaceship_v2.png);background-repeat: no-repeat; ")

        self.show()


        #-----------------------------------------------
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
