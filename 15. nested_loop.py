# Nested Loop

# *
# **
# ***
# ****
# *****

rows = int(input('Enter your number: '))

for i in range(0, rows + 1):
    for j in range(0, i):
        print('*', end=' ')

    print('')
