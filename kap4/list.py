# coding=utf-8
"""
# *************** Variable names *************** #

    Allowed.        Not allowed
    -------         -----------
    varname         näme
    vArNaMe1        1_varname
    var_name_1      varname-1
    _varname        var&name

"""



# **************** Some math ******************** #
print '# ************** Math **************** #'
x = 5
y = 2
print '%d + %d = %d' % (x, y, x + y)
print '%d - %d = %d' % (x, y, x - y)
print '%d * %d = %d' % (x, y, x * y)
print '%d / %d = %d' % (x, y, x / y) # Wrong
print '%d / %d = %f' % (x, y, float(x) / y) # Correct

print '# ************ Math lib ************** #'

from math import *
print ceil(8.9), ceil(8.1) # Return the ceiling
print floor(8.9), floor(8.1) #Return the floor
print pow(x,y)
print fmod(x,y)

# ******************* Bool ********************** #
"""
False = False, None, 0, "", (), [], {}
True = rest
"""
print '# ************** Bool **************** #'
x = True
y = 1
if x == y:
    print 'true'
else:
    print 'false'
print 5<2 # False
print 2<5 # True

print (x==y)

# ******************* List ********************** #
print '# ************** List **************** #'
list = ['Audi', 'Bmw', 'Volvo']
# *************** Print w Index ***************** #
print list[0:2] # Print index 0 and 1
print list[:3]
print list[-1] # print from end of list
# ************** Append to list ***************** # // Append to end of list
list.append('Volkswagen')
# ************** insert to list ***************** # // Insert after index 2
list.insert(2, 'Saab')
# ************** Change in list ***************** #
list[1] = 'BMW'
# *************** Print w loop ****************** #
for item in list:
    print item


# ************** Multidim List ****************** #
m = []
m.append([]) # List index 0
m[0].append([])
m[0].append(1)
print m

# **************** Tupleter ********************* #
tup1 = (12,) # Need comma
tup2 = (34, 66, 9, 74)
print tup2[1]
#tup2[1] = 0 # Cant change
print tup2

# ******************** Sets ********************** #
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket) # create a set without duplicates
set(['orange', 'pear', 'apple', 'banana'])
print 'orange' in fruit                 # fast membership testing
print 'crabgrass' in fruit


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
                                 # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
print a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
print a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
print a & b                              # letters in both a and b
set(['a', 'c'])
print a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])
















dict = {'Namn':'Kalle', 'Efternamn' : 'Karlsson'}
print dict

dict['Personnummer'] = '196505062759'
