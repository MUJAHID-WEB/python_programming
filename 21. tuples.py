############## Tuples :: written in () : Immutable : No changes : read only data type : No write functions


## ################### #### create

t = () # Empty list
print(t)

t1 = (1,2,3,4) # Homogenous
print(t1)

t2 = ('Mujahid', 30, True, 5+6j) # Hetrogenous
print(t2)

# Multidimentional list
t3 = (1,2,3, (4,5)) # 2D
print(t3)

t4 = ( ( (1,2),(3,4) ), ( (5,6),(7,8) ) ) # 3D
print(t4)

# Type Conversion
t5 = tuple('Mujahid')
print(t5) # ('M', 'u', 'j', 'a', 'h', 'i', 'd')

# Single Tuple :: just use comma ,
t6 = ('Mujahid',) 
print(t6)  # ('Mujahid',)
 
## ################### #### Access

print(t1[1]) # 2
print(t1[-1]) # 4 
print(t1[1:3]) # [2.,3]
print(t1[::-1]) # [4, 3, 2, 1]

# BUT for Multi-Dimentional

print(t3[-1][0]) # 4
print(t3[3][0]) # 4
print(t3[-1][-1]) # 5

print(t4[-1][-1][0]) # 7
print(t4[1][1][0]) # 7

## ################### #### Edit

# t1[1]=200
# print(t1) # TypeError: 'tuple' object does not support item assignment

## ################### #### Add :: No addition

## ################### #### Delete :: 

# del

# del t2  # fully delete
# print(t2)

# del t1[0]
# print(t1) # TypeError: 'tuple' object doesn't support item deletion


## ################### #### Operations

# Concatination :

print(t2+t3) # ('Mujahid', 30, True, (5+6j), 1, 2, 3, (4, 5))

# Multiplication
t6 = (2,3,4,5,6)
print(t6*2) # (2, 3, 4, 5, 6, 2, 3, 4, 5, 6)

# Loop :

for i in t6:
    print(i)

# Membership

print(4 in t6) # True

## ################### #### Functions

# len ::
print(len(t6)) # 5
# min :: need numaric
print(min(t6)) # 2
# max :: need numaric
print(max(t6)) # 6
# sorted :: Temporary sorted
print(sorted(t6)) # [2, 3, 4, 5, 6]
print(sorted(t6, reverse=True)) # [6, 5, 4, 3, 2]
# sort :: permanently sorted
# print(t6.sort(reverse=True))
# index
print(t6.index(2)) # 4
# sum
print(sum(t6)) # 20

