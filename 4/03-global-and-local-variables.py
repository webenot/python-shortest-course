global_var = 'Zero'


def one():
    global global_var
    global_var = 'One'


def two():
    global global_var
    global_var = 'Two'


print(global_var)
one()
print(global_var)
two()
print(global_var)
