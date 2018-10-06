import random

#quick and dirty
times = int(input("How many companies do you want to start? "))

# Open files
Xfile = open('X.txt')
Yfile = open('Y.txt')

#create lists from files
X = [line.strip() for line in Xfile]
Y = [line.strip() for line in Yfile]

for num in range(0,times):
    s = "The next big thing is: "
    s = s + random.choice(X) + " for " + random.choice(Y) + "."
    print (s)
    print("")

print ("bye")
