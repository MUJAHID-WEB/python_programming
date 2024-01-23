################# Dictionary :: 'key' : 'value'

# Mutable = List/Sets/ Dictionary
# Immutable = String/ Tuples/ Int/ Float/ Boolean/ Complex

##### Rules : 
# has no indexing
# It is mutable types
# keys are Immutable, Values can be mutable
# Keys should be unique

## Create

d = {}
print(d)

d1 = {'Name':'Mujaid', 'Gender':'Male'}
print(d1)

# d2 = {[1,2,3] :'Mujaid', 'Gender':'Male'}  # using list
# print(d2) # TypeError: unhashable type: 'list' :: # keys are Immutable, Values can be mutable

d2 = {(1,2,3):'Mujaid', 'Gender':'Male'} # using tuple
print(d2) # {(1, 2, 3): 'Mujaid', 'Gender': 'Male'} :: keys are Immutable, Values can be mutable

d3 = {'Name':'Mujaid', 'Name':'Islam'} # using same Key
print(d3) # {'Name': 'Islam'} :: # Keys should be unique

d4 = {'Name':'Mujaid', 'Gender':'Male', 'Marks' : {'Math': 96, 'Eng':90, 'CSE': 95}}
print(d4)  # 2D

## ################### Access :: have no indexing/slicing, so access by 'key'

print(d1['Gender']) # Male
print(d4['Marks']['Eng']) # 90

## #################### Add :: key-value pairs

d1['age'] = 32
print(d1) # {'Name': 'Mujaid', 'Gender': 'Male', 'age': 32}

d4['Marks']['Bangla'] = 83
print(d4) # {'Name': 'Mujaid', 'Gender': 'Male', 'Marks': {'Math': 96, 'Eng': 90, 'CSE': 95, 'Bangla': 83}}

## #################### edit

d1['Name'] = 'Mujahidul'
print(d1) # {'Name': 'Mujahidul', 'Gender': 'Male', 'age': 32}

d4['Marks']['Eng'] = 92
print(d4) # {'Name': 'Mujaid', 'Gender': 'Male', 'Marks': {'Math': 96, 'Eng': 90, 'CSE': 92, 'Bangla': 83}}


## #################### Delete

# del

# del d
# print(d)  # fully Deleted

del d1['age']
print(d1) # {'Name': 'Mujahidul', 'Gender': 'Male'}

d3.clear()
print(d3) # {}

## Operation

# Concatination :

# print(d1+d2) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# Multiplication
# print(d2*2) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# Loop :

for i in d4:
    print(i) # Output only keys

# if want to value also:
for i in d4:
    print(i, d4[i])

# Name Mujaid
# Gender Male
# Marks {'Math': 96, 'Eng': 92, 'CSE': 95, 'Bangla': 83}

# Membership

print('Name' in d4) # True :: Key search

## Functions

# len ::
print(len(d4)) # 3
# min :: 
print(min(d4)) # Gender
# max :: 
print(max(d4)) # Name
# sorted :: Temporary sorted
print(sorted(d4)) # ['Gender', 'Marks', 'Name']
print(sorted(d4, reverse=True)) # ['Name', 'Marks', 'Gender']


print(d4.keys()) # dict_keys(['Name', 'Gender', 'Marks'])

print(d4.values()) # dict_values(['Mujaid', 'Male', {'Math': 96, 'Eng': 92, 'CSE': 95, 'Bangla': 83}])









