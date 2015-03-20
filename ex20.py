from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Print whole file: \n"
print_all(current_file)

print "rewind!!"
rewind(current_file)

print "one line at a time now!"

def print_n_lines(total, f):
    for current_line in range(1, total + 1):
        print_a_line(current_line, current_file)

print_n_lines(3, current_file)

