# coding: utf8

import sys
from PyQt4 import QtGui, QtCore
import get_weather

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle(self.trUtf8('Информер погоды'))
        self.resize(650, 245)
#        self.center()  # Function places the window in the center of the screen
        self.statusBar()
        self.setMinimumSize(520, 250)
        self.setMaximumSize(520, 250)
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
        self.frame1.setGeometry(15, 10, 150, 120)
        self.gridlay1 = QtGui.QGridLayout(self.frame1)

        self.group1 = QtGui.QGroupBox('Для иконки погоды:', self.frame1)  # Frame with an inscription
        self.lay1 = QtGui.QVBoxLayout(self.group1)  # Manager placement of elements in the frame
        self.gridlay1.addWidget(self.group1, 0, 0, 0, 0)

        """ First frame - weather data """

        self.frame2 = QtGui.QFrame(self)
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setGeometry(165, 10, 355, 220)
        self.gridlay2 = QtGui.QGridLayout(self.frame2)

        self.group2 = QtGui.QGroupBox('Погода в текущем городе:', self.frame2)  # Frame with an inscription
        self.lay2 = QtGui.QVBoxLayout(self.group2)  # Manager placement of elements in the frame
        self.gridlay2.addWidget(self.group2, 0, 0, 0, 0)

        self.label1 = QtGui.QLabel(self.group2)
        self.label1.setText(label_condition)
        self.lay2.addWidget(self.label1)

        self.label2 = QtGui.QLabel(self.group2)
        self.label2.setText(label_temperature)
        self.lay2.addWidget(self.label2)

        self.label3 = QtGui.QLabel(self.group2)
        self.label3.setText(label_humidity)
        self.lay2.addWidget(self.label3)

        self.label4 = QtGui.QLabel(self.group2)
        self.label4.setText(label_cloud_cover)
        self.lay2.addWidget(self.label4)

        self.label5 = QtGui.QLabel(self.group2)
        self.label5.setText(label_wind_speed)
        self.lay2.addWidget(self.label5)

        self.label6 = QtGui.QLabel(self.group2)
        self.label6.setText(label_wind_direction)
        self.lay2.addWidget(self.label6)

        self.label7 = QtGui.QLabel(self.group2)
        self.label7.setText(label_visibility)
        self.lay2.addWidget(self.label7)

        self.label8 = QtGui.QLabel(self.group2)
        self.label8.setText(label_precipitation)
        self.lay2.addWidget(self.label8)

        self.label9 = QtGui.QLabel(self.group2)
        self.label9.setText(label_pressure)
        self.lay2.addWidget(self.label9)

        self.button1 = QtGui.QPushButton('Получить данные', self)
        self.button1.setGeometry(30, 130, 120, 32)
#        self.button1.setFont(self.font2)
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.setStatusTip('Получить данные о погоде')
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.update_weather)

    def update_weather(self):
        cur_weather = get_weather.get_weather()
        if cur_weather == 0:
            # TODO вывод ошибки
            return 0

        self.label1.setText("<font color = blue>Состояние погоды: <\\font>" + cur_weather['condition'])
        self.label2.setText("<font color = blue>Температура: <\\font>" + cur_weather['temperature'] + " (°C)")
        self.label3.setText("<font color = blue>Влажность: <\\font>" + cur_weather['humidity'] + "%")
        self.label4.setText("<font color = blue>Облачность: <\\font>" + cur_weather['cloudcover'] + "%")
        self.label5.setText("<font color = blue>Скорость ветра: <\\font>" + cur_weather['windSpeed'] + " (км/ч)")
        self.label6.setText("<font color = blue>Направление ветра: <\\font>" + cur_weather['windDirection'])
        self.label7.setText("<font color = blue>Видимость: <\\font>" + cur_weather['visibility'] + " (км)")
        self.label8.setText("<font color = blue>Количество осадков: <\\font>" + cur_weather['precipitation'] + " (мм)")
        self.label9.setText("<font color = blue>Давление: <\\font>" + str(cur_weather['pressure']) + " (мм р. ст.)")

# неправильно обновляешь
label_condition = "<font color = blue>Для получения данных о погоде необходимо нажать кнопку<\\font>"
label_temperature = ""
label_humidity = ""
label_cloud_cover = ""
label_wind_speed = ""
label_wind_direction = ""
label_visibility = ""
label_precipitation = ""
label_pressure = ""


#cur_weather = get_weather.get_weather()

#label_condition = "<font color = blue>Состояние погоды: <\\font>" + cur_weather['condition']
#label_temperature = "<font color = blue>Температура: <\\font>" + cur_weather['temperature'] + " (°C)"
#label_humidity = "<font color = blue>Влажность: <\\font>" + cur_weather['humidity'] + "%"
#label_cloud_cover = "<font color = blue>Облачность: <\\font>" + cur_weather['cloudcover'] + "%"
#label_wind_speed = "<font color = blue>Скорость ветра: <\\font>" + cur_weather['windSpeed'] + " (км/ч)"
#label_wind_direction = "<font color = blue>Направление ветра: <\\font>" + cur_weather['windDirection']
#label_visibility = "<font color = blue>Видимость: <\\font>" + cur_weather['visibility'] + " (км)"
#label_precipitation = "<font color = blue>Количество осадков: <\\font>" + cur_weather['precipitation'] + " (мм)"
#label_pressure = "<font color = blue>Давление: <\\font>" + str(cur_weather['pressure']) + " (мм р. ст.)"


"""
'condition': data['lang_ru'][0]['value'],  # состояние погоды
        'temperature': data['temp_C'],  # температура (в градусах Цельсия)
        'cloudcover': data['cloudcover'],  # облачность (%)
        'humidity': data['humidity'],  # влажность(%)
        'visibility': data['visibility'],  # видимость (км)
        'image': data['weatherIconUrl'][0]['value'],  # url иконки погоды
        'windSpeed': data['windspeedKmph'],  # скорость ветра (км/ч)
        'windDirection': data['winddir16Point'],  # направление ветра (16 вариантов)
        'precipitation': data['precipMM'],  # количество осадков (мм)
        'pressure': round(int(data['pressure']) * 0.75006, 2)  # давление (в мм рт. ст.)

"""


app = QtGui.QApplication(sys.argv)
qb = Window()
qb.show()
sys.exit(app.exec_())