# Type Conversion

## Implicit

sum = 4+5.5
print(sum)
type(sum)

## Explicit: int, float, str, bool, complex, list, tuple, set, dictonary

print(int(4+9.5))

# print(int('Dhaka'))  # Error

print(float(4+6))

print(str(4+7))

name = 'Hello'
print(list(name))

print(tuple('Mujahid'))

a = 4.5
print(int(a)) 

############

first_num = input('Enter the first number: ')
second_num = input('Enter the second number: ')

add_result = int(first_num) + int(second_num)
print(add_result)

# For more readability : add type conversion while input

first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))

add_result = first_num + second_num
print(add_result)

