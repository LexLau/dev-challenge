# Exercises for chapter 2:

# Name:Alex Lau

import math
#Exercise 2.1
print ''
print 'Exercise 2.1'
print ''
#zipcode = 02492
#print zipcode
#zipcode returns error
zipcode = 02132
print 'zipcode 02132 = '
print zipcode
#zipcode returns 1114
zipcode = 01
print 'zipcode 01 = '
print zipcode
zipcode = 010
print 'zipcode 010 = '
print zipcode
zipcode = 0100
print 'zipcode 0100 = '
print zipcode
zipcode = 01000
print 'zipcode 01000 = '
print zipcode
print ''
#returns 1, 8, 512
print 'these values above indicate the binary numbers.'
print 'calling zipcode would return the numbers these binary nubmers represent.'

#Exercise 2.2 also done in python interpreter
print 'Exercise 2.2'
print ''

5
x = 5
x + 1

print 'there is no output because there is no print statement'
print ''
print '5'
x = 5
print 'x = 5'
print 'x + 1'
print x + 1
print ''
#result = 6 Python command prompt

#Exercise 2.3
print 'Exercise 2.3'
print ''
width = 17
height = 12.0
delimiter = '.'

print 'width = 17'
print 'height = 12.0'
print "delimiter = '.'"

print ''
print 'problem 1'
print 'width/2 = '
print width/2

print ''
print 'problem 2'
print 'width/2.0 = '
print width/2.0

print ''
print 'problem 3'
print 'height/3 = '
print height/3

print ''
print 'problem 4'
print '1 + 2 * 5'
print 1 + 2 * 5

print ''
print 'problem 5'
print 'delimiter * 5'
print delimiter * 5
print ''

#Exercise 2.4
print "Exercise 2.4"
print ''

print 'Using python interpreter as a calculator'
print ''

print 'Problem 1'
print 'volume of a sphere, radius = 5?'
volume = (4/3) * math.pi * (5**3)
print volume
print ''

print 'Problem 2'
print 'Total wholesale cost is?'
book = 24.95
discountedBook = 0.6*book
numBooks = 60
shipping = (3) + (numBooks - 1) * 0.75
totalCost = numBooks * discountedBook + shipping
print totalCost
print ''

print 'Problem 3'
print 'What time do I get home for breakfast?'
easyPace = 8.25
fastPace = 7.2
runTime = 2 * easyPace + 3 * fastPace
print 'It takes ', runTime, 'minutes'
print 'I will get home at 7:30'

