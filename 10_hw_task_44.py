# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd                 # Импортируем библиотеку pandas под сокращением pd
import random                       # Импортируем библиотеку prandom для 
lst = ['robot'] * 10                # Созаём список
lst += ['human'] * 10               # Дополняем этот список
random.shuffle(lst)                 # Перемешиваем список
data = pd.DataFrame({'whoAmI':lst}) # Создадим датафрейм пандас с заголовком whoAmI из списка lst
pd.get_dummies(data['whoAmI'])      # Выведем таблицу для ознакомления к чему нужно придти
data.head(n = 20)

# Решение 1
print()
print("Решение 1:")
print("\trobot\thuman")             # печатаем заголовок
for i in range(len(lst)):           # Выводим таблицу аналогичную get_dummies
  if lst[i] == 'robot':
    print(f'{i}\t  1\t  0')         # Печатаем: индекс таб  1 таб 0 
  else:
    print(f'{i}\t  0\t  1')         # Печатаем: индекс таб  0 таб  1 

# Решение 2
print()
print("Решение 2:")
lst_out = [['index','robot','human']] # Создадим список для вывода
for i in range(len(lst)):           # Выводим таблицу аналогичную get_dummies
  if lst[i] == 'robot':
    lst_out.append([i,'1','0'])     # добавим с список список
  else:
    lst_out.append([i,'0','1'])
for i in range(len(lst)):           # Выводим таблицу аналогичную get_dummies
  print(*lst_out[i], sep='\t')      # добавим с список список