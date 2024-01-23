########### Literals : New data given in a variables

### numeric: Integers, Floating, Complex Number
# 
# Int
a = 0b1010 # binary
b = 100 # decimal
c = 0o310 # octal
d = 0x12c # hexa-decimal

print(a,b,c,d)

# float

f_1 = 10.5
f_2 = 1.5e2
f_3 = 1.5e-3

print(f_1, f_2, f_3)

# complex

x = 3.15j

print(x)

### String: sequences of characters surrounded by quotes

string = 'Mujahid'
strings = "This is Mujahid"
char = "C"
multiline_str = """ This is multiline using 03 inverted comma """
unicode = u"\U0001f600\U0001F606"
raw_str = r"raw \n string"

print (string, strings, char, multiline_str, unicode, raw_str)


### boolean: True, False

a = True + 4  # True = 1; 1+4=5
b = False + 10 # False = 0; 0+10= 10

print('a: ', a)
print('b: ', b)

### special: without value any 'variable' cannot be declared, that time use 'None' for using in future

a = None
print(a)