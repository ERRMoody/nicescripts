from ete3 import Tree
import sys
counter = 0
f = open(sys.argv[1])
for line in f:
    counter += 1
    t = Tree(line, format=1)
    out = str(sys.argv[1]) + '_file_' + str(counter)
    t.write(format=9,outfile=out)
