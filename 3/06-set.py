fruits = {'none'}
berries = {'none'}
print(type(fruits))
print(type(berries))
for i in range(3):
    fruits.add(input('Enter fruit name: '))
for i in range(3):
    berries.add(input('Enter berry name: '))
print('Fruits len:', len(fruits))
print('Berries len:', len(berries))
fruits.remove('none')
berries.remove('none')
print('Fruits len:', len(fruits))
print('Berries len:', len(berries))
if 'watermelon' in fruits:
    print('Watermelon is a fruit!')
if 'watermelon' in berries:
    print('Watermelon is a berry!')
print(len(fruits.union(berries)))
print(len(fruits.difference(berries)))
print(fruits.intersection(berries))
