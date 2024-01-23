# Operator:

## Arithmatic:

x = 5
y = 4
print(x + y) # 9
print(x - y) # 1
print(x * y) # 20
print(x / y) # 1.25 # true division
print(x % y) # 1 # Modulus
print(x ** y) # 625 # power
print(x // y) # 1 # Integer Division

## Comparison

print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False
print(x == y) # False
print(x != y) # True


## Logical: or, and, not

a = True
b = False

print( a or b) # True ; if one value is 'True', answer will be 'True'
print( a and b) # False ; if both value is 'True', answer will be 'True'
print(not b) # True ; if value is 'False', answer will be 'True'
print(not a) # False ; if value is 'True', answer will be 'False'

## Bitwise: works on binary value 

m = 2 # 010
n = 3 # 110

print (m & n)           # 2 ; 010+110 = 010 # & = and

print (m | n)           # 3 ; 010-110 = 110 # | = or

print (m >> 2)          # 0 ;  # >> = right shift

print (n << 3)          # 24 ; # << = left shift

print (~m)              # -3 ; # ~ = one's complement

## Assignment: assigning a value to a 'variable'

name = 3
print(name)

name += 30  # name = name + 30
print(name) # 33

#can use all operators
# a++ ; error 


## Identify : identify the memory location. values are in same location or not.

ab = 3
bc = 3

print(ab is bc) # True ; They are in same memory location. They are identical

abc = [1,2,3,4]
bcd = [1,2,3,4]

print(abc is bcd) # False; not in same memory location. They are not identical

abc = [1,2,3,4]
bcd = [1,2,3,4]

print(abc is not bcd) # True; not in same memory location. They are not identical

## Membership: Finding the vlaue is whether in another vlaue

xy = 'Dhaka'
print('D' in xy) # True; 

xy = 'Dhaka'
print('D' not in xy) # False; 

xy = [1,2,3,4]
print(5 not in xy) # True; 5 is not in the list xy

xy = (1,2,3,4)
print(5 in xy) # False; 5 is not in the tuple xy

# It also works in set, dictionary 