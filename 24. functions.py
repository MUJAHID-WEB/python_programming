########## Functions :: given input provide output through conditioned procrdd

### Abstraction :: ghost
### Decomposition :: various functions works togather for one app

# define-identifier(parameters):
def is_even(number):
    '''
    Optional docsting which tell about functions
    input- valid integer
    outout - odd/even
    created - Mujahid
    Last edited - 
    '''
    if type(number) == int:

        if number % 2 == 0:
            return 'even'
        else:
            return 'odd'
        
    else:
        return 'Not allowed'

# call
for i in range(1, 11):
    print(is_even(i))

# for Doc print
print(is_even.__doc__)

# or
print(is_even(34))


## How to store in memory location :: pythontutor.com

####################### Parameters vs Arguments

# Monitor Brightness Functinality is 'Parameter' and its value 1-100 is 'Argument'

########### There are 04 arguments:
####### Default

# def power(a,b):
#     return a**b

# print(power(2,3)) # 8
# # print(power(2)) # TypeError: power() missing 1 required positional argument: 'b'
# # print(power()) # TypeError: power() missing 2 required positional arguments: 'a' and 'b'

## To avoid this error :: should use 'Default Argument'

def power(a = 1,b = 1):
    return a**b

print(power(2,3)) # 8
print(power(3)) # 3
print(power()) # 1


######## Positinal

print(power(2,3)) # 8 :: Argumets should call as positioned :: sending argument in a order, parameter receives value in that order

######## Keyword

print(power(b=2, a=3)) # 9 :: if Argumet call by mentioning keyword, its override positional argument :: It is used when dont know the position or oder

######## Arbitrary :: flexible function

def flexy(*number): # It makes input into 'tuple
    product = 1

    print(number) # (1, 2, 3, 4, 5, 6)

    for i in number:
        product = product * i

    return product

# call
print(flexy(1,2,3,4,5,6)) # 720



################# Global Var vs Local Var

def f(y): # 5 comes from f(x)                                   # 3
    x = 1  # New Variable create in Function :: Local Var       # 4
    x += 1  # x = x +1 = 1 + 1                                  # 5
    print(x) # 2                                                # 6

x = 5 # Global Vriable                                          # 1
f(x)  # 5 comes from x = 5                                      # 2
print(x) # destroying functions variable, print 5               # 7

#### If Function does not have any Local Variable, It will use Global Var

def g(y): # 5 comes from f(x)                                   # 3
    print(x) # 5  :: print Global Var                           # 4
    print(x+1) # 6                                              # 5

x = 5 # Global Vriable                                          # 1
g(x)  # 5 comes from x = 5                                      # 2
print(x) # destroying functions variable, print 5               # 6


####  Trying change the value of global variables through functions :: not allowed to chage, just allow to use

# def h(y):                        # 3
#     x += 1 # not allowed         # 4

# x = 5                            # 1
# h(x)                             # 2
# print(x)  # Error                # 

# ---------- global keyword use ------ to change the value
def h(y):                        # 3
    global x
    x += 1 # not allowed         # 4

x = 5                            # 1
h(x)                             # 2
print(x)  # 6                    # 5

##### 

def f(x):                                       # 3
    x =x+1                                      # 4
    print(' in f(x) : x= ', x)  # 4             # 5
    return x                                    # 6

x = 3                                           # 1
z = f(x)                                        # 2
print('in main program scope: z= ', z) # 4      # 7
print('in main program scope: x= ', x) # 3      # 8


######### Nested Function :: will be adstrcted/hidden into main Function.

def f():
    print('Inside f')
    def g():
        print('Inside g')

    g()

print( f() ) # Inside f, Inside g


##### Example

def g(x):                                   # 3
    def h():                                # 7
        x = 'abc' # abc                     # 8
    
    x = x+1                                 # 4
    print('in g(x): x= ', x) # 4            # 5
    h()                                     # 6
    return x  # 4                           # 9

x = 3                                       # 1
z = g(x)                                    # 2




##### ################ Object #########

## Everything (int, str etc) in python is object
## Function is also object 

def f(num):
    return num**2

print( f(2)) # 4
print( f(4)) # 16

x = f # aliasing :: as like aother objects

print( x(2)) # 4 :: because x=f
print( x(4)) # 16 :: because x=f

# if del f, x will work insted :: reference
del f
# print( f(2)) #NameError: name 'f' is not defined

print( x(5)) # 25 :: x works though f delete

###### So, we can:
# Renaming
# deleting
# Storing
# Returning
def func_a():                       # 5
    print('inside func_a')          # 6

def func_c(z):                      # 2
    print('inside func_c')          # 3
    return z()                      # 4

print(func_c(func_a))               # 1

#####

def f():                        #2
    def x(a, b):                #4
        return a + b            #5
    return x                    #3

val = f()(3,4)                  #1
print(val)  #7                  #6

# Function as argument


######## Benefit ::
# Code Modularity
# Code Reusability
# Code Readability