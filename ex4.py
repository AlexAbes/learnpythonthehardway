# these things are just assigning a value to the variable names
cars = 100
space_in_a_car = 4.00
drivers = 30
passengers = 90
# the variable below takes the # of drivers away from the # of cars
cars_not_driven = cars - drivers
# the # of cars driven must be equal to the # of drivers
# Should we do things like assign one variable name to another variable?
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# my own variable below finds the minimum number of cars needed
cars_needed = passengers / space_in_a_car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
# the round function rounds up the number in brackets
print "Or we can just use", round(cars_needed) , "cars."