
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



