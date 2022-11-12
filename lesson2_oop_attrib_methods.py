my_list = [1,2,3]
print(type(my_list))
myset = set()
print(type(myset))
print()
#----------------------
# simple class 
class Sample():
    pass

my_sample = Sample()
print(type(my_sample))

print()
#----------------------

class Dog():


    # Class object Attribut 
    #Same for any instance of a class
    species = 'mamal'



    # a function inside a class is a method 
    # init can be consedered as a contructor for the class
    def __init__(self,breed,name,spots):
        #Attributes
        # We take in the argument
        #Assign it using self.attribute_name 
        #self.my_attribute =breed
        self.breed =breed
        self.name = name
        #expect boolean True/False
        self.spots =spots

    # Operations/Actions --> Methods

    def bark(self,age):
        print('Woof! My name is {} and my age is {} '.format(self.name,age))


my_dog = Dog(breed='Huskie',name='Tiger',spots= False)
print(type(my_dog))
print(my_dog.breed)
#print(my_dog.my_attribute)
#print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark(5)

print('----------------')
#another Example 

class Circle():
    # Class Object Attribute must be true for any instance of the class 
    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius*radius*self.pi

    # Method 
    def get_circumfrence(self):
       # return self.radius * self.pi *2
        return self.radius * Circle.pi *2

my_circle = Circle(30)
print('pi = ',my_circle.pi)
print('radius =',my_circle.radius)
print('Circumfrence = ',my_circle.get_circumfrence())
print('Area =' , my_circle.area)

