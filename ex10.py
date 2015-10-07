# the \t makes the rest of the sentence one tab in
tabby_cat = "\tI'm tabbed in."
# the \n puts what comes after on a new line
persian_cat = "I'm split \non a line."
# the double backslash is printed as one backslash
# because one backslash is interpreted by python as a 
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list;
\t* Cat food
\t * Fishies
\t * Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat