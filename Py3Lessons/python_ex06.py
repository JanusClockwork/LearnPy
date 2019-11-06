x = "There are %d types of people." % 10 #statement 1
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #statement 2

#when these statements are printed, the variables should be placed and complete the joke.
print (x)
print (y)

#and now to explain the joke
print ("I said: %r." % x)
print ("I also said: '%s'." % y)

#determining if the joke is funny is a boolean
hilarious = False #note that False must be capitalized so that it's recognized as a bool result, not just a variable name.
joke_eval = "Isn't that joke so funny?! %r" #%r to literally spell out the boolean result (true or false)

#ask and get the bool result
print (joke_eval % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e) #lets statement e complete statement w
#notice that + works even tho this is not a mathematical equation.
#this is because it is kinda just adding the two statements. Together, they make this one long string.

#A-HA!! r% stands for 'raw data' SO I WAS RIGHT it's just the literal data. yussssss