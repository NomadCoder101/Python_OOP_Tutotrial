# list comprihension
def func_one(n):
    return[str(num) for num in range(n)]

#print(func_one(10))

#map
def func_two(n):
    return list(map(str,range(n)))

#print(func_two(10))

import time
# current time before 
start_time = time.time()
# run code 
result = func_one(1)
# current time after running the code 
end_time = time.time()
# elapsed time 
elapsed_time =end_time-start_time
print(elapsed_time)


start_time = time.time()
# run code 
result = func_two(1)
# current time after running the code 
end_time = time.time()
# elapsed time 
elapsed_time =end_time-start_time
print(elapsed_time)


print("=====================")


import timeit

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return[str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number=100000))



stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt,setup,number=100000))