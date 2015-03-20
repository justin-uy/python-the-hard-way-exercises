def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_split(arg1, arg2):
    print 'arg1: %r, arg2: %r' % (arg1, arg2)

def print_one(arg1):
    print 'arg1: %r' % arg1

def print_none():
    print 'nothin\''

first_name = 'Justin'
last_name = 'Uy'

print_two(first_name, last_name)
print_two_split(first_name, last_name)
print_one(first_name)
print_none()

