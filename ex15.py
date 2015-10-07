from sys import argv

# we get the script name and the filename from the user in the terminal
script, filename = argv

# we perform the function open on this thing filename, and then assign
# the product (the file) to the variable txt
txt = open(filename)

print "Here's your file %r:" % filename
# here we call a function on txt called read
# since txt is a file, we call the function using a dot
# so we're saying to the object txt to do a command called read on itself, with parameters in brackets
# no parameters are needed in this case
print txt.read()

# now instead of using argv to get the filename from the user, we use raw_input
print "Type the filename again:"
file_again = raw_input("> ")

# txt_again is the result of opening the file which has been called file_again
txt_again = open(file_again)

# print the results of reading the object txt_again
print txt_again.read()