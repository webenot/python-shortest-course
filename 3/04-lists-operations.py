veggies = []
for i in range(5):
    veggies.append(input("Enter veggie name: "))
for i, veggie in enumerate(veggies):
    print(len(veggie))
if 'tomato' in veggies:
    print('I love tomatos!')
if 'onion' in veggies:
    print("I'm going to cry ,-)")
