import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import numpy


url = "https://world-weather.ru/pogoda/russia/tver/"
headers_ = {"User-Agent": "Chrome/39.0.2171.95"}
months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
temperature_list = []
for month in months:
    url_ = url + month + "-2022/"
    data = requests.get(url_, headers=headers_)
    data_ = bs(data.content, "html.parser")
    month_data = data_.find("ul", class_="ww-month")
    temperature_list += [int(elem.text[:-1]) for elem in month_data.find_all("span")]
    temperature_array = numpy.array(temperature_list)
    print(f"Для месяца {month}: \n"
          f"Максимальная температура: {np.max(temperature_array)} \n"
          f"Средняя температура: {np.average(temperature_array):.2f} \n"
          f"Минимальная температура: {np.min(temperature_array)} \n"
          f"Дисперсия: {np.var(temperature_array):.2f} \n"
          f"Стандартное отклонение: {np.std(temperature_array):.2f}")