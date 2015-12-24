# -*- coding: utf-8 -*-

from urllib.request import urlopen
import json
import re
import logging as log

log.basicConfig(format='%(asctime)s: %(message)s', level=log.DEBUG)  # конфигурация логирования
urlIPService = 'http://checkip.dyndns.org'  # сервис для определения своего ip-адреса
reIP = re.compile('<body>Current IP Address: (.*)</body>')  # поиск ip-адреса на странице
key = 'a37fae643df77aa83d88abbc9e8e96194ab242d4'  # API key для сервиса погоды
dirImg = 'img.png'  # путь сохранения изображения
ip = ''

def get_ip():

    """ Получить свой IP-адрес """

    global ip
    log.debug('Запрос на получение IP-адреса')

    try:
        data = urlopen(urlIPService).read().decode('utf-8')
    except IOError:
        log.error('Сервер вернул ошибку')
        return ''

    ip = re.findall(reIP, data)[0]
    log.debug('IP-адрес: %s' % ip)
    return ip

def get_weather():

    """
    Получить данные по погоде
    Возвращает:
        -(dict) параметры погоды с их значениями
    """

    global ip
    if len(ip) == 0:
        ip = get_ip()
    if ip == '':  # если не получили ip-адрес
        return 0
    url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?' +\
          'key=' + key +\
          '&q=' + ip +\
          '&num_of_days=0' \
          '&lang=ru' \
          '&format=json'
    log.debug('Запрос на получение информации по погоде')
    try:
        data = urlopen(url).read().decode('utf-8')  # считываем ответ сервиса погоды
    except IOError:
        log.error('Сервер вернул ошибку')
        return 0
    log.debug('Получена информация по погоде')
    data = json.loads(data)  # сериализируем полученные данные
    data = data['data']['current_condition'][0]  # выбираем данные по текущей погоде

    # переводим данные в удобный для работы вид
    weather = {
        'condition': data['lang_ru'][0]['value'],  # состояние погоды
        'temperature': data['temp_C'],  # температура (в градусах Цельсия)
        'cloudcover': data['cloudcover'],  # облачность (%)
        'humidity': data['humidity'],  # влажность(%)
        'visibility': data['visibility'],  # видимость (км)
        'windSpeed': data['windspeedKmph'],  # скорость ветра (км/ч)
        'windDirection': data['winddir16Point'],  # направление ветра (16 вариантов)
        'precipitation': data['precipMM'],  # количество осадков (мм)
        'pressure': round(int(data['pressure']) * 0.75006, 2)  # давление (в мм рт. ст.)
        }

    # сохраняем иконку погоды
    log.debug('Запрос изображения')
    try:
        img = urlopen(data['weatherIconUrl'][0]['value'])
    except IOError:
        log.error('Сервер вернул ошибку')
        return 0
    log.debug('Получено изображение')
    out = open(dirImg, 'wb')
    out.write(img.read())
    out.close()

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
