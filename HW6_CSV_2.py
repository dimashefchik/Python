# Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
import csv
import names
file_path = 'D:/Di/python/course/CSV_2/'

# Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
digits_2 = 'digits_2.csv'
file_1 = file_path + digits_2
with open(file_1, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns = ["Number"]
    writer.writerow(columns)
    data_1 = []
    data_all = []
    for i in range(10,311):
        data_1.append([i])
    writer.writerows(data_1)

# Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
emals_2 = 'emals_2.csv'
file_2 = file_path + emals_2
with open(file_2, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_2 = ["Email"]
    writer.writerow(columns_2)
    for i in range(0,400):
        name = names.get_full_name(None)
        name_true = name.replace(" ", "")
        email = [name_true+'@gmail.com']
        writer.writerow(email)

# Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
nne_2 = 'nne_2.csv'
file_3 = file_path + nne_2
with open(file_3, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_4 = ["Number", "Name", "Email"]
    writer = csv.DictWriter(csv_f, fieldnames=columns_4)
    writer.writeheader()
    rows = []
    for i in range(1,450):
        name_2 = names.get_full_name(None)
        name_true_2 = name_2.replace(" ", "")
        row = {"Number":i,"Name":name_2,"Email":name_true_2+'@gmail.com'}
        rows.append(row)
    writer.writerows(rows)

# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)
import datetime
import random

nne_3 = 'nne_3.csv'
file_4 = file_path + nne_3
with open(file_4, 'w', newline="") as csv_f:
    writer = csv.writer(csv_f)
    columns_4.append("Date")
    writer = csv.DictWriter(csv_f, fieldnames=columns_4)
    writer.writeheader()
    rows = []
    count = 1
    for i in range(1, 51):
        name_2 = names.get_full_name(None)
        name_true_2 = name_2.replace(" ", "")
        start_date = datetime.date(1980, 1, 1)
        end_date = datetime.date(1990, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        row = {"Number": count, "Name": name_2, "Email": name_true_2 + '@gmail.com',"Date":str(random_date)}
        rows.append(row)
        count += 1
    writer.writerows(rows)

    print(count)

    for i in range(1, 101):
        name_3 = names.get_full_name(None)
        name_true_3 = name_3.replace(" ", "")
        start_date = datetime.date(1991, 1, 1)
        end_date = datetime.date(2000, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        row = {"Number": count, "Name": name_2, "Email": name_true_2 + '@gmail.com',"Date":str(random_date)}
        writer.writerow(row)
        count += 1

    for i in range(1, 151):
        name_3 = names.get_full_name(None)
        name_true_3 = name_3.replace(" ", "")
        start_date = datetime.date(2001, 1, 1)
        end_date = datetime.date(2010, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        row = {"Number": count, "Name": name_2, "Email": name_true_2 + '@gmail.com',"Date":str(random_date)}
        writer.writerow(row)
        count += 1

    for i in range(1, 151):
        name_3 = names.get_full_name(None)
        name_true_3 = name_3.replace(" ", "")
        start_date = datetime.date(2011, 1, 1)
        end_date = datetime.date(2021, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        row = {"Number": count, "Name": name_2, "Email": name_true_2 + '@gmail.com',"Date":str(random_date)}
        writer.writerow(row)
        count += 1


