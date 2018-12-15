import sys, random

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

class StarWars(QMainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi('StarWarsui.ui', self)
        self.initUI()

    def initUI(self):

        #self.stars = Stars(self)
        #self.setCentralWidget(self.stars)

        #self.stars.start()

        self.resize(750, 800)
        self.center()
        self.setWindowTitle('StarWars')
        self.setStyleSheet("background-image:url(\"fone.jpg\"); background-position: center;" )
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)



app = QApplication(sys.argv)
ex = StarWars()
ex.show()
sys.exit(app.exec_())
