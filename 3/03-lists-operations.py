veggies = []
for i in range(5):
    veggies.append(input("Enter veggie name: "))
del veggies[3]
veggies.append('unknown')
veggies[0] = 'missing'

for i, veggie in enumerate(veggies):
    if veggie != 'unknown' and veggie != 'missing':
        print(veggie)
