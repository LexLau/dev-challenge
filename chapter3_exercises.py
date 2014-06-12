# Exercises for chapter 3:

# Name:Alex Lau

print ''
print 'Exercise 3.1'
print ''

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

repeat_lyrics()

print ''
print 'Move last line to top, what error do you get?'
print "name  'repeat_lyrics' is not defined"
print ''

print 'Exercise 3.2'
print ''
print 'Move call function back, and print_lyrics() to the bottom:'
print "name 'repeat_lyrics' is not defined"
print ''

print 'Exercise 3.3'
print ''

def right_justify(allen):
	space = ' '
	numSpaces = 70 - len(allen)
	print (space * numSpaces) + allen

right_justify('allen')
print ''

print 'Exercise 3.4'
print ''

print 'Problem 1'

def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)
print ''

print 'Problem 2'
print ''
def do_twice(f, arg):
 	f(arg)
 	f(arg)

def print_spam(arg):
	print arg

do_twice(print_spam, 'whatever')
print ''

print 'Problem 3'
print ''

def print_twice(arg):
	print arg
	print arg

print_twice('argument')
print ''

print 'Problem 4'
print ''

do_twice(print_twice, 'spam')
print ''

print 'Problem 5'
print ''

def do_four(f, arg):
	do_twice(f, arg)
	do_twice(f, arg)

do_four(print_twice, 'spam')
print ''

print 'Exercise 3.5'
print ''

print 'Problem 1'
print ''

#edit do_four() nad do_twice() function to take 1 arugment
def do_twice(f):
	f()
	f()
def do_four(b):
	do_twice(b)
	do_twice(b)
def one_four_one(f, g, h):
	f()
	do_four(g)
	h()
def one_two_one(f, g, h):
	f()
	do_twice(g)
	h()
def print_plus():
	print '+', 
def print_dash():
	print '-',
def print_bar():
	print '|', 
def print_space():
	print ' ',
def print_end():
	print ''
def nothing():
	"do nothing"
def print1beam():
	one_four_one(nothing, print_dash, print_plus)
def print1post():
	one_four_one(nothing, print_space, print_bar)
def print2beams():
	one_two_one(print_plus, print1beam, print_end)
def print2posts():
	one_two_one(print_bar, print1post, print_end)
def print_row():
	one_four_one(nothing, print2posts, print2beams)
def print_grid():
	one_two_one(print2beams, print_row, nothing)

print_grid()
print ''

print 'Problem 2'
print ''

#most functinon already defined above
#edited number of rows and columns
def print4beams():
	one_four_one(print_plus, print1beam, print_end)
def print4posts():
	one_four_one(print_bar, print1post, print_end)
def print_row():
	one_four_one(nothing, print4posts, print4beams)
def print_grid():
	one_four_one(print4beams, print_row, nothing)

print_grid()
