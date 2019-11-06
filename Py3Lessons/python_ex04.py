#Remember to add comments to your code to make sure what you intend to do matches what the code actually does uwu

c = 100 #cars
s = 4 #space or seats in a car
d = 30 #drivers
p = 90 #passengers
n = c - d #cars not driven
r = d #cars driven
t = r * s #carpool capacity
a = p // r #average passengers per car

print ("There are", c, "cars available.")
print ("There are only", d, "drivers available.")
print ("There will be", n, "empty cars today.")
print ("We can transport", t, "people today.")
print ("We have", p, "to carpool today.")
print ("We need to put about", a, "in each car.")

#In the study drills, the reason "car_pool_capacity" didn't work is likely because the name was misspelled.
#ie. it should've been "carpool_capacity".

#also added // to line 10 (math defining average_passengers_per_car) so that it's not a float. I still may not be doing that correctly but we'll see.

#rewritten with only letter variables, and then commented.
