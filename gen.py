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
#Opening files in python is easy
Xfile = open('X.txt')
Yfile = open('Y.txt')

#create lists from files
#Here we loop through each line in the the files
#We call string() on the lines to make it easier to read, and get rid of weird \n
#then we add those lines to a list of lines as X and Y
X = [line.strip() for line in Xfile]
Y = [line.strip() for line in Yfile]

#s is a string that we want to build
s = "The next big thing is: "

#get a random element in our list of lines.
s = s + random.choice(X) + " for " + random.choice(Y)
print (s)
