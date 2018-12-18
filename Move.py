    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            if self.y_ss > 0:
                for i in range(7):
                    self.y_ss = self.y_ss - 1
                self.x_ss = self.x_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_S:
            if self.y_ss < 750:
                for i in range(7):
                    self.y_ss = self.y_ss + 1
                self.x_ss = self.x_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_A:
            if self.x_ss > 0:
                for i in range(7):
                    self.x_ss = self.x_ss - 1

                self.y_ss = self.y_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()

        if event.key() == Qt.Key_D:
            if self.x_ss < 700:
                for i in range(7):
                    self.x_ss = self.x_ss + 1
                self.y_ss = self.y_ss
                self.spaceship.move(self.x_ss, self.y_ss)
                self.repaint()
