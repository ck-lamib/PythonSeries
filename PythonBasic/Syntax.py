# print a _Statement
from tkinter.tix import Tree
from unicodedata import name


print("bimal")  #bimal

#python follows strong identation(space at the start of code).
#And space can be 1 or many according to programmer. 4 is mostly preferred
if(100%20 == 0 ):
    print("100 is a even number")

#python variable
# In python variable type is not decleared. But is determined by python itself.
#NOTE: variable are case sensitive as a and A are different variable in python
a = 2
b = "bimal"
c = True
print(type(a)) #int
print(type(b)) #str and str can be double or single quote.
print(type(c)) #bool


#python comment
# This is python comment and python doesnot have any sepereate multi line comments like java

"""
This is a comment
written in
more than just one line
"""#this is also a comment which is used as multi line comment in python


# Different type of case for defining variable name
# Camel case:
myAge = 20

#Pascal case
IsAge = True

#Snake case
my_age_is_20 = 20

#assigning varable
#many value to many varable
x,y,z = "banana", "mangoes", 'apple'
print(x)
print(y)
print(z)

#one value to multiple varable
x = y = z = "banana"
print(x)
print(y)
print(z)

#unpacking a collection
list_ = [1,3,4,"bimal"]
x,y,z,w = list_
# x,y,z = list_ #this is a complete error
print(x)
print(y)
print(z)
print(w)


# printing variable
x = "hello"
y = " world"
z = 3
a = 3
print(x,y) #hello  world
print(x+y) #hello world
print(x+str(z)) #hello3
# print(x+z) #error
print(z+a) #6


# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = set(vowels)
# fSet[0] = 1
print('The frozen set is:', fSet)
print('The empty frozen set is:', type(fSet))


# set of letters
s = {'g', 'e', 'k', 's'}
# adding 's'
s.add(0)
print('Set after updating:', s)
 
# Discarding element from the set
s.discard('g')
print('\n\tSet after updating:', s)
 
# Removing element from the set
s.remove('e')
print('\nSet after updating:', s)
 
# Popping elements from the set
print('\nPopped element', s.pop())
print('Set after updating:', s)
 
s.clear()
print('\nSet after updating:', s)