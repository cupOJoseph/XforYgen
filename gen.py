import random

'''
People come up to you and say, "I have the next big thing... it's X for Y"

Examples include:
- Uber for dog walkers
- Yelp for bonsai growers
- Snapchat for babies

This generation script helps you determine what the next big thing
is really going to be.
'''

# Open files
Xfile = open('X.txt')
Yfile = open('Y.txt')

#create lists from files
X = [line.strip() for line in Xfile]
Y = [line.strip() for line in Yfile]

s = "The next big thing is: "
s = s + random.choice(X) + " for " + random.choice(Y)
print (s)
