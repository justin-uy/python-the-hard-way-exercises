from sys import argv

script, filename = argv

print "We're going to erase %r." % filename

print 'Opening the file...'
target = open(filename, 'w')

print 'Truncating file.'
target.truncate()

print 'write some lines'

line1 = raw_input('line 1:')
line2 = raw_input('line 2:')
line3 = raw_input('line 3:')


print 'write the lines!'

target.write(line1 + '\n')
target.write(line2 + '\n')
target.write(line3 + '\n')

print 'close!'

target.close()

