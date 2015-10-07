print "What file do you want to open?"
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()