

f = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 3\Q3 Answers\Q3X\gohawks3.txt', 'r')
l = f.readline()
l = f.readline()
l = f.readline()

l = l.split()
X=[l[x:x+9] for x in xrange(0, len(l), 9)]
