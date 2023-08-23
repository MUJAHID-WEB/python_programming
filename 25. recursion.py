
############### Recursion :: function calls itself :: loop not need

##### Iterative vs Recursive

# a * b :: multiplication is the repeated time addition

#### Functions
def multiply(a,b):
    result = 0

    for i in range(b):
        result = result + a

    print(result)

multiply(3,4)   # 12

#### Recursion :: 5*6
def mul(a,b):
    if b == 1:
        return a
    else:
        return a + mul(a,b-1)
print(mul(5,6))  # 30

## Factorial Recursion :: 5!
def factorial(number):
    if number == 1:
        return 1
    else:
        # 5 = 5*4!
        return number * factorial(number-1)

print(factorial(5))  # 120

#### Palindrome :: madam :: removing 'first' and 'last' char, ramain 'one' char 

def palindrome(text):
    if len(text) <= 1:
        print('Palindrome')

    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        else:
            print('Not Palindrome')

palindrome('madam')
palindrome('malayalam')
palindrome('maam')
palindrome('python')


####### Rabbit Problem :: 
### If 2 newborn rabbits are put in a pen, How many rabbits will be in the pen after 01 year?
## Rules: Assume that Rabbits -
# always produce one male and one female offspring
# can reproduce one every month
# can reproduce one they are one month old
# No one die

### 1,2,3,5,8,13,21,34,55,89,144,233 (fibonacci series)

def fib(m):
    if m==0 or m==1:
        return 1
    else:
        result = fib(m-1) + fib(m-2)
        return result
    
print(fib(12)) # 233 

## Memorization :: by using this above code will be run smoothly for big data :: storing fib(1), fib(2), etc :: space used but time reduce :: dynamic Programming
import time 
def fibonacci(m,d):
    if m in d:
        return d[m]
    else:
        d[m] = fibonacci(m-1,d) + fibonacci(m-2,d)
        return d[m]

start = time.time()
d = {0:1, 1:1}
print(fibonacci(48, d)) # 7778742049

print(time.time()-start) # 1.5735626220703125e-05

print(fibonacci(60, d)) # 2504730781961 :: time consume 

print(time.time()-start) # 2.7179718017578125e-05

#### Power set :: {1,2} = { {},{1},{2},{1,2} }



