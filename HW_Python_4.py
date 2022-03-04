# Python HW 4 Cycles
# Цилы While
# Создать переменную count со значением 0
# Создать переменную range_count со значением 10
# Создать переменную for_count со значением 0
# Создать переменную run  со значением True
import time
count = 0
range_count = 10
for_count = 0
run = True
# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	5.1 Выводить в консоль “Hello Cycle”
# Сделать цикл while который будет работать пока run
# while run:
#     time.sleep(0.500)
#     print('Hello Cycle')
# Тело цикла:
# 	6.1 Выводить в консоль (“Step =”, count)
# 	6.2 Переменной count прибавлять 1 с присвоением.
# Сделать цикл while который будет работать пока count < range_count
while count < range_count:
    time.sleep(0.300)
    print('Step =', count)
    count += 1
# Тело цикла:
# 	7.1 Выводить в консоль (“Step =”, count)
# 	7.2 Переменной count прибавлять 1 с присвоением.
# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
# 	8.1 Выводить в консоль (“Step =”, count)
# 	8.2 Переменной count прибавлять 1 с присвоением.
# 	8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)
count = 0
while count < range_count:
    time.sleep(0.300)
    print('Step =', count)
    count += 1
    if count == 3:
        print('Ster = ', count, 'If body')
        continue
# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	9.1 Выводить в консоль (“Step =”, count)
# 	9.2 Переменной count прибавлять 1 с присвоением.
# 	9.2 Сделать if с условием, если count равен range_count то цикл остановится.
# 	9.3 В теле if вывести в консоль (“STOP”, count)
count = 0
while run:
    print('Stepp = ', count)
    count += 1
    time.sleep(0.5)
    if count == range_count:
        print('STOP', count)
        break
#
# Цилы For
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# Тело цикла:
# 10.1 Вывести в консоль (‘Step =’, item)
for item in range(for_count, range_count):
    print('Step = ', item)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# Тело цикла:
# 11.1 Вывести в консоль (‘Step =’, item)
# 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
# 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
# 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
# 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).
for item_1 in range(0, 30):
    time.sleep(0.300)
    if item_1 == 5:
        print('Item =', item_1)
        continue
    if item_1 == 10:
        print('Item =', item_1)
        continue
    if item_1 == 4:
        print('Item =', item_1)
        continue
    if item_1 == 27:
        print('Item =', item_1)
        continue
    print('Step =', item_1)
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# Тело цикла:
# 12.1 Вывести в консоль (‘Step =’, item)
# 12.2 Сделать if с условием, если item равен  7.
# 	 - В теле if создать переменную inner_count равную 0
# 	 - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
# 	 - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
# 	Тело внутреннего цикла For:
# 		-- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
# 		-- Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
# 	- За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)
range_count = 10
for item_2 in range(0, range_count+1):
    time.sleep(0.300)
    if item_2 == 7:
        inner_count = 0
        print('-- inner_count =', inner_count)
        for inner_item in range(inner_count, item_2):
            print('------ Inner_Step =', inner_item)
            if inner_item ==5:
                inner_count = inner_item
            print('-- inner_count =', inner_count)
    print('Step =', item_2)
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
# Тело цикла:
# 13.1 Вывести в консоль (‘Step =’, item)
# 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
# 	- В теле if вывести (‘If_item =’, item)
# 	- В теле if поставить continue
# 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)
for item_3 in range(0, 20):
    time.sleep(0.300)
    print('Step = ', item_3)
    if item_3 > 7 and item_3 < 12:
        print('If_item = ', item_3)
        continue
print('End_iteration = ', item_3)
