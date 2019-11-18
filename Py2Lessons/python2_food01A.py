#!/usr/bin/python2.7.17
#drive thru op's questions
startScene = '''
You pull up to the drive thru to order food. The intercom crackles: 
"Hello, welcome to McPy\'s! Can I get your order?"
'''

#the ordered items
sr = "small ramen"
mf = "melon soda"
p = "pocky"
f = "cookies and cream" #the pocky flavor

#to order the food; customer's order
custOrder = "You order: \n\t%s\n\t%s\n\t%s" % (sr, mf, p)
AskFlav = '''
"What flavor do you want for the %s?"
You say you want %s. 
''' % (p, f) #this sequence is getting the pocky flavor

#print out the initial exchange
print startScene
print custOrder
print AskFlav

#list off the ordered items
repeatOrder = "\"Okay, that\'s a %s, a %s and %s %s. Is that correct?\"" % (sr, mf, f, p)

print repeatOrder


#to confirm the order is correct, which it is
validOrder = True

#I want to reply with something other than just "True"
if validOrder == True : 
    print "You say, \"Yeh.\"\n"
    
print "\"Cool. That\'ll be $%.2f at the window.\"" % 9.69 #the price of the order

#end the scenario
print "You say, \"Heh, nice,\" and drive up to the pick up window."