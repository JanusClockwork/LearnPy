from sys import argv

script, user_name, sname = argv #sname is the third argument for Study Drill 3.
#sname is to give the script a "human" name
prompt = '---> ' #note this is a character, not a string. You can make it a string tho.

print "Hi %s, I\'m %s." % (user_name, sname)
print "I\'d like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt) #this is to start with the prompt then allow for input

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#remember for string blocks, you don't necessarily need \n for line breaks.