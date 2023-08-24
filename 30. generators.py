## ######## ## Generators :: Its a simple way of creating Iterator

## 'yield' statement :: return generator object

## 'return' vs 'yield' :: yield execute and close and remember the last execution. So it wont print again. 

L = [x for x in range(100000)]
# for i in L:
#     print(i**2)
import sys

print(sys.getsizeof(L)) # 800984 bytes

##### using iterator

x = range(1000000)
#for i in x:
#    print(x)

print(sys.getsizeof(x)) # 48 bytes

##### Simple Example of Python Generator

def gen():
    yield 'Mujahidul'
    yield 'Islam'
    yield 'Mujahid'

Gen = gen()

for i in Gen:  #
    print(i)
## output ::
# Mujahidul
# Islam
# Mujahid


##### Example 2:
def sqr(num):
    for i in range(1, num+1):
        yield i**2

gen = sqr(5)

print(next(gen)) # 1 
print(next(gen)) # 4
print(next(gen)) # 9

for i in gen:
    print(i) 
## output :: from where it stops
# 16
# 25


###### My Range ::

def my_range(start, end):
    for i in range(start, end):
        yield i

for i in my_range(15,25):
    print(i)

##### Genrator Expression ::

gen = (i**2 for i in range(1,5)) # as like list comprehension

for i in gen:
    print(i)


######## Practical Example ::

## Big Data :: like image file

######## Benefits

# memory efficient
# work with Infinite Streams 
# Chainning Generators

def fib_num(nums):
    x,y = 0,1
    for _ in range(nums):
        x,y = y, x+y
        yield x

def square(nums):
    for i in nums:
        yield i**2


print(sum(square(fib_num(10)))) # 4895

