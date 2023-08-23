##### Iteration :: process of going over a group of items  one after another using loop


##### Iterators :: is an object that allows to traverse through a sequence of data without having to store the entire data in the memory

x = range(1,100) # iterable

for i in x: # Iterators
    print(i*2)

import sys
print(sys.getsizeof(x)/1024) # 0.046875


##### Iterable :: an object which on can iterate over

L = [1,2,3]
print(type(L)) 
## L is an iterable

print(type(iter(L))) # <class 'list_iterator'>
# iter(L) --> iterator

###### Point :: All Iterables are not Iterator

L1 = [x for x in range(1,100)] # Iterable

for i in L1: # Not Iterators
    print(i*2)

print(sys.getsizeof(x)/1024) # 0.046875


######### Trick ::  dir()
## Iterable : has an iter() function :: dir
L2 = [2,4,9,4]
print(dir(L2)) # '__iter__' :: L is Iterable :: 

## Iterator : has both iter and next function 

iter_l = iter(L2) # by using iter, can make iterator
print(dir(iter_l)) # '__iter__' and '__next__' :: iter_l is an iterator 


########### Understanding how 'for loop' works ::

num = [2,4,6,8]

# for i in num:
#     print(i)

# step1 --> fetch the iterator by iter function
iter_num = iter(num)
# step2 --> next
next(iter_num) 
next(iter_num) 
next(iter_num) 
#next(iter_num) :: untill showint error

####### My LOOP ::

def my_loop(iterable):

    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

a =[1,2,3,4]
print(my_loop(a))

b = range(1,10)
print(my_loop(b))

####################### Confusion ::



################ Application ::

# Big Data handle :: one by one in memory

