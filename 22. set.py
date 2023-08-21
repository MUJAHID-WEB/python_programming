######### Sets :: 

### Rules: 
# 1. Dont allow duplicates
# 2. have no indexing/slicing
# 3. dont allow mutable data types
# 4. It itself is a mutable data types

#################### Create ::
# s= {} # {} is used for dictionary. So empty set not created

s1 = set()
print(s1) # set() :: empty set

s2 = {1,2,3,4,5}
print(s2)  # {1, 2, 3, 4, 5} :: Homogenous

s3 = {'Mujahid', 4.5, True}
print(s3)  # {'Mujahid', True, 4.5} :: Heterogenous

s4 = {1,1,2,2,3,3}
print(s4) # {1, 2, 3} ::  Dont allow duplicates

# s5 = { [1,2,3], 'Mujahid'}  # with list
# print(s5) # TypeError: unhashable type: 'list' :: dont allow mutable data types

s6 = { (1, 3,5), 'Mujahid' } # with tuples
print(s6) # {'Mujahid', (1, 3, 5)} :: Sets have no indexing :: Hasshing

# s7 = { {1,2}, {3,4} } # 2D, 3D cannot be created
# print(s7) # unhashable type: 'set' :: dont allow mutable data types

################ Access :: cannot access

# print(s2[1]) # 'set' does not support indexing :: have no indexing/slicing

################ Edit :: cannot edit 

################# Add :: It itself is a mutable data types

s2.add(6)
print(s2) # {1, 2, 3, 4, 5, 6} 
print(id(s2)) # 4364178528 :: memory location

s2.add(7)
print(s2) # {1, 2, 3, 4, 5, 6, 7} 
print(id(s2)) # 4364178528 :: memory location


################# Delete :: 

# del

# del s3
# print(s3)

# del s2[-1]
# print(s2) # TypeError: 'set' object doesn't support item deletion

# remove

s2.remove(7)
print(s2) # {1, 2, 3, 4, 5, 6} 

# pop

s2.pop()
print(s2) # {2, 3, 4, 5, 6}

################### Operation ::

# Concatination :

# print(s2+s3) # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# Multiplication
s7 = {2,3,4,5,6,7,8}
# print(s7*2) # TypeError: unsupported operand type(s) for *: 'set' and 'int'

# Loop :

for i in s7:
    print(i)

# Membership

print(4 in s7) # True

################### Function ::

# len ::
print(len(s7)) # 7
# min :: need numaric
print(min(s7)) # 2
# max :: need numaric
print(max(s7)) # 8
# sorted :: Temporary sorted
print(sorted(s7)) # [2, 3, 4, 5, 6, 7, 8]
print(sorted(s7, reverse=True)) # [8, 7, 6, 5, 4, 3, 2]
# sum
print(sum(s7)) # 35

# union
print(s2.union(s7)) # {2, 3, 4, 5, 6, 7, 8}
# inter-section
print(s2.intersection(s7)) # {2, 3, 4, 5, 6}
# difference
print(s2.difference(s7)) # set()
print(s7.difference(s2)) # {8, 7}
print(s7.symmetric_difference(s2)) # {7, 8} :: both haven't

print(s7.isdisjoint(s2)) # False :: common item check

print(s7.issubset(s2)) # False :: common item check and 

print(s7.issuperset(s2)) # True :: Is s7 is superset of s2

s3.clear() 
print(s3) # set()
