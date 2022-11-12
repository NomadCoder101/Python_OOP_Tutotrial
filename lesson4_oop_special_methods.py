my_list = [1,2,3]
print(len(my_list))

class Sample():
    pass

print(Sample)
#print(len(Sample))

print('-----------------')

class Book():
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    
b =Book('Python rocks','John',200)
print(b)
print(str(b))


class Books():
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")




    
b =Books('Python rocks','John',200)
print(b)
print(str(b))
print(len(b))

del b

print(b)