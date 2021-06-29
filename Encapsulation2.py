 #Python program to
# demonstrate private members
 
# Creating a Base class that has a private and protected variable
class Base:
    def __init__(self,name,age):
        self._name = name
        self.__age = age

test1 = Base('John', 18) # this has the name as protected and age as private
print(test1._name)
print(test1._Base__age)
 
