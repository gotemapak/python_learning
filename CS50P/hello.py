
# Включения (list сomprehension)
# более короткий способ работы со списком
# sales = [10, 5, 6, 8, 1] #список

# total = 0
# for x in sales:
#   if x < 10:
#     total += x

# total = sum([x for x in sales if x < 10])

# total = [x for x in sales] # — это list comprehension 
# оно означает тоже самое, что в строчке ниже  
#for x in sales: 
#  x
# print(total)

client = {
  'name': 'Фёдор',
  'email': 'fedor@yandex.ru',
  'reg_date': '2021-01-01',
  'status': 'active',
  'n_orders': 12,
  'total_sales': 100500
}

#  res = []
#  for k,v in client.items():
#    if type(v) == int:
#      res.append(v)
#  print(res) # выведет [12, 100500]

# res = [v for v in client.values() if type(v) == int]
# print(res) # выведет список [12, 100500]

# res = {k: v for k, v in client.items() if type(v) == int}
# print(res) # выведет словарь {'n_orders': 12, 'total_sales': 100500}


# Перечисления (enumeration)

sales = [10, 5, 6, 8, 1]
# хотим достать каждый 2 элемент и умножить на 2

#for x in sales: #стандартный способ
#  if ...: 

for x in enumerate(sales):
  print(x)
# выведет 
# (0, 10)
# (1, 5)
# (2, 6)
# (3, 8)
# (4, 1)

# for i, x in enumerate(sales): #через enumerate
#     if i % 2 == 0:
#       sales[i] *= 2
# print(sales) #выведет [20, 5, 12, 8, 2]
