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


my_dog = Dog(breed='Huskie',name='Tiger',spots= False)
print(type(my_dog))
print(my_dog.breed)
#print(my_dog.my_attribute)
print(my_dog.name)
print(my_dog.spots)