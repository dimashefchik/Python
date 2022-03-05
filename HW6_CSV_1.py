# Генерировать данные на лету, не создавая предварительных списков.

import random
import csv
import names

file_path = 'D:/Di/python/course/CSV_1/'
empty = 'empty.csv'

# Создать пустой empty.csv файл.
file_1 = file_path + empty
f = open(file_1, 'w')
# Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
digits = 'digits.csv'
file_2 = file_path + digits
with open(file_2, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns = ["Numbers"]
    writer.writerow(columns)
    for i in range(0,151):
       writer.writerow([i])

# Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
names_file = 'names.csv'
file_3 = file_path + names_file
with open(file_3, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_2 = ["Names"]
    writer.writerow(columns_2)
    for i in range(0,100):
        name = [names.get_first_name(None)]
        writer.writerow(name)

# Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
emals = 'emals.csv'
file_3 = file_path + emals
with open(file_3, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_3 = ["Emails"]
    writer.writerow(columns_3)
    for i in range(0,100):
        name = names.get_full_name(None)
        name_true = name.replace(" ", "")
        email = [name_true+'@gmail.com']
        writer.writerow(email)

# Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
nne = 'nne.csv'
file_4 = file_path + nne

with open(file_4, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_4 = ["Number", "Name", "Email"]
    writer = csv.DictWriter(csv_f, fieldnames=columns_4)
    writer.writeheader()
    for i in range(1,101):
        name_2 = names.get_full_name(None)
        name_true_2 = name_2.replace(" ", "")
        row = {"Number":i,"Name":name_2,"Email":name_true_2+'@gmail.com'}
        writer.writerow(row)


