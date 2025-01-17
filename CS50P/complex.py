

# Списки списков

#student = [5, 2, 3, 3, 5]

# students = (
#    [5, 2, 3, 3, 5],
#    [3, 3, 4, 5, 4],
#    [5, 5, 5, 5, 4]
#) # кортеж () со списками

# Извлечение данных
# print(students[0][0]) #мы обращаемся к переменной с кортежом,
# внутри которого список и мы хотим получить первый элемент кортежа
# и дальше получить первый элемент списка → 5
# print()

# Редактирование данных
# students[0][0] = 1 #меняем первый элемент выбранного элемента
# print(students) #([1, 2, 3, 3, 5], [3, 3, 4, 5, 4], [5, 5, 5, 5, 4])
# поменялось [5, 2, 3, 3, 5] → [1, 2, 3, 3, 5]

# students = [
#     (5, 2, 3, 3, 5),
#     (3, 3, 4, 5, 4),
#     [5, 5, 5, 5, 4]
# ]  # два кортежа внутри одного списка

# # students[0] = 0
# # print(students) # [0, (3, 3, 4, 5, 4), [5, 5, 5, 5, 4]]
# # перезаписался первый элемент СПИСКА

# students[0][0] = 0 
# print(students) #ошибка, т.к. первый элемент - это кортеж

# # Списки словарей

# users = [
#     {'name': 'Alex', 'reg_date:': '2021-01-01'},
#     {'name': 'Maria', 'reg_date:': '2021-01-01'},
#     {'name': 'Fedor', 'reg_date:': '2021-02-03'},
# ] #список со словарями
# print(users)
# print()

# # Извлечение данных
# u = users[0]
# #print(u) #{'name': 'Alex', 'reg_date:': '2021-01-01'}
# print(u['name']) #Alex / обращаемся через переменную и ключ
# print(users[0]['name']) #Alex / обращаемся через индекс списка и
# # ключ словаря, чтобы извлечь значение

# Словари списков
# students = {
#     'Alex': [5, 2, 3, 3, 5],
#     'Maria': [3, 3, 4, 5, 4],
#     'Fedor': [5, 5, 5, 5, 4],
# }

# # Извлекаем данные
# print(students['Fedor']) #[5, 5, 5, 5, 4]
# print(students['Fedor'][0]) #5
# print()

# Словари словарей

# stats = {
#      '2023-01-01': {'n_visitors': 100, 'revenue': 0},
#      '2023-01-02': {'n_visitors': 33, 'revenue': 25},
#      '2023-01-03': {'n_visitors': 435, 'revenue': 154}
# }
# print(stats) #{'2023-01-01': {'n_visitors': 100, 'revenue': 0} ...}
# print(stats['2023-01-03']) #{'n_visitors': 435, 'revenue': 154}
# print(stats['2023-01-03']['revenue']) #154


# Перебор и агрегирование
# stats = {
#       '2023-01-01': {'n_visitors': 100, 'revenue': 0},
#       '2023-01-02': {'n_visitors': 33, 'revenue': 25},
#       '2023-01-03': {'n_visitors': 435, 'revenue': 154}
# }

# # хотим посчитать общую выручку
# total_revenue = 0
#  for date in stats:
#      total_revenue += stats[date]['revenue']
#  print(total_revenue) #179

# # второй способ через comprehension
# total_revenue = (sum([date['revenue'] for date in stats.values()]))
# print(total_revenue)

# Добавление и редактирование значений
stats = {
       '2023-01-01': {'n_visitors': 100, 'revenue': 0},
       '2023-01-02': {'n_visitors': 33, 'revenue': 25},
       '2023-01-03': {'n_visitors': 435, 'revenue': 154}
}

# stats['2023-01-04'] = {'n_visitors': 1435, 'revenue': 554}
# print(stats) #добавилось '2023-01-04': {'n_visitors': 1435, 'revenue': 554}


# stats['2023-01-05'] = 'Хаха. вас взломали!'
# print(stats) #{'n_visitors': 1435, ... 'Хаха. вас взломали!'}

# Удаление значений
# students = {
#     'Alex': [5, 2, 3, 3, 5],
#     'Maria': [3, 3, 4, 5, 4],
#     'Fedor': [5, 5, 5, 5, 4],
# }
# print(students['Alex'].pop(0)) #удалиться оценка 5 из списка

# stats = {
#     '2023-01-01': {'n_visitors': 100, 'revenue': 0},
#     '2023-01-02': {'n_visitors': 33, 'revenue': 25},
#     '2023-01-03': {'n_visitors': 435, 'revenue': 154}
# }

# del stats['2023-01-03']['n_visitors'] #'2023-01-03': {'revenue': 154}}
# print(stats)


clients_data = [
    ('Joe Smith', 20),
    ('George Hanna', 8),
    ('Tami Foster', 19)
]

for pair in clients_data:
    print(pair)
    print(pair[0], pair[1])  # Доступ к элементам через индексы