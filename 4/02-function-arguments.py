def full_name(surname, name='John'):
    return name + ' ' + surname


print(full_name(input('Enter surname: ')))
print(full_name(input('Enter surname: '), input('Enter name: ')))
