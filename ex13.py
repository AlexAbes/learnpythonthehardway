# you need to import the 'features' of Python that you need
# these 'features' are actually called modules (or libraries)
# MODULES GIVE YOU FEATURES
from sys import argv
# the argv is the argument variable; it holds the the arguments you pass
# to the Python script when you run it

# this line 'unpacks' argv so that it all the variables it is holding get
# assigned to to four variables, which are listed on the left
# it says "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.""
# ORIGINAL SCRIPT
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# MY OWN SCRIPT

script, first = argv

print "The script is called:", script
age = raw_input("How old are you? ")
print "You are: ", age
print "Another variable is: ", first