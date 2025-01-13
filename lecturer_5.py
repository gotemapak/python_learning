import os
import csv
import json



# print(os.getcwd()) #откуда запускается файл
#  /Users/artempak_macbook_air/Desk
# top/Code/alex_python_edu/venv/bin/python /Users
# /artempak_macbook_air/Desktop/Code/alex_python_
# edu/lecturer_5.py
# /Users/artempak_macbook_air/Desktop/Code


# print(os.listdir()) #список все объектов в директории
# ['.DS_Store', 'alex_python_edu', 'CS50P']

# print(os.path.isfile('/Users/artempak_macbook_air/Desktop/Code/alex_python_edu/lecturer_5.py'))
#true / false если это файл

# print(os.path.isdir('/Users/artempak_macbook_air/Desktop/Code/alex_python_edu/lecturer_5.py'))
# #true / false если это папка-директория


# obj = os.listdir()
# for o in obj:
#     print(o, 
#           os.path.isdir(o), #это директория?
#           os.path.isfile(o), #это файл?
#           os.path.exists(o)) #такой файл существует?

# # target_dir ='alex_python_edu'

# открыть файл в режиме read и закрыть его после
# f = open('greeting.py', 'r') 
# f.close

# частый способ открывать файлы, чтобы не забыть закрыть
# with open('greeting.py', 'r') as f:
#     # txt = f.read() #читает весь файл, возращает текст 
#     # txt = f.readlines() #возращает список, знак \n - окончание строки
#     # txt = f.readline() #читает только одну строку текста
#     #                    #при повторе, выводит следующую
#     for line in f:
#         print(line)


# with open('greeting.py', 'a') as f: #режим аppend - добавляет строку в конец файла
#     f.write('Привет!\n')

# with open('test_write_file.txt', 'w') as f: #режим write - перезаписывает весь файл
#     f.write('Ещё раз привет\n')
#     f.writelines(['один\n', 'два\n', 'овечка\n'])


# CSV - comma-separated values. Значения разделённые запятой
# TSV - tab-separated values. \t

# new_user = ['Ivan,Ivan', 'Ivanov', 48]
# with open('users.csv', 'a') as f:
#     writer = csv.writer(f) #создаёт штуку, которая умеет писать в csv
#     writer.writerow(new_user) #запишет "Ivan,Ivan",Ivanov,48

# JSON - стандартизированная система словарей
one_more_new_user = {
    'first_name': 'Alexander',
    'last_name': 'Pushkin',
    'is_alive': False,
    'books': ['Капитанская дочка', 'Евгений Онегин']
}

#импортировали выше json
# в выводе кириллица названия книг будет в юнит-коде
with open('text', 'w') as f: #режим write - перезаписывает весь файл     
    json.dump(one_more_new_user, f)

# json.dumps() #берёт словарь и превращает в json (это строка)
# json.loads() #берёт json строку и превращает в объект питона

with open('text', 'r') as f: #режим чтения
    u = json.load(f) #перевели json значение в словарь python
    print(u) #напечатали словарь Python
