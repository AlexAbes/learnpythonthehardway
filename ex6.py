# The variable below is a string with a number inserted into it
x = "There are %d types of people." % 10
# The variable below is a string
binary = "binary"
# The variable below is a string
do_not = "don't"
# The variable below is a string with two strings inserted into it
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# The below line prints a string, with a string inserted into it using %r
print "I said: %r." % x
# The below line prints a string, with a string inserted into it using %r
print "I also said: '%s'." % y

# The below line assigns the variable hilarious a value true or false
# I think this is different from assigning it the string "true" or "false"
hilarious = True
# The variable is assigned as a string with a variable inserted into it.
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e