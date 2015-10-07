name = 'Zed A. Shaw'
age = 35 
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_ft = height / 12
weight_in_kg = weight / 2.2


# %s refers to a string variable whereas %d refers to a number variable
print "Let's talk about %s." % name
print "He's %d inches tall, which is %d feet tall" % (height, height_in_ft)
print "He's %d pounds heavy, which is %d kg heavy." % (weight, weight_in_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are unusually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
