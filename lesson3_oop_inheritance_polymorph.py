
# will use as a base class
class Animal():
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an Animal')
    def eat(self):
        print('I am eating')


# inheritance Example
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    

    def eat(self):
        print('I am dog and i am eating')

    def who_am_i(self):
        print('I am a Dog')

    def bark(self):
        print('Woof Woof ..')



my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
print("---------------")
myanimal = Animal()
#myanimal
myanimal.eat()
myanimal.who_am_i()
print()
print('-----------------')
#  Example Polymorphism 


class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof Woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow Meow !"

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())


 #one way   
#for pet in [niko,felix]:
   # print(type(pet))
    #print(pet.speak())

#another way

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)


#------------------------------
print()

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method ')

#myanm = Animal('fred')
#myanm
#myanm.speak()

class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'

        
class Cat(Animal):
    def speak(self):
        return self.name + ' says Meow!'


fido = Dog('fido')
iris = Cat('Iris')


print(fido.speak())
print(iris.speak())

