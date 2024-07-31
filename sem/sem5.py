import pandas as pd
from pandas import read_csv


file_patch = 'california_housing_test.csv'
data = read_csv(file_patch)
# print(type(data))
# print(data.shape)
# print(data.dtypes)
# print(data.info())
# print(data.describe())


"""
 1. Проверить есть ли в файле пустые значения
"""
df = pd.read_csv('./california_housing_test.csv')
# print(df.isnull())
# print(df.isnull().sum())
"""

2. Показать median_house_value где median_income < 2
"""

# print(df[df['median_income'] < 2]['median_house_value'])


"""
3. Показать данные в первых 2 столбцах
"""
# print(df[['longitude', 'latitude']])
# print(df.iloc[:, :2]) # если не знаем название столбцов


"""
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""
# print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])


"""
Задача №3. Решение в группах
1. Определить какое максимальное и минимальное значение median_house_value
"""
# print(f'Минимальное - {df["median_house_value"].min()}, Максимальное - {df["median_house_value"].max()}')



"""
2. Показать максимальное median_house_value, где
median_income = 3.1250
"""

# print(df[df['median_income'] == 3.1250]["median_house_value"].max())



"""
3. Узнать какая максимальная population в зоне
минимального значения median_house_value
"""
# print(df[df['median_house_value'] == df['median_house_value'].min()]['population'].max())

"""
ДЗ
Урок 9. Работа с табличными данными
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , 
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""


# print(df['households'])
