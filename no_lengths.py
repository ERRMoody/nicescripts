from ete3 import Tree
import sys


t = Tree(sys.argv[1])


t.write(format=9, outfile =sys.argv[2])
