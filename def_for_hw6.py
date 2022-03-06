import datetime
import names
import random

def get_email (name):
    email = str(name.replace(" ", "") + '@gmail.com')
    return email

def get_date (start, end):
    start_date = datetime.date(start, 1, 1)
    end_date = datetime.date(end, 1, 1)
    time_between = end_date - start_date
    days_betwen_date = time_between.days
    random_days = random.randrange(days_betwen_date)
    random_date = start_date + datetime.timedelta(days=random_days)
    return str(random_date)

def get_phone (a):
    if a == 0:
            code = 37529
    elif a == 1:
            code = 37533
    elif a == 2:
            code = 37544
    elif a == 3:
            code = 37525
    number = random.randint(1000000, 999999999)
    phone = str('+' + str(code) + str(number))
    return phone