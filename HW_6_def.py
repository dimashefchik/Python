import csv
import datetime
import names
import random
from def_for_hw6 import get_email, get_phone, get_date

file_path = 'D:/Di/python/course/CSV/'
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
file_4 = file_path + emals
with open(file_4, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_3 = ["Emails"]
    writer.writerow(columns_3)
    for i in range(0,100):
        name = names.get_full_name(None)
        email = get_email(name)
        writer.writerow(email)

# Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
nne = 'nne.csv'
file_5 = file_path + nne

with open(file_5, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_4 = ["Number", "Name", "Email"]
    writer = csv.DictWriter(csv_f, fieldnames=columns_4)
    writer.writeheader()
    for i in range(1,101):
        name = names.get_full_name(None)
        row = {"Number":i,"Name":name,"Email":get_email(name)}
        writer.writerow(row)

# Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.

# Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
digits_2 = 'digits_2.csv'
file_6 = file_path + digits_2
with open(file_6, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns = ["Number"]
    writer.writerow(columns)
    data_1 = []
    for i in range(10,311):
        data_1.append([i])
    writer.writerows(data_1)

# Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
emals_2 = 'emals_2.csv'
file_7 = file_path + emals_2
with open(file_7, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_2 = ["Email"]
    emails = []
    writer.writerow(columns_2)
    for i in range(0,400):
        name = names.get_full_name(None)
        emails.append(get_email(name))
    writer.writerows(emails)

# Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
nne_2 = 'nne_2.csv'
file_8 = file_path + nne_2
with open(file_8, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_4 = ["Number", "Name", "Email"]
    writer = csv.DictWriter(csv_f, fieldnames=columns_4)
    writer.writeheader()
    rows = []
    for i in range(1,451):
        name = names.get_full_name(None)
        row = {"Number":i,"Name":name,"Email":get_email(name)}
        rows.append(row)
    writer.writerows(rows)

# Добавить в файл task_1.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)

task_1 = 'task_1.csv'
file_9 = file_path + task_1
with open(file_9, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_4.append("Date")
    writer = csv.DictWriter(csv_f, fieldnames=columns_4)
    writer.writeheader()
    rows = []
    count = 1
    for i in range(1, 51):
        name = names.get_full_name(None)
        row = {"Number": count, "Name": name, "Email":get_email(name),"Date":get_date(start=1980,end=1990)}
        rows.append(row)
        count += 1
        writer.writerow(row)


    for i in range(1, 101):
        name = names.get_full_name(None)
        row = {"Number": count, "Name": name, "Email":get_email(name),"Date":get_date(start=1991,end=2000)}
        writer.writerow(row)
        count += 1

    for i in range(1, 151):
        name = names.get_full_name(None)
        row = {"Number": count, "Name": name, "Email":get_email(name),"Date":get_date(start=2001,end=2010)}
        writer.writerow(row)
        count += 1

    for i in range(1, 151):
        name = names.get_full_name(None)
        row = {"Number": count, "Name": name, "Email": get_email(name), "Date": get_date(start=2011,end=2020)}
        writer.writerow(row)
        count += 1


# Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) Соберите имена из файла task_1.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла task_1.csv забрать даты из task_1.csv которые были с этими именами в task_1.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.
combo = 'combo.csv'
file_10 = file_path + combo

# достаем данные из файла task_1.csv

with open(file_9, 'r') as f1:
    original = csv.reader(f1)
    file_name = []
    for i in original:
        i.pop(0)
        i.pop(1)
        file_name.append(i)
    file_name.pop(0)
    file_name.sort(reverse=False)

with open(file_10, 'w', newline="") as f2:
    writer = csv.writer(f2)
    columns = ["Number", "Name", "Email", "Phone", "Gender", "Salary", "Date"]
    writer = csv.DictWriter(f2, fieldnames=columns)
    writer.writeheader()
    count = 1
    for ii in file_name:
        a = random.randint(0, 1)
        if a == 0:
            gender = 'Female'
            code = 29
        else:
            gender = 'Male'
            code = 33
        email_1 = str(ii[0].replace(" ", "") + '@gmail.com')
        salary = random.randrange(1000, 2000, 100)
        row = {"Number": count, "Name": ii[0], "Email": email_1,"Phone":get_phone(a=random.randint(0,3)), "Gender":gender, "Salary":salary, "Date": get_date(start=1990, end=2000)}
        count += 1
        writer.writerow(row)

    for aa in range(1, 551):
        row_2 = []
        a_2 = random.randint(0, 1)
        salary_2 = random.randrange(1000, 2000, 100)
        if a_2 == 0:
            name = names.get_full_name(gender='female')
            gender_2 = 'Female'
        else:
            name = names.get_full_name(gender='male')
            gender_2 = 'Male'
        row = {"Number": count, "Name": name, "Email": get_email(name),"Phone":get_phone(a=random.randint(0,3)), "Gender": gender_2, "Salary": salary_2,  "Date": get_date(start=2001, end=2010)}
        count += 1
        writer.writerow(row)













