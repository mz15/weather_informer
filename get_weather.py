# -*- coding: utf-8 -*-

import re
from urllib.request import urlopen
import json


reg = re.compile('<body>Current IP Address: (.*)</body>')  # поиск ip-адреса
key = 'a37fae643df77aa83d88abbc9e8e96194ab242d4'  # API key


def get_ip():
    """Получить свой IP-адрес
    """
    url = 'http://checkip.dyndns.org'  # сервис для определения своего ip-адреса
    data = urlopen(url).read().decode('utf-8')
    ip = re.findall(reg, data)[0]
    return ip


def get_weather():
    """
    Получить данные по погоде
    Возвращает:
        -(dict) параметры погоды с их значениями
    """
    ip = get_ip()
    url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?' +\
          'key=' + key +\
          '&q=' + ip +\
          '&num_of_days=0' \
          '&lang=ru' \
          '&format=json'
    data = urlopen(url).read().decode('utf-8')  # считываем ответ сервиса погоды
    data = json.loads(data)  # сериализируем полученные данные
    data = data['data']['current_condition'][0]  # выбираем данные по текущей погоде
    # переводим данные в удобный для работы вид
    weather = {
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
        }
    return weather


if __name__ == '__main__':
    cur_weather = get_weather()
    print(
        '''
        Погода : %s
        Температура : %s C
        Ветер : %s км/ч %s
        Влажность : %s
        Количество осадков : %s мм
        '''
        % (cur_weather['condition'],
           cur_weather['temperature'],
           cur_weather['windSpeed'],
           cur_weather['windDirection'],
           cur_weather['humidity'],
           cur_weather['precipitation']
           ))
