# Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

import csv
import names
import datetime
import random

file_path = 'D:/Di/python/course/CSV_2/'
nne = 'nne_3.csv'
combo = 'combo.csv'
file = file_path + nne
file_1 = file_path + combo

with open(file, 'r') as f1:
    original = csv.reader(f1)
    file_name = []
    for i in original:
        i.pop(0)
        i.pop(1)
        file_name.append(i)
    file_name.pop(0)
    file_name.sort(reverse=False)
    print(file_name[0][0])
    print(file_name[0][1])

with open(file_1, 'w', newline="") as f2:
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
        email_1 = ii[0].replace(" ", "")
        salary = random.randrange(1000, 2000, 100)
        row = {"Number": count, "Name": ii[0], "Email": email_1 + '@gmail.com',"Phone":'+375'+str(code)+str(random.randint(1000000, 9999999)), "Gender":gender, "Salary":salary, "Date": str(ii[1])}
        count += 1
        writer.writerow(row)

    for aa in range(1, 551):
        row_2 = []
        a_2 = random.randint(0, 1)
        salary_2 = random.randrange(1000, 2000, 100)
        if a_2 == 0:
            name_2 = names.get_full_name(gender='female')
            gender_2 = 'Female'
            code = 29
        else:
            name_2 = names.get_full_name(gender='male')
            gender_2 = 'Male'
            code = 33
        email_2 = name_2.replace(" ", "")
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2020, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        row = {"Number": count, "Name": name_2, "Email": email_2 + '@gmail.com',"Phone": '+375' + str(code) + str(random.randint(1000000, 9999999)), "Gender": gender_2, "Salary": salary_2,
               "Date":str(random_date)}
        count += 1
        writer.writerow(row)


