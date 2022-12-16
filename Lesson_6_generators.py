def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))


def create_cubes_two(n):
    
    for x in range(n):
        yield x**3
            
   
for x in create_cubes_two(10):
    print(x)
print(create_cubes_two(10))
print(list(create_cubes_two(10)))



def gen_fibb(n):
    a =1
    b =1
    for i in range(n):
        yield a
        a,b =b,a+b

for num in gen_fibb(10):
    print(num)



def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen():
    print(x)

g = simple_gen()
print(g)
print(next(g))
print(g)
print(next(g))
print(g)
print(next(g))
#print(g)
#print(next(g))

s = 'hello'
for letter in s:
    print(letter)
print('-------------')
s_iter = iter(s)
print(next(s_iter))
print('-------------')

def gensquares(n):
    for i in range(n):
        yield i **2
for x in gensquares(10):
    print(x)

print('-------------')

import random

print(random.randint(1,10))

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for num in rand_num(1,10,12):
    print(num)

print('-------------')

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)



