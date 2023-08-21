###### string : Immutable ( cannot be changed ) data type : sequence of characters : unicode characters
# str object doesn't support item assignment but allow reassign 


## creating string

c = 'Mujahid'
print(c)

c = "Mujahid"
print(c)

c = "It's Mujahid"
print(c)

d = '''Mujahid''' # for multiline
print(d)

a = str('Mujahid')
print(a)

## Accessing String

###############################

# Concept of Indexing
a = "Hello" # each char has index number 
print(a)  # Hello
print(a[4]) # o : in 4th index char is 'o'

# Positive Indexing : : Start from 0 when counted from left side

print(a[1]) # o : in 1st index char is 'e'

# Negative Indexing : : Start from -1 when counted from right side

print(a[-1]) # o : in -1st index char is 'o'

############################

# Concept of Slicing :: Dividing char based on Index : start(included), end(excluded), Skip(-1)

b = 'Mujahidul Islam'

print(b[0:7]) # It will print from 0 index to 6th index char : Mujahid
print(b[3:])  # It will print from 3rd index to last char : ahidul Islam
print(b[:9])  # It will print from 0 index to 8th index char : Mujahidul
print(b[:])  # It will print all char : Mujahidul Islam
print(b[0:7:3]) # It will print from 0 index to 6th index char but skip two char : Mad
print(b[-11:-3:2]) # From 'hidul Is' : It will print from -11th index to -3th index char but skip one char : hdlI
print(b[::-1])  # It will print all char in reverse : malsI ludihajuM
print(b[-1:-6:-1]) # From 'Islam' : It will print from -5th index to -1 index char but in reverse : malsI

################################ 

## Adding Chars to String : : str object doesn't support item assignment
## Editing String : : str object doesn't support item assignment
x = 'Dhaka'
print(x)
# x[1] = 'd' # TypeError: 'str' object does not support item assignment
x = 'BD'
print(x) # But It support reassignment
## Deleting String :: str object doesn't support item deletion

##################################

## Operations on String

# Arithmatic :: + (Concatinate), * (Multiplication)

print('Mujahid'+'ul'+ ' Islam')

print('*' * 10) # **********
print('Mujahid ' * 10) #  Mujahid Mujahid Mujahid Mujahid Mujahid Mujahid Mujahid Mujahid Mujahid Mujahid S

# Relational :: =, ==, !=, >, <

print('mujahid' == 'mujahid') # True
print('mujahid' != 'mujahid') # False
print('Mujahid' > 'Islam') # True :: lexiographically : as per dictionary pattern
print('mujahid' < 'islam') # False :: lexiographically : as per dictionary pattern
print('Mujahid' < 'mujahid') # True :: Capital comes first and small comes next



# Logical :: and, or, not :: '' -> False (empty string), 'Mujahid' -> True (not empty string)
a = True
b = False
print( a or b) # True ; if one value is 'True', answer will be 'True'
print( a and b) # False ; if both value is 'True', answer will be 'True'
print(not b) # True ; if value is 'False', answer will be 'True'
print(not a) # False ; if value is 'True', answer will be 'False'

print('' and 'Dhaka') # '' : both value is 'True', answer will be 'True' BUT '' -> False (empty string), 'Dhaka' -> True (not empty string), SO ans is False = ''

print('' or 'Dhaka') # Dhaka : if one value is 'True', answer will be 'True' BUT '' -> False (empty string), 'Dhaka' -> True (not empty string), SO ans is True = Dhaka

print('Mujahid' and 'Dhaka') # 'Dhaka' : both value is 'True', answer will be 'True' BUT 'Mujahid' -> True (not empty string), 'Dhaka' -> True (not empty string), SO ans is True = 'Dhaka' , cause 'Dhaka' makes this true

print('Mujahid' or 'Dhaka') # 'Mujahid' : if one value is 'True', answer will be 'True' BUT 'Mujahid' -> True (not empty string), 'Dhaka' -> True (not empty string), SO ans is True = 'Mujahid' , cause 'Mujahid' makes this true first.

print(not 'Mujahid') # False ; value is 'True' { 'Mujahid' -> True (not empty string) }, answer will be 'False'

print(not '') # True ; value is 'False' { '' -> False (empty string) }, answer will be 'True'



# Loops on String

y = 'Mujahidul'
for i in y:
    print(i)

for i in y[2:6]:
    print(i) 

# for i in y[2:6:2]:
#     print(i) 

for i in y[2:6:-1]:
    print(i) 

# Membership :: in, not in

print('h' in y) # True

print('H' in y) # False

print('Islam' not in y) # True

############################
## String Functions

# Common Functions: 

# len:
a = 'mujahidul'
print(len(a)) # 7
# max
print(max(a))  # u : Based on ASCII 
# min
print(min(a))  # a : Based on ASCII 
# sorted
print(sorted(a))  # ['a', 'd', 'h', 'i', 'j', 'm', 'u'] : Based on ASCII in ascending order
print(sorted(a, reverse=True))  # ['u', 'm', 'j', 'i', 'h', 'd', 'a'] : Based on ASCII in ascending order

# 1. Capitalize, Title, Upper, Lower, Swapcase

print(a.capitalize()) # Mujahid
print(a.title()) # Mujahid
print(a.upper()) # MUJAHID
print(a.lower()) # mujahid
print(a.swapcase()) # MUJAHID

# 2. count
print(a.count('u')) # 2

# 3. find/index
print(a.find('u')) # 1 : index number
print(a.find('s')) # -1 : index number which is not find in string
print(a.index('u')) # 1 : index number

# 4. endswith/ startswith
print(a.endswith('u')) # False : 
print(a.startswith('m')) # True : 

# 5. format

print('Hello, my name is {} and I am {}'.format('Mujahid', 32)) # Hello, my name is Mujahid and I am 32

print('Hello, my name is {1} and I am {0}'.format('Mujahid', 32)) # Hello, my name is 32 and I am Mujahid

print('Hello, my name is {age} and I am {name}'.format(name = 'Mujahid', age= 32)) # Hello, my name is 32 and I am Mujahid

print('Hello, my name is {name} and I am {weight}'.format(name = 'Mujahid', age= 32, weight = 72)) # Hello, my name is Mujahid and I am 72

# 6. isalnum, isalpha, isdecimal, isdigit, isidentifier

print('FLAT20'.isalnum()) # True : its alphabet and numerical
print('flat'.isalpha()) # True : its alphabet 
print('20'.isdigit()) # True : its digit 
print('hello_world'.isidentifier()) # True : its identifier 

# 7. split

print('Who is the PM of BD ?'.split()) # ['Who', 'is', 'the', 'PM', 'of', 'BD', '?']
print('Who is the PM of BD ?'.split('the')) # ['Who is ', ' PM of BD ?']

# 8. Join

print(' '.join(['Who', 'is', 'the', 'PM', 'of', 'BD', '?'])) # Who is the PM of BD ?

# 9. Replace :

print('My name is Mujahid'.replace('Mujahid', 'Abdullah')) # My name is Abdullah

# 10. Strip

print('          Mujahid        '.strip()) # Mujahid
