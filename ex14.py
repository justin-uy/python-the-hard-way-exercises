from sys import argv

script, user_name = argv
prompt = '> '

print 'Do you like me, %s?' % user_name
likes = raw_input(prompt)

print 'Where do you live, %s?' % user_name
lives = raw_input(prompt)

print '''
So you live here: %s
And whether or not you like me? %s
''' % (lives, likes)

