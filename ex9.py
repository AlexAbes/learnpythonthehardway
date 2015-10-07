days = "Mon Tue Wed Thu Fri Sat Sun"
# I'm guessing the \n makes the next month on a new line when printed
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# what I don't understand here:
# how does it know to put the variable days in this string: there's no formatter required
print "Here are the days: ", days
print "Here are the months: ", months

# The three double-quotes seems to be making sure that
# when I write on a new line in the code, the
# words actually appear on a new line when printed
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""