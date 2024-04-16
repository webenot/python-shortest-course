someList = []
for i in range(3):
    someList.append(input("Enter list item: "))
someTuple = (someList[2], someList[1], someList[0])
print(someTuple[0] + ' ' + someTuple[1] + ' ' + someTuple[2])
print(someTuple[0:2])
if 'stone' in someTuple:
    print('Stone found!')
