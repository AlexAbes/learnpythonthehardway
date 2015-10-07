# the line below assigns the string of four %r's to the variable formatter
formatter = "%r %r %r %r"

# the line below puts one of the numbers in for % at a time
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# the line below puts the variable formatter in for the % once
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)