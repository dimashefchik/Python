oldlist = [10, 75, 43, 14, 25, -4, 28]
def bubble(oldlist):
    last_item = len(oldlist) - 1
    for z in range(0, last_item):      
        for x in range(0, last_item - z):
            if oldlist[x] > oldlist[x+1]:
                oldlist[x], oldlist[x+1] = oldlist[x+1], oldlist[x]     # меняем 0 и 1 элемент местами если 1>0
            print(oldlist)
    return oldlist

print(oldlist)
newlist = bubble(oldlist).copy()
print(newlist)


