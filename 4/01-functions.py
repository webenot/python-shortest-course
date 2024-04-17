def name():
    return 'Hello'


def make_name(first_name, last_name):
    return first_name + ' ' + last_name


print(make_name(input('Enter first name: '), input('Enter last name: ')))
