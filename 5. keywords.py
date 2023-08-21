import keyword

print(keyword.kwlist)

# Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

## Identifiers : A name used to identify variable, functions, class, module or other objects

## Rules:
# can only start with 'Alphabet' or _
# followed by 0 or more letter, _ or digits
# keywords cannot be used as an identifier

name = 'Mujahid'
print(name)

_ = 'Mujahid'
print(_)

_name = 'Mujahid'
print(_name)

name_01 = 'Mujahid'
print(name_01)

# 1name = 'Mujahid'  # error
# print(1name)

# del = 'Mujahid'  # error
# print(del)