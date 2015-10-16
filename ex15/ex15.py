from sys import argv

script, filename = argv

with open(filename) as f:
    print "Here's your file %r:" % filename
    print f.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print type(txt_again.read())
txt_again.close()


