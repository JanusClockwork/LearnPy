#Make something that can more or less count how many manga vols you have, and be able to update it in real time.

l = 9 #lowercase L is for the shelf levels; how many you have. In my case, it's 9. For right now, this is static.
s = 70 #s is for no. of  individual series. Currently I have 70. No, I'm not counting the Hino Horror books all separately; they are one series. This number should be able to be updated in real time.
v = 35 #v is for volumes per shelf. This number, 35, is going to be static.

print ("I have {x} manga volumes!".format (x = s*v // l))

x = s*v // l

if (x > 100):
    print ("I'm a goddamn nerd.")
else:
    print ("I haven't reached my true potential...")
    
    #note that in python, the else does NOT belong in the if-block. ie. it has the same indent level as the preceeding if.