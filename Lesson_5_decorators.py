def func():
    return 1
'''
def Hello(name ='jose'):
    print('The hello() func has been executed')
    def greet():
        return '\t This is the greet func inside hello()'
    
    def welcome():
        return '\t This is the welcome inside hello()'

    print(greet())
    print(welcome())
    print('This is the end of the hello function')

#-----------------------------------------------------

def Hello(name ='jose'):
    print('The hello() func has been executed')
    def greet():
        return '\t This is the greet func inside hello()'
    
    def welcome():
        return '\t This is the welcome inside hello()'
    print('i am going to return a function')

    if name == 'jose':
        return greet
    else:
        return welcome

def cool():
    def super_cool():
        return ' i am super cool'
    return super_cool

my_new_func = (Hello())

print(my_new_func)
print(my_new_func())

some_func = cool()
print(some_func)
print(some_func())


def hello():
    return 'hi jose'

def other(some_def_func):
    print('other code runs here ')
    print(some_def_func())

other(hello)
'''


def new_decorator(original_func):
    def wrap_func():
        print('SOme extra code before the original func')

        original_func()

        print('SOme extra code after the original func')

    return wrap_func


def func_needs_decorator():
    print('i want to be decorated')

decorated_func = new_decorator(func_needs_decorator)

decorated_func()
print("====================")
#@new_decorator
def func_needs_decorator_two():
    print('i want to be decorated')

func_needs_decorator_two()