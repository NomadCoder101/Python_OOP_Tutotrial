import math

#print(help(math))

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(4.5))
print(round(5.5))

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)

print(math.log(math.e))
print(math.log(100,10))  # 10**2
print(math.sin(10))
print(math.degrees(math.pi/2))
print(math.degrees(12.57/2))
print(math.radians(180))

print("====================")

import random

print(random.randint(0,100))

random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))


print("====================")

mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))


print("====================")

# sample with replacement

print(random.choices(population=mylist,k=10))

# sample without  replacement

print(random.sample(population=mylist,k=10))


print("====================")
print(mylist)
random.shuffle(mylist)
print(mylist)

print("====================")

print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))














