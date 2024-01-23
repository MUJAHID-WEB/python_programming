######## Variable and memory : Call by object reference



###### Aliasing ::
a = 'Mujahid'
b = a 
c = b

# print(id(a)) # 4364854568
# print(id(b)) # 4364854568
# print(id(c)) # 4364854568

import sys

sys.getrefcount(a) # 4 :: How many variable are point in one memory location


######## Garbage Collection :: python runs programs name 'garbage collector'

# for delete unused memory 

######## Weird Stuff

# WB1

a = 2
b = a 
c = b

sys.getrefcount(a) # 373 :: How many variable are point in one memory location :: actually 4

# WB2

# -5 to 256 same memory location for memory optimization

# WB3
