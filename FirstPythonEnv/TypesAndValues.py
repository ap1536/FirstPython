# String Type
x = 'seven {} {}'.format(8,9)
print('x is {}'.format(x))
print()
x = 'seven {1} {0}'.format(8,9) # mention the order
print('x is {}'.format(x))
print()
x = 'seven "{1:<9}" "{0:>9}"'.format(8,9)   # append 9 spaces after first input and 9 spaces before second input
print('x is {}'.format(x))
print()
x = 'seven "{1:<09}" "{0:>09}"'.format(8,9)     # append 0's after first input and 0 before second input
print('x is {}'.format(x))
print()
a = 10
b = 11
x = f'seven {a} {b}'    # fstring model. works only after 3.6 version
print('x is {}'.format(x))
print()

print('------------------------------------------------------------------')
# Integer and Float types
x = 7 * 13      # returns Int type
print('x is {}'.format(x))
print(type(x))
print()
x = 13 / 7      # returns float type
print('x is {}'.format(x))
print(type(x))
print()
x = 13 // 7      # returns int type
print('x is {}'.format(x))
print(type(x))
print()
x = 0.1 + 0.1 + 0.1 - 0.3       # calculations are not accurate due to precision
print('x is {}'.format(x))      # below snippet is to fix it
print(type(x))
print()
from decimal import *

a = Decimal('0.10')
b = Decimal('0.30')
x = a + a + a - b      # calculations are not accurate due to precision
print('x is {}'.format(x))
print(type(x))
print()

print('------------------------------------------------------------')
# Sequences
x = [1,2,3,4,5]     # this is a list
for i in x:
    print(f'i is {i}')
print('****************')
x[2] = 42       # List Sequence is mutable
for i in x:
    print(f'i is {i}')
print('****************')

x = (1,2,3,4,5)     # this is a tuple
for i in x:
    print(f'i is {i}')
print('****************')
#x[2] = 42       # tuple Sequence is not mutable and this assignment operation will not work

# range always sets tuple
x = range(10)   # prints till 10 starting 0
for i in x:
    print(f'i is {i}')
print('****************')
x = range(5, 10)   # prints 5 to 10.
for i in x:
    print(f'i is {i}')

print('****************')
x = range(5, 50, 5)   # prints 5 to 50 step by 5
for i in x:
    print(f'i is {i}')

print('****************')
x = list(range(5, 50, 5))  # prints 5 to 50 step by 5. list constructor will give output as constructor
x[2] = 23
for i in x:
    print(f'i is {i}')

print('-----------------------------------------------------')
# Dictionaries
x = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
for i in x:         # returns only keys
    print(f'i is {i}')

x['three'] = 43
for k, v in x.items():
    print(f'Key is {k} and Value is {v}')

print('-----------------------------------------------------')
# Type() and ID()
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print(type(x))
print(type(x[1]))

# creates two objects for x and y tuples but literals inside x and y have same objects.
print(id(x))
print(id(y))
if x is y:
    print('Yep, x and y are same')
else:
    print('Nope, x and y are not same')

print(id(x[0]))
print(id(y[0]))
if x[0] is y[0]:
    print('Yep, x[0] and y[0] are both same')
else:
    print('Nope, x[0] and y[0] are not same')

# to check whether x is tuple or list
if isinstance(x, tuple):
    print('Yep. it is a tuple')
else:
    print('Nope, it is not a tuple')


print('----------------Conditional Assingment-------------------')
hungry = False
x = 'Feed the bear' if hungry else 'Do not feed the bear'
print(x)