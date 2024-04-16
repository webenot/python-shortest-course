car = {
    'model': 'Toyota',
    'engine': 2.0,
    'type': 'diesel',
}
print(car)
print(len(car))
car['color'] = input('Enter a color: ')
car['price'] = input('Enter a price: ')
print(car)
print(len(car))
car['engine'] = float(input('Enter engine number: '))
print(car)
print(len(car))
if 'color' in car:
    print('Color present')
del car['color']
print(car)
print(len(car))
if 'color' not in car:
    print('Color missing')
