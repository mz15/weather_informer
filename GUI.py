# coding: utf8

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle(self.trUtf8('Информер погоды'))
        self.resize(650, 245)
#        self.center()  # Function places the window in the center of the screen
        self.statusBar()
        self.setMinimumSize(520, 200)
        self.setMaximumSize(520, 200)
#        self.setGeometry(100, 100, 1000, 205)
        self.statusBar().showMessage('какая-нибудь информация')

        self.exit_program = QtGui.QAction(QtGui.QIcon('open.png'), 'Закрыть программу', self)
        self.exit_program.setShortcut('Ctrl+Q')
        self.exit_program.setStatusTip('Выход из программы')
        self.connect(self.exit_program, QtCore.SIGNAL('triggered()'), exit)

        """ First frame - weather icon """

        self.frame1 = QtGui.QFrame(self)
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setGeometry(15, 0, 200, 180)
        self.gridlay1 = QtGui.QGridLayout(self.frame1)

        self.group1 = QtGui.QGroupBox('Для иконки погоды:', self.frame1)  # Frame with an inscription
        self.lay1 = QtGui.QVBoxLayout(self.group1)  # Manager placement of elements in the frame
        self.gridlay1.addWidget(self.group1, 0, 0, 0, 0)

        """ First frame - weather data """

        self.frame2 = QtGui.QFrame(self)
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setGeometry(220, 0, 290, 180)
        self.gridlay2 = QtGui.QGridLayout(self.frame2)

        self.group2 = QtGui.QGroupBox('Погода в текущем городе:', self.frame2)  # Frame with an inscription
        self.lay2 = QtGui.QVBoxLayout(self.group2)  # Manager placement of elements in the frame
        self.gridlay2.addWidget(self.group2, 0, 0, 0, 0)

        self.label1 = QtGui.QLabel(self.group2)
        self.label1.setText(weather)
        self.lay2.addWidget(self.label1)

        self.label2 = QtGui.QLabel(self.group2)
        self.label2.setText(temperature)
        self.lay2.addWidget(self.label2)

        self.label3 = QtGui.QLabel(self.group2)
        self.label3.setText(wind_speed)
        self.lay2.addWidget(self.label3)

        self.label4 = QtGui.QLabel(self.group2)
        self.label4.setText(humidity)
        self.lay2.addWidget(self.label4)

        self.label5 = QtGui.QLabel(self.group2)
        self.label5.setText(precipitation)
        self.lay2.addWidget(self.label5)

weather = "<font color = blue>Погода:<\\font>"
temperature = "<font color = blue>Температура:<\\font>"
wind_speed = "<font color = blue>Скорость ветра:<\\font>"
humidity = "<font color = blue>Влажность:<\\font>"
precipitation = "<font color = blue>Осадки:<\\font>"

app = QtGui.QApplication(sys.argv)
qb = Window()
qb.show()
sys.exit(app.exec_())
