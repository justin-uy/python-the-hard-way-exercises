#!/usr/bin/python

print 'something'
print 'something that \n escapes \t and stuff'

multipleLines = '''
something that is
multiple
lines?!
'''

print '---------------'
print multipleLines
print '---------------'

math = 5 + 5 / 2 * 4 - 1

print 'this is the value of math: %d' % math

def someArbitraryFunction(n):
    b = n * 5
    c = b / 20
    d = c / 2

    return b, c, d

n = 1000

b, c, d = someArbitraryFunction(n)

print 'n: %d' % n
print 'b = %d, c = %d, d = %d' % (b, c ,d)

