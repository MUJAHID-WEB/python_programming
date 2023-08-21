########## List : data types : store multiple 

### List vs arrays:
# 1. Arrays are homogenous but List Hetrogenous
# 2. Arrays store in memory location as one by one
# 3. Arrays are much faster
# 4. Lists are more programmer friendly but slow

####################################### Create :
l = [] # Empty list
print(l)

l1 = [1,2,3,4] # Homogenous
print(l1)

l2 = ['Mujahid', 30, True, 5+6j] # Hetrogenous
print(l2)

# Multidimentional list
l3 = [1,2,3, [4,5]] # 2D
print(l3)

l4 = [ [ [1,2],[3,4] ], [ [5,6],[7,8] ] ] # 3D
print(l4)

# Type Conversion
l5 = list('Mujahid')
print(l5) # ['M', 'u', 'j', 'a', 'h', 'i', 'd']


#################################### Access : as like string

print(l1[1]) # 2
print(l1[-1]) # 4 
print(l1[1:3]) # [2.,3]
print(l1[::-1]) # [4, 3, 2, 1]

# BUT for Multi-Dimentional

print(l3[-1][0]) # 4
print(l3[3][0]) # 4
print(l3[-1][-1]) # 5

print(l4[-1][-1][0]) # 7
print(l4[1][1][0]) # 7

#################################### Edit : List are Mutable

l1[1]=200
print(l1) # [1, 200, 3, 4]

l1[2:4]=[300, 400] # slicing
print(l1) # [1, 200, 300, 400]


############################## Add :

# append :: one item add
l1.append(500) 
print(l1) # [1, 200, 300, 400, 500]

l1.append('Mujahid') 
print(l1) # [1, 200, 300, 400, 500, 'Mujahid']

l1.append([600,700,800]) # confusion
print(l1) # [1, 200, 300, 400, 500, 'Mujahid', [600, 700, 800]]

# extend :: multiple add
l1.extend([600,700,800]) 
print(l1) # [1, 200, 300, 400, 500, 'Mujahid', 600, 700, 800]

l1.extend('Dhaka') # confusion
print(l1) # [1, 200, 300, 400, 500, 'Mujahid', 600, 700, 800, 'D', 'h', 'a', 'k', 'a']

# insert
l1.insert(6, 'Islam') # index 6 adding 'Islam'
print(l1) # [1, 200, 300, 400, 500, 'Mujahid', 'Islam', [600, 700, 800], 600, 700, 800, 'D', 'h', 'a', 'k', 'a']

################################### Delete :

# del
# del l2  # delete fully
# print(l2)

del l1[0]
print(l1) # [200, 300, 400, 500, 'Mujahid', 'Islam', [600, 700, 800], 600, 700, 800, 'D', 'h', 'a', 'k', 'a']

del l1[-9]
print(l1) # [200, 300, 400, 500, 'Mujahid', 'Islam', 600, 700, 800, 'D', 'h', 'a', 'k', 'a']

del l1[-5:]
print(l1) # [200, 300, 400, 500, 'Mujahid', 'Islam', 600, 700, 800]


# remove :: when not know about index number

l1.remove('Islam')
print(l1) #[200, 300, 400, 500, 'Mujahid', 600, 700, 800]

# pop :: It deletes LAST item
l1.pop()
print(l1) # [200, 300, 400, 500, 'Mujahid', 600, 700]

# clear :: Remove all items and make empty list

l1.clear()
print(l1) # []


################################### oprations :

# Concatination :

print(l2+l3) # ['Mujahid', 30, True, (5+6j), 1, 2, 3, [4, 5]]

# Multiplication
l6 = [2,3,4,5,6]
print(l6*2) # [2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

# Loop :

for i in l6:
    print(i)

# Membership

print(4 in l6) # True

################################### Functions :

# len ::
print(len(l6)) # 5
# min :: need numaric
print(min(l6)) # 2
# max :: need numaric
print(max(l6)) # 6
# sorted :: Temporary sorted
print(sorted(l6)) # [2, 3, 4, 5, 6]
print(sorted(l6, reverse=True)) # [6, 5, 4, 3, 2]
# sort :: permanently sorted
print(l6.sort(reverse=True))
# index
print(l6.index(2)) # 4


################### Test : 1 : Without using 'title()' , Make as like its result

test = 'how are you?' # output should be 'How Are You?'

l = []

for i in test.split():
    l.append(i.capitalize())

print(' '.join(l)) # How Are You?

# print(test.split())

# l = []

# for i in test.split():
#     print(i.capitalize())
#     l.append(i.capitalize())

# print(l)
# print(' '.join(l))

################# Test : 2 : from 'abc@gmail.com' , write all letter before @

sample = 'mujahid@gmail.com'

print(sample[:sample.find('@')]) # mujahid

################ Tst : 3 : duplicate Item remove

l10 = [1,2,1,1,2,3,4,3]

L = []
for i in l10:
    if i not in L:
        L.append(i)

print(L) # [1, 2, 3, 4]



