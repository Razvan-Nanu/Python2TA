y = input('Enter what car you drive')

try:
    print( '{} is a nice car to have'.format(y))
except:
    print('You forgot to enter your car')
finally:
    print('Thanks for telling us.')
