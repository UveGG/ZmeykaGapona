#это примерные наброски на класс корабля
class spaceship(StarWars):
    #Решение вопроса с фреймом (в процесе)
    self.kor = QtWidgets.QFrame(self.centralwidget)
    self.kor.setGeometry(QtCore.QRect(350, 700, 50, 50))
    self.kor.setAutoFillBackground(False)
    self.kor.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.kor.setFrameShadow(QtWidgets.QFrame.Raised)
    self.kor.setObjectName("kor")
