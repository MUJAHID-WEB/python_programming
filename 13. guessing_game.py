import random

jackpot = random.randint(1, 50)
count = 1

guess = int(input('Guess a number to win Jackpot: '))

while guess != jackpot:

    if guess < jackpot:
        print('Guess Higher')
    else:
        print('Guess Lower')

    guess = int(input('You can gues again: '))
    count += 1

print('You won the Jackpot !!!')
print('You took', count, 'attempts')

# jackpot = random.randint(1, 50)
# count = 1
# attempt = 5

# guess = int(input('Guess a number to win Jackpot: '))

# while guess != jackpot:
    

#     if guess < jackpot:
#         print('Guess Higher')
#     else:
#         print('Guess Lower')

#     if guess < attempt:

#         guess = int(input('You can gues again: '))

#         count += 1
    
#     else:
#         print('You Failed !')

# print('You won the Jackpot !!!')
# print('You took', count, 'attempts')