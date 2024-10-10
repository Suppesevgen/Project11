import requests
import matplotlib.pyplot as plt
import datetime
from datetime import date

# Пример действия библиотеки requests (работа с веб-сайтами)
r = requests.get('https://ria.ru/?ysclid=m239prx5j2767041445')
print(r.headers) #доступ к заголовкам сайта
print(r.status_code) # cтатус код
print(r.text) #вывод содержимого сайта

# Пример действия библиотеки matplotlib (создание графиков)
x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x,y) #стандартная функция, которая строит график
plt.title('График') # название графика
plt.xlabel('x') # обозначение по оси x
plt.ylabel('y') # обозначение по оси y
plt.show() # вывод графика на экран

# Пример действия библиотеки datetime (создание и вывод объектов времени и даты)
timeobj= datetime.time(22,34,12) # создание объекта времени
dt_now = datetime.datetime.now() # получение текущей даты и времени
current_date = date.today() # получение текущей даты
print(timeobj) # вывод объекта времени
print(dt_now) # вывод текущей даты и времени
print(current_date)# вывод текущей даты




