####### if else :

email = input('Enter your Email: ')
password = input('Enter your password: ')

if email == 'mujahid@gmail.com' and password == '12345':
    print('Welcome')
else:
    print('Incorrect credentials')

####### Nested if else

email = input('Enter your Email: ')
password = input('Enter your password: ')

if email == 'mujahid@gmail.com' and password == '12345':
    print('Welcome')

elif email == 'mujahid@gmail.com' and password != '12345':
    print('Password Incorrect')
    password = input('Enter your password again: ')

    if password == '12345':
        print('Welcome')
    else:
        print('Password still incorrect')

else:
    print('Incorrect credentials')

######## If @ is not in email, alert shows

email = input('Enter your email: ')
if '@' in email:

    password = input('Enter your password: ')

    if email == 'mujahid@gmail.com' and password == '1234':
        print('Welcome')
    elif email == 'mujahid@gmail.com' and password != '1234':
        print('Password is incorrect')
        password = input (' Enter your password again: ')
        if password == '1234':
            print ('Finally Welcome')
        else:
            print('Password is still incorrect')

    else:
        print('Incorrect credentials')

else:
    print('Email is incorrect')