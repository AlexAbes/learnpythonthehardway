from sys import argv

script, user_name = argv
# we make a variable called prompt, which we set to the character >
prompt = '>'

# if we change the prompt later, we can just change it in the variable
# instead of changing it in every raw_input
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives  = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What gender are you %s?" % user_name
gender = raw_input(prompt)

# Below I combine both the raw_input variables and the argv variable gender
print """
Alright, so you have said %r about liking me.
You live in %s. Not sure where that is.
And you have a %r computer. Nice. You're also %s.
""" % (likes, lives, computer, gender)