# Напишите валидационный скрипт используя функции
#  1. Скрипт должен на вход принимать строку.
#  2. После проверки строки выводить в консоль сообщение где будет конкретно написано, что не так в ведённой строке.
#  3. Минимум 5 символов в строке
#  4. Максимум 64 символа в строке
#  5. В строке должны быть буквы
#  6. Должна быть хотя бы одна буква в верхнем регистре
#  7. Должна быть хотя бы одна цифра
#  8. Должна быть хотя бы одна @
#  9. Строка не должна быть пустой

def check_len(text):
    if  len(text) >= 5:
        if len(text) <= 64:
            return True
        else:
            print('Строка содержит более 64 символов')
            return False
    else:
        print('Строка содержит менее 5 символов')
        return False

def check_letters(text):
    if text.isspace():
        print('Введена пустая строка')
        return False
    else:
        d = {'letter_lower': 0,
             'letter_upper': 0,
             'number': 0,
             'at': 0}
        for i in text:
            if i.isalpha():
                if i.islower():
                    d['letter_lower'] += 1
                else:
                    d['letter_upper'] += 1
            elif i.isdigit():
                d['number'] += 1
            elif i == '@':
                d['at'] += 1
            elif i == ' ':
                print('Строка не должна содеражать пробелов')
                return False
            else:
                print(f'Строка содержит запрещенный символ {i}')
                return False
    if d['number'] < 1:
        print('Строка не содержит цифр')
        return False
    elif d['at'] == 0:
        print('Строка не содержит @')
        return False
    elif d['at'] > 1:
        print('Строка содержит более одной @')
        return False
    elif d['letter_lower'] == 0 and d['letter_upper'] == 0:
        print('Строка не содержит букв')
        return False
    elif d['letter_lower'] == 0:
        print('Строка не содержит строчных букв')
        return False
    elif d['letter_upper'] == 0:
        print('Строка не содержит хотя бы 1 большую букву')
        return False
    return True


text = input('Введите текст: ')
re = True
while True:
    if check_len(text):
        if check_letters(text):
            print('Введена валидная строка')
            break
        else:
            break
    else:
        break




