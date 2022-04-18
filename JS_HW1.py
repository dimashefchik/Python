item1 = 5
print('item1 = ', item1)
item2 = 3
print('item2 = ', item2)
item3 = item1 + item2
print('item3 = ', item3)
item4 = 'Yolochka'
print('item4 + item3 = ', item4+str(item3))
print('item4 * item3 = ', item4*item3)
item5 = item3
item6 = 15
item6_type = type(item6)
print(f'item6 == {item6}, item_6_type == {item6_type}')
item7 = str(item6)
item7_type = type(item7)
print(f'item7 == {item7}, item_7_type == {item7_type}')

age_1 = 10
age_2 = 18
age_3 = 60
if age_1 < age_2:
    print(f'You don’t have access cause your age is  {age_1}. It’s less then {age_2}')
elif age_2 <= age_1 < age_3:
    print('Welcome')
elif age_1 > age_3:
    print('Keep calm and look Culture channel')
else:
    print('Technical work')



print('==========')
def fucn_1(age):
    if age < 18:
        print(f'You don’t have access cause your age is  {age}. It’s less then 18')
    elif 18 <= age < 60:
        print(f'age = {age}','Welcome',sep='\n')
    elif age > 60:
        print(f'age = {age}' , 'Keep calm and look Culture channel', sep='\n')
    else:
        print('Technical work')

ages_1 = [17, 18,61]
for elem in ages_1:
    fucn_1(elem)

print('==========')
ages_2 = [17, 18,61]
for elem in ages_2:
    if type(elem) == int:
        fucn_1(elem)
        print('*****')
    else:
        print('Invalid type')

print('==========')
ages_3 = ['17', '18','61']
for elem in ages_3:
    if elem.isdigit():
        elem = int(elem)
        fucn_1(elem)
        print('*****')
    else:
        print('Invalid type')

print('==========')
ages_4 = list((input('Введите числа: ')).split())
for elem in ages_4:
    if elem.isdigit():
        elem = int(elem)
        fucn_1(elem)
        print('*****')