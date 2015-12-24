# coding: utf8

import sys
from PyQt4 import QtGui, QtCore
import get_weather

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle(self.trUtf8('Информер погоды'))
#        self.resize(520, 245)
#        self.setGeometry(100, 100, 1000, 205)
#        self.center()  # Function places the window in the center of the screen
        self.setMinimumSize(520, 245)
        self.setMaximumSize(520, 245)
        self.statusBar()
#        self.statusBar().showMessage('статус-бар')

        """ First frame - weather icon """

        self.frame1 = QtGui.QFrame(self)
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setGeometry(15, 10, 150, 165)
        self.gridlay1 = QtGui.QGridLayout(self.frame1)

        self.group1 = QtGui.QGroupBox('Для иконки погоды:', self.frame1)  # Frame with an inscription
        self.lay1 = QtGui.QVBoxLayout(self.group1)  # Manager placement of elements in the frame
        self.gridlay1.addWidget(self.group1, 0, 0, 0, 0)

        # TODO иконка погоды

        """ First frame - weather data """

        self.frame2 = QtGui.QFrame(self)
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setGeometry(165, 10, 355, 220)
        self.gridlay2 = QtGui.QGridLayout(self.frame2)

        self.group2 = QtGui.QGroupBox('Погода в текущем городе:', self.frame2)  # Frame with an inscription
        self.lay2 = QtGui.QVBoxLayout(self.group2)  # Manager placement of elements in the frame
        self.gridlay2.addWidget(self.group2, 0, 0, 0, 0)

        self.label_condition = QtGui.QLabel(self.group2)
        self.label_condition.setText(condition)
        self.lay2.addWidget(self.label_condition)

        self.label_temperature = QtGui.QLabel(self.group2)
        self.label_temperature.setText(temperature)
        self.lay2.addWidget(self.label_temperature)

        self.label_humidity = QtGui.QLabel(self.group2)
        self.label_humidity.setText(humidity)
        self.lay2.addWidget(self.label_humidity)

        self.label_cloud_cover = QtGui.QLabel(self.group2)
        self.label_cloud_cover.setText(cloud_cover)
        self.lay2.addWidget(self.label_cloud_cover)

        self.label_wind_speed = QtGui.QLabel(self.group2)
        self.label_wind_speed.setText(wind_speed)
        self.lay2.addWidget(self.label_wind_speed)

        self.label_wind_direction = QtGui.QLabel(self.group2)
        self.label_wind_direction.setText(wind_direction)
        self.lay2.addWidget(self.label_wind_direction)

        self.label_visibility = QtGui.QLabel(self.group2)
        self.label_visibility.setText(visibility)
        self.lay2.addWidget(self.label_visibility)

        self.label_precipitation = QtGui.QLabel(self.group2)
        self.label_precipitation.setText(precipitation)
        self.lay2.addWidget(self.label_precipitation)

        self.label_pressure = QtGui.QLabel(self.group2)
        self.label_pressure.setText(pressure)
        self.lay2.addWidget(self.label_pressure)

        self.button1 = QtGui.QPushButton('Получить данные', self)
        self.button1.setGeometry(30, 180, 120, 32)
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.setStatusTip('Получить данные о погоде. Местоположение будет определено по Вашему IP-адресу.')
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.update_weather)

    def update_weather(self):

        cur_weather = get_weather.get_weather()
        if cur_weather == 0:

            global condition, temperature, humidity, cloud_cover, wind_speed, wind_direction, visibility,\
                precipitation, pressure

            self.label_condition.setText("<font color = grey>Ошибка. Проверьте подключение к Интернету.<\\font>")
            self.label_temperature.setText("")
            self.label_humidity.setText("")
            self.label_cloud_cover.setText("")
            self.label_wind_speed.setText("")
            self.label_wind_direction.setText("")
            self.label_visibility.setText("")
            self.label_precipitation.setText("")
            self.label_pressure.setText("")

            return 0

        self.label_condition.setText("<font color = blue>Состояние погоды: <\\font>"
                                     + cur_weather['condition'])
        self.label_temperature.setText("<font color = blue>Температура: <\\font>"
                                       + cur_weather['temperature'] + " (°C)")
        self.label_humidity.setText("<font color = blue>Влажность: <\\font>"
                                    + cur_weather['humidity'] + "%")
        self.label_cloud_cover.setText("<font color = blue>Облачность: <\\font>"
                                       + cur_weather['cloudcover'] + "%")
        self.label_wind_speed.setText("<font color = blue>Скорость ветра: <\\font>"
                                      + cur_weather['windSpeed'] + " (км/ч)")
        self.label_wind_direction.setText("<font color = blue>Направление ветра: <\\font>"
                                          + cur_weather['windDirection'])
        self.label_visibility.setText("<font color = blue>Видимость: <\\font>"
                                      + cur_weather['visibility'] + " (км)")
        self.label_precipitation.setText("<font color = blue>Количество осадков: <\\font>"
                                         + cur_weather['precipitation'] + " (мм)")
        self.label_pressure.setText("<font color = blue>Давление: <\\font>"
                                    + str(cur_weather['pressure']) + " (мм р. ст.)")

    def closeEvent(self, event):  # Confirmation of exit

        """ Message Box opens to confirm the exit from the program. """

        reply = QtGui.QMessageBox.question(self, self.trUtf8('Закрытие программы'),
                                           self.trUtf8("Вы уверены что хотите выйти?"),
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        event.accept() if reply == QtGui.QMessageBox.Yes else event.ignore()

condition = "<font color = grey>Для получения данных о погоде необходимо нажать кнопку<\\font>"
temperature = ""
humidity = ""
cloud_cover = ""
wind_speed = ""
wind_direction = ""
visibility = ""
precipitation = ""
pressure = ""

app = QtGui.QApplication(sys.argv)
qb = Window()
qb.show()
sys.exit(app.exec_())
