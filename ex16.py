from sys import argv

print "What file do you want to play with?"
filename = raw_input("> ")

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."
# control-c just takes you out of the python shell
# hitting return seems to advance the script to the next line

raw_input("?")

target = open(filename, 'r')

print target.read()

print "Opening the file..."
# the file object created by using the open function on the filename
# is assigned to the variable target
# it is opened in write mode
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# this function deletes everything in the target variable, which is our file object
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file"

# there is a quicker and DRY-er way of doing the writing than below
# but I haven't been able to find it
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()