from collections import Counter

mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3]

print(Counter(mylist))

mylist = ['a','a','10','10']

print(Counter(mylist))

print(Counter('aaaabbbbcccc'))

sentence = 'How many time does each word show up in this sentence with a word'

print(Counter(sentence.split()))
print(Counter(sentence.lower().split()))
print(Counter(sentence.capitalize().split()))

letter = 'aaabbbbbbbbbbbcccccccdddddddddddd'
c= Counter(letter)
print(c)
print(c.most_common)
print(c.most_common(3))
print(list(c))

print('=============================')

from collections import defaultdict

d  =  {'a':10}
print(d)
print(d['a'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['Wrong'])
print(d)

print("===================")

mytuple = (10,20,30)
print(mytuple[0])

from collections  import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
print(Dog)
sammy = Dog(age= 5, breed='lab', name='sam')

print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(type(sammy))
print(sammy[0])















