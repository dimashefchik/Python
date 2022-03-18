import random
def binarysearch(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid -1)
        else:
            return binarysearch(mylist, iskat, mid + 1 , stop)
"""Список уже существует"""
mylist = [1, 3, 5, 8, 12, 16, 17, 22, 33, 35, 39, 40, 41, 47]
iskat = 12
x = binarysearch(mylist, iskat, 0, len(mylist))
if x == False:
    print('Item', iskat, 'Not Found!')
else:
    print('Item', iskat, 'Found at idex', x)

"""Список создаем сами"""
mylist_2 = random.sample(range(1,101), 30)
mylist_2.sort()
print(mylist_2)
iskat_2 = 14
y = binarysearch(mylist_2, iskat_2, 0, len(mylist_2))
if y == False:
    print('Item', iskat_2, 'Not Found!')
else:
    print('Item', iskat_2, 'Found at idex', y)

