'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?
'''
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random

# Генерация данных
lst = ['red_panda'] * 10
lst += ['white_panda'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание пустого DataFrame для one-hot кодирования
one_hot = pd.DataFrame()

# Получение уникальных значений
unique_values = data['whoAmI'].unique()

# Заполнение DataFrame значениями 0 и 1
for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

# Вывод первых строк
print(one_hot.head())