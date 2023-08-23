
######### Lambda Function :: one line functions

# lambda input: expression

x = lambda x: x**2
print(x(9)) # 81

a = lambda x,y: x+y
print(a(5,6)) # 11

#### Difference between Lambda and def
# Lambda has no return value
# One line Function
# Not use for reusability
# No Name

# ### # Is first letter 'a' or not
b = lambda x: x[0] == 'a'
print(b('apple')) # True
print(b('banana')) # False

# ## # Check 'Even' or 'Odd"

eo = lambda a: 'Even' if a % 2 == 0 else 'Odd'
print(eo(4)) # Even

##### Why do use?
# Use along with higher order function :: Higher Order :: Need a function in input :: Or in return or output

## HOF :: 1
L = [11, 14, 21, 23, 56, 78, 45, 29,28]

x = lambda e: e % 2 ==0
y = lambda o: o% 2 != 0
z = lambda d3: d3 % 3 == 0

def return_result(func, L):
    result = 0

    for i in L:
        if func(i):
            result = result + i

    return result

print(return_result(x, L)) # 175 :: sum of even number
print(return_result(y, L)) # 129 :: sum of odd number
print(return_result(z, L)) # 144 :: sum of division by 3 


######### Map 

## 1
l = [1,2,3,4,5,6,4]

lam = lambda x: x*2
print(list(map(lam, l))) # [2, 4, 6, 8, 10, 12, 8]

print(list(map(lambda oe: oe % 2 == 0, l))) # [False, True, False, True, False, True, True]

## 2
students = [
    {
        'name':'Mujahid',
        'age':32
    },  {
        'name':'Subaha',
        'age':3
    },  {
        'name':'Anabia',
        'age':1
    },
]

print(list(map(lambda st: st['name'], students))) # ['Mujahid', 'Subaha', 'Anabia']

######### Filter :: conditioned
print(list(filter(lambda x:x>3, l))) # [4, 5, 6, 4]

fruits = ['Apple', 'Orange', 'Malta', 'Coconut', 'Grape']

print(list(filter(lambda fruit: 'e' in fruit, fruits))) # ['Apple', 'Orange', 'Grape']

######### Reduce

import functools 
L1 = [11,12,13,15,53,2,8,25]

red1 = functools.reduce(lambda x,y: x+y, L1) 
print(red1) # 139

red2 = functools.reduce(lambda x,y: x if x>y else y, L1)
print(red2) # 53

red3 = functools.reduce(lambda x,y: x if x<y else y, L1)
print(red3) # 2

###### List Comprehension ::  Used for making List programitically

L2 = [i*2 for i in L1]
print(L2) # [22, 24, 26, 30, 106, 4, 16, 50]

l3 = [i**2 for i in range(10)]
print(l3) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

l4 = [i**2 for i in range(10) if i%2 == 0]
print(l4) # [0, 4, 16, 36, 64]

l5 = [fruit for fruit in fruits if fruit[0] == 'M']
print(l5) # ['Malta']

###### Dictionary Comprehention :: Used for making Dictionary programitically
d1 = {i:i**2 for i in L1}
print(d1) # {11: 121, 12: 144, 13: 169, 15: 225, 53: 2809, 2: 4, 8: 64, 25: 625}

d2 = {i:i**2 for i in L1 if i % 2 != 0}
print(d2) # {11: 121, 13: 169, 15: 225, 53: 2809, 25: 625}