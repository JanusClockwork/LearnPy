#How 'bout a Dragalia team builder lmao
from sys import argv

s, e1, e2, e3, e4 = argv #user can create 4 elements, ***s is just the script***
#***you MUST make a variable for the script because that is part of the unpacking.***
#do I need the definitions first??
#the answer is no -- the "definitions" come at the very beginning, before you even run the code.

print "Get ready to build your very own Dragalia Lost team!\n" #the intro text

#first adventurer, uses the first element, e1
print "Your first adventurer\'s element is: ", e1
print "What is your %s adventurer\'s name?  " % e1
n1 = raw_input() #name the first adventurer

#second adventurer, uses the second element, e2
print "\nYour second adventurer\'s element is: ", e2
print "What is your %s adventurer\'s name?  " % e2
n2 = raw_input() #name the second adventurer

#third adventurer, e3
print "\nYour third adventurer\'s element is: ", e3
print "What is your %s adventurer\'s name?  " % e3
n3 = raw_input() #third one's name

#fourth, e4
print "\nYour fourth adventurer\'s element is: ", e4
print "What is your %s adventurer\'s name?  " % e4
n4 = raw_input() #fourth one's name


#sum up everything here
print """\nHere is your Dragalia Lost team!\n
\t+ %s, %s\n
\tx %s, %s\n
\t+ %s, %s\n
\tx %s, %s\n
""" % (n1, e1, n2, e2, n3, e3, n4, e4)

#conclusion text
print "How cool! Your team will do great!"
